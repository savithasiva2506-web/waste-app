from flask import Flask, request, jsonify
from flask_cors import CORS
import os

# Create app FIRST
app = Flask(__name__)

# Enable CORS
CORS(app)

# 🔥 AI Logic (Multiple Suggestions)
def match_waste(waste_type):
    waste_type = waste_type.lower()

    if "plastic" in waste_type:
        return [
            "Plastic Recycling Industry",
            "Packaging Industry",
            "Road Construction Use"
        ]

    elif "food" in waste_type or "organic" in waste_type:
        return [
            "Biogas Plant",
            "Compost Unit",
            "Animal Feed Industry"
        ]

    elif "metal" in waste_type:
        return [
            "Metal Recycling Industry",
            "Automobile Industry",
            "Construction Industry"
        ]

    elif "chemical" in waste_type or "water" in waste_type:
        return [
            "Water Treatment Plant",
            "Chemical Processing Unit"
        ]

    else:
        return [
            "General Recycling Facility",
            "Waste Sorting Unit"
        ]

# 🔹 Home route (for testing)
@app.route("/")
def home():
    return "Backend is running 🚀"

# 🔹 API route
@app.route("/match", methods=["POST"])
def match():
    data = request.json
    waste = data.get("waste", "")

    result = match_waste(waste)

    return jsonify({
        "suggestion": result,
        "co2_saved": "20kg CO2"
    })

# 🔥 IMPORTANT for Render deployment
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))