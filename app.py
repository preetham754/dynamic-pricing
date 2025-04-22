from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from pymongo import MongoClient
import pandas as pd
import joblib
import numpy as np
import datetime
from bson import ObjectId

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Required for session management

# MongoDB setup
client = MongoClient("mongodb://localhost:27017/dp")
db = client["dp"]
collection = db["products"]
print("Connected to MongoDB!")

# Load trained ML model
model = joblib.load("pricing_model.pkl")

@app.route("/")
def home():
    # Recalculate and update prices on each page load
    products = list(collection.find({}))
    for product in products:
        demand = product.get("demand", 100)  # Default to 100 if missing
        competitor_price = product.get("competitor_price", 500)  # Default to 500 if missing

        features = np.array([demand, competitor_price]).reshape(1, -1)
        new_price = model.predict(features)[0]

        # Use string _id directly if stored as string
        result = collection.update_one(
            {"_id": product["_id"]},  # Assumes _id is string like "P001"
            {"$set": {"optimal_price": round(new_price, 2), "last_updated": datetime.datetime.now()}}
        )
        print(f"Update result for {product['_id']}: {result.modified_count} document(s) updated")
        if result.modified_count == 0:
            print(f"No update for {product['_id']}. Check _id or document.")

    # Reload products with updated prices
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

@app.route("/add_to_cart", methods=["POST"])
def add_to_cart():
    data = request.json
    product_id = data["id"]
    product = collection.find_one({"_id": product_id}, {"_id": 1, "name": 1, "optimal_price": 1})

    if not product:
        return jsonify({"error": "Product not found"}), 404

    cart = session.get("cart", {})
    if product_id in cart:
        cart[product_id]["quantity"] += 1
    else:
        cart[product_id] = {
            "name": product["name"],
            "price": product["optimal_price"],
            "quantity": 1
        }

    session["cart"] = cart
    session.modified = True
    return jsonify({"message": "Added to cart!", "cart": cart})

@app.route("/cart")
def cart():
    cart_items = session.get("cart", {})
    total_price = sum(item["price"] * item["quantity"] for item in cart_items.values())
    return render_template("cart.html", cart_items=cart_items, total_price=total_price)

@app.route("/checkout", methods=["POST"])
def checkout():
    session.pop("cart", None)
    return jsonify({"message": "Order placed successfully!"})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5089)