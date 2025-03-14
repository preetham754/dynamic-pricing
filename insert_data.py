from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/dp")
db = client["dp"]
collection = db["products"]

products = [
    {"_id": "P001", "name": "Laptop ABC", "base_price": 900, "optimal_price": 750, "demand": 500, "competitor_price": 700, "season": 1},
    {"_id": "P002", "name": "Smartphone XYZ", "base_price": 800, "optimal_price": 550, "demand": 500, "competitor_price": 500, "season": 0},
    {"_id": "P003", "name": "Headphones 123", "base_price": 80, "optimal_price": 95, "demand": 300, "competitor_price": 85, "season": 1},
    {"_id": "P004", "name": "Smartwatch 456", "base_price": 200, "optimal_price": 230, "demand": 150, "competitor_price": 210, "season": 0},
]

collection.insert_many(products)
print("Products inserted successfully!")
