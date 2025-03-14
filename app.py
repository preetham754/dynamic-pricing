from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
import pandas as pd
import joblib
import numpy as np
import datetime

app = Flask(__name__)

# MongoDB setup
client = MongoClient("mongodb://localhost:27017/dp")
db = client["dp"]
collection = db["products"]

# Load trained ML model
model = joblib.load("pricing_model.pkl")

@app.route("/")
def home():
    products = list(collection.find({}))
    for product in products:
        product["_id"] = str(product["_id"])  # Convert ObjectId to string
    return render_template("index.html", products=products)

@app.route("/get_prices", methods=["GET"])
def get_prices():
    """Returns updated product prices"""
    products = list(collection.find({}, {"_id": 1, "name": 1, "optimal_price": 1}))
    
    for product in products:
        product["_id"] = str(product["_id"])  # Convert ObjectId to string
    
    return jsonify(products)

@app.route("/update_prices", methods=["POST"])
def update_prices():
    """Recalculates and updates product prices dynamically"""
    products = list(collection.find({}))

    for product in products:
        demand = product.get("demand", 100)
        competitor_price = product.get("competitor_price", 500)
        season = product.get("season", 0)

        features = np.array([demand, competitor_price, season]).reshape(1, -1)
        new_price = model.predict(features)[0]

        collection.update_one(
            {"_id": product["_id"]},
            {"$set": {"optimal_price": round(new_price, 2), "last_updated": datetime.datetime.now()}}
        )

    return jsonify({"message": "Prices updated successfully!"})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5009)
