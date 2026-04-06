from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import random

app = Flask(__name__)
CORS(app)

# 🔥 Smart AI Logic
def match_waste(waste, quantity):
    waste = waste.lower()

    # Normalize input (smart understanding)
    if "bottle" in waste:
        waste = "plastic"
    elif "leftover" in waste or "food" in waste:
        waste = "food"
    elif "iron" in waste or "scrap" in waste:
        waste = "metal"

    locations = ["Chennai", "Coimbatore", "Erode"]

    if "plastic" in waste:
        base_co2 = 25
        results = [
            {
                "industry": "Plastic Recycling Plant",
                "usage": "Used to manufacture new plastic products"
            },
            {
                "industry": "Packaging Industry",
                "usage": "Used for packaging materials"
            },
            {
                "industry": "Road Construction",
                "usage": "Used in plastic roads"
            }
        ]

    elif "food" in waste:
        base_co2 = 15
        results = [
            {
                "industry": "Biogas Plant",
                "usage": "Used to produce biogas energy"
            },
            {
                "industry": "Compost Unit",
                "usage": "Used to create organic fertilizer"
            },
            {
                "industry": "Animal Feed Industry",
                "usage": "Used as livestock feed"
            }
        ]

    elif "metal" in waste:
        base_co2 = 30
        results = [
            {
                "industry": "Metal Recycling Industry",
                "usage": "Reused in manufacturing"
            },
            {
                "industry": "Automobile Industry",
                "usage": "Used in vehicle parts"
            },
            {
                "industry": "Construction Industry",
                "usage": "Used in building structures"
            }
        ]

    else:
        base_co2 = 10
        results = [
            {
                "industry": "General Recycling Facility",
                "usage": "Basic waste processing"
            }
        ]

    # 🔥 Add dynamic fields
    for item in results:
        item["co2_saved"] = base_co2 * quantity
        item["location"] = random.choice(locations)

    return results


@app.route("/")
def home():
    return "Backend is running 🚀"


@app.route("/match", methods=["POST"])
def match():
    data = request.json

    waste = data.get("waste", "")
    quantity = int(data.get("quantity", 1))

    results = match_waste(waste, quantity)

    return jsonify({
        "results": results
    })


# 🔥 Render deployment
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))