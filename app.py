from flask import Flask, request, jsonify

app = Flask(__name__)

# Route to return student number
@app.route('/')
def home():
    return jsonify({"student_number": "200607983"})

# Webhook route for Dialogflow
@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json()

    # Extract the intent name
    intent = req.get('queryResult', {}).get('intent', {}).get('displayName', '')

    if intent == "GetWeatherInfo":
        # Extract city from user input
        city = req.get('queryResult', {}).get('parameters', {}).get('city', 'Unknown Location')
        response_text = f"The current weather in {city} is sunny and 25°C."
    else:
        response_text = "Sorry, I couldn't understand that intent."

    return jsonify({
        "fulfillmentText": response_text
    })

if __name__ == '__main__':
    app.run(debug=True)
