from flask import Flask,jsonify,request
from flask_cors import CORS
import spacy
import random

# Initializing flask app
app = Flask(__name__)
CORS(app)		

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

rules = {
    "greetings": [
        {"text": "Hi there!", "clickable": False},
        {"text": "Hello!", "clickable": False},
        {"text": "Hey!", "clickable": False},
        {"text": "Hi!", "clickable": False},
        {"text": "Howdy!", "clickable": False}
    ],
    "how_are_you": [
        {"text": "I'm doing well, thanks!", "clickable": False},
        {"text": "I'm good. How about you?", "clickable": False},
        {"text": "I'm just a chatbot, but I'm here to help!", "clickable": False}
    ],
    "goodbye": [
        {"text": "Goodbye!", "clickable": False},
        {"text": "See you later!", "clickable": False},
        {"text": "Have a great day!", "clickable": False}
    ],
    "ask_name": [
        {"text": "I'm just a chatbot, but you can call me ChatGPT.", "clickable": False},
        {"text": "I don't have a name, but you can call me Chatbot.", "clickable": False}
    ],
    "main menu": [
        {"text": "Services", "clickable": True},
        {"text": "Products", "clickable": True},
        {"text": "Request Price/Quote", "clickable": True},
        {"text": "Branches", "clickable": True},
        {"text": "Contact Us", "clickable": True},
        {"text": "About Us", "clickable": True},
        {"text": "Clients", "clickable": True}
    ],
    "services": [
        {"text": "Pest Control", "clickable": True},
        {"text": "Fumigation Service", "clickable": True},
        {"text": "Silo Fumigation", "clickable": True},
        {"text": "Sanitization", "clickable": True},
        {"text": "Other Services", "clickable": True}
    ],
    "products": [
        {"text": "RodeXit Proofing Strip", "clickable": True},
        {"text": "AedesX Smart Gravitrap", "clickable": True},
        {"text": "FLYght Traps", "clickable": True}
    ],
    "request price/quote": [
        {"text": "https://docs.google.com/forms/d/1Ae_Zo1efdL6HSdk9KCeOJLrUAZWSGWDj7UnYMJNopoA/viewform?edit_requested=true", "clickable": False}
    ],
    "branches": [
        {"text": "Pune", "clickable": False},
        {"text": "Hyderabad", "clickable": False},
        {"text": "Mumbai", "clickable": False},
        {"text": "Belgaum", "clickable": False},
        {"text": "Nagpur", "clickable": False},
        {"text": "Aurangabad", "clickable": False},
        {"text": "Amravati", "clickable": False},
        {"text": "Indore", "clickable":False},
        {"text": "Nizamabad", "clickable": False}
    ],
    "contact us": [
        {"text": "Seva Facility Services Pvt. Ltd. Office No. 406, 4th Floor Biz Building, Above Axis Bank S. No. 203, Bhondve Chowk Ravet, Pune - 412101 Contact: +91 7219241555 Mail: info@sevafacility.com", "clickable": False}
    ],
    "about us": [
        {"text": "https://sevafacility.com/about-us.html", "clickable": False}
    ],
    "clients": [
        {"text": "Bosch Chassis System Pvt Ltd", "clickable": False},
        {"text": "Flash Electronics", "clickable": False},
        {"text": "IDBI bank", "clickable": False},
        {"text": "Parekh Integrated", "clickable": False},
        {"text": "Podar International School", "clickable": False},
        {"text": "Sony India Pvt Ltd", "clickable": False},
        {"text": "Tata Chemicals Ltd", "clickable": False},
        {"text": "Silver Gardenia Society", "clickable": False},
        {"text": "Shree Trading Company", "clickable": False}
    ],
    "pest control": [
        {"text": "Cockroach Management", "clickable": True},
        {"text": "Ant Management", "clickable": True},
        {"text": "Bed bug Management", "clickable": True},
        {"text": "Rodent Management", "clickable": True},
        {"text": "Fly Management", "clickable": True},
        {"text": "Mosquito Management", "clickable": True},
        {"text": "Termite Management", "clickable": True},
        {"text": "Wood Borer Management", "clickable": True},
        {"text": "Lizard Management", "clickable": True},
        {"text": "Spider Management", "clickable": True},
    ],
}


def respond_to_input(input_text):
    # Tokenize the input text
    doc = nlp(input_text.lower())

    # Check for greetings
    for token in doc:
        if token.text in ["hello", "hi", "hey", "howdy"]:
            return random.choice(rules["greetings"])

    input_text_lower = input_text.lower()
    if input_text_lower in rules:
        response = rules[input_text_lower]
        if isinstance(response, list):
            return response
        return [response]

    # If no matching rules, return a default response
    return ["I'm sorry, I don't understand that."]         
           
# Route for seeing a data
@app.route('/data',methods=['POST'])
def get_data():
     user_input = request.json.get('user_input', '')
     response = respond_to_input(user_input)
     return jsonify({"response": response})
	
# Running app
if __name__ == '__main__':
	app.run(debug=True)

















# from flask import Flask, render_template, request

# app = Flask(__name__)

# # Your chatbot code goes here
# import spacy

# # Load the spaCy model
# nlp = spacy.load("en_core_web_sm")

# # Define some example rules
# rules = {
#     "greetings": ["Hi there!", "Hello!", "Hey!", "Hi!", "Howdy!"],
#     "how_are_you": ["I'm doing well, thanks!", "I'm good. How about you?", "I'm just a chatbot, but I'm here to help!"],
#     "goodbye": ["Goodbye!", "See you later!", "Have a great day!"],
#     "ask_name": ["I'm just a chatbot, but you can call me ChatGPT.", "I don't have a name, but you can call me Chatbot."],
# }

# # Define a function to handle user input
# def respond_to_input(input_text):
#     # Tokenize the input text
#     doc = nlp(input_text.lower())

#     # Check for greetings
#     for token in doc:
#         if token.text in ["hello", "hi", "hey", "howdy"]:
#             return rules["greetings"]

#     # Check for how are you
#     if "how are you" in input_text.lower():
#         return rules["how_are_you"]

#     # Check for goodbye
#     if "bye" in input_text.lower():
#         return rules["goodbye"]

#     # Check for asking the chatbot's name
#     if "name" in input_text.lower():
#         return rules["ask_name"]

#     # If no matching rules, return a default response
#     return ["I'm sorry, I don't understand that."]

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/chat', methods=['POST'])
# def chat():
#     user_input = request.form['user_input']
#     response = respond_to_input(user_input)
#     return {'response': response[0]}

# if __name__ == '__main__':
#     app.debug = True
#     app.run()


