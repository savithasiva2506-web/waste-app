from flask import Flask, request, jsonify, send_file
import pandas as pd

data = {
    "waste": ["plastic", "metal", "food"],
    "industry": ["Recycling Plant", "Metal Works", "Biogas Plant"]
}

df = pd.DataFrame(data)

def match_waste(waste_type):
    for i in range(len(df)):
        if waste_type in df["waste"][i]:
            return df["industry"][i]
    return "General Industry"
from flask_cors import CORS
CORS(app)

app = Flask(__name__)

# Simple AI Logic (Rule-based)
def match_waste(waste_type):
    waste_type = waste_type.lower()

    if "plastic" in waste_type:
        return "Plastic Recycling Industry"
    elif "organic" in waste_type or "food" in waste_type:
        return "Biogas Plant / Compost Unit"
    elif "metal" in waste_type:
        return "Metal Recycling Industry"
    elif "water" in waste_type or "chemical" in waste_type:
        return "Water Treatment Plant"
    else:
        return "General Recycling Facility"

@app.route("/")
def home():
    return send_file("index.html")

@app.route("/match", methods=["POST"])
def match():
    data = request.json
    waste = data.get("waste")

    result = match_waste(waste)

    return jsonify({
        "suggestion": result,
        "co2_saved": "20kg CO2"
    })

if __name__ == "__main__":
    app.run(debug=True)
def match_waste(waste_type):
    waste_type = waste_type.lower()

    if "plastic" in waste_type:
        return [
            "Plastic Recycling Industry",
            "Packaging Industry",
            "Road Construction Use"
        ]

    elif "food" in waste_type:
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

    else:
        return [
            "General Recycling Facility",
            "Waste Sorting Unit"
        ]