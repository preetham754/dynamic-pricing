Dynamic Pricing System
Overview
This project is a web-based Dynamic Pricing System inspired by Amazon, designed to adjust product prices in real-time based on demand and competitor prices using machine learning. Built with Python (Flask), MongoDB, and a Linear Regression model, it features an e-commerce-style UI with a shopping cart and checkout functionality. The project showcases my skills in web development, database management, and data science, leveraging my GUVI & HCL Python Certification (October 2024).
Features

Dynamically updates product prices on page refresh using a trained ML model.
Stores product data in MongoDB with real-time price optimization.
User-friendly Amazon-like interface built with HTML, CSS, and Bootstrap.
Shopping cart and checkout system with session management.
Integrates a machine learning model to predict optimal prices.

Technologies Used

Backend: Python, Flask
Database: MongoDB
Machine Learning: scikit-learn, joblib
Frontend: HTML, CSS, Bootstrap
Other: pandas, numpy

Prerequisites

Python 3.8+
MongoDB (local instance running on port 27017)
Required Python packages: flask, pymongo, pandas, numpy, scikit-learn, joblib

Installation

Clone the repository:git clone https://github.com/your-username/dynamic-pricing.git
cd dynamic-pricing


Install dependencies:pip install -r requirements.txt


Set up MongoDB:
Ensure MongoDB is installed and running locally (mongod).
Create a database named dp with a collection products.


Prepare the model:
Run model.py to train and save the pricing_model.pkl file:python model.py


Ensure salesdata.csv is in the project directory.


Insert sample data (optional):
Use a script or MongoDB shell to add products (e.g., from the provided sample data).


Run the application:python app.py


Access the app at http://0.0.0.0:5009/.



Usage

Visit the homepage to view products with dynamically updated prices.
Add items to the cart and proceed to checkout.
Prices refresh automatically on each page load based on the ML model.

Project Structure
dynamic-pricing/
│
├── app.py            # Flask application logic
├── model.py          # Machine learning model training
├── index.html        # Main UI template
├── salesdata.csv     # Sample dataset for model training
├── static/           # Folder for images (e.g., m1.webp, m2.webp, h1.webp)
├── templates/        # HTML templates (index.html, cart.html)
├── pricing_model.pkl # Trained ML model
├── requirements.txt  # Python dependencies
└── README.md         # This file

Sample Data
The salesdata.csv includes:

demand,competitor_price,price
100,50,55
200,45,60
150,47,58
300,55,70
400,60,75

Product examples in MongoDB:

_id: "P001", name: "Samsung S24+", demand: 500, competitor_price: 200, optimal_price: 749.99
_id: "P002", name: "Iphone 16", demand: 100, competitor_price: 200, optimal_price: 559.99

Future Improvements

Add a scheduler to update prices periodically instead of on every refresh.
Incorporate more features (e.g., user authentication, payment integration).
Expand the ML model with additional features (e.g., season, category).

Credits

Developed by [Your Name] as a personal project.
Inspired by GUVI’s Python course and IIT Madras certification.
Uses open-source libraries and Bootstrap for styling.

License
This project is for educational purposes only. Feel free to fork and modify, but please credit the original author.
Contact

LinkedIn: [Your LinkedIn Profile]
Email: [Your Email]
Open to collaboration or job opportunities in tech!


