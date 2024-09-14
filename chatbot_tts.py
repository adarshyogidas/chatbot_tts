!sudo apt-get install espeak
!pip install pyttsx3

import nltk
import random
import string  # for string operations
import pyttsx3  # for Text-to-Speech

# Initialize the TTS engine explicitly with the 'espeak' driver
engine = pyttsx3.init(driverName='espeak') 

# Function to speak the chatbot's response
def speak_response(response):
    engine.say(response)
    engine.runAndWait()

# Download required NLTK data files
nltk.download('punkt')  # Tokenizer model
nltk.download('wordnet')  # WordNet corpus

# Import tokenizer and stemmer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

lemmatizer = WordNetLemmatizer()

# Simple dataset
data = {
    "greetings": {
        "patterns": ["hello", "hi", "greetings", "hey", "what's up"],
        "responses": ["Hello!", "Hi there!", "Greetings!", "Hey!", "Hello, how can I help you today?"]
    },
    "goodbye": {
        "patterns": ["bye", "goodbye", "see you later", "take care"],
        "responses": ["Goodbye!", "See you later!", "Take care!", "Bye!"]
    },
    "thanks": {
        "patterns": ["thank you", "thanks", "I appreciate it"],
        "responses": ["You're welcome!", "No problem!", "Glad I could help!"]
    }
}

# Function to preprocess input sentence
def preprocess(sentence):
    tokens = word_tokenize(sentence.lower())
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in string.punctuation]
    return tokens

# Function to check for matches
def match_category(user_input):
    tokens = preprocess(user_input)
    for category, details in data.items():
        for pattern in details["patterns"]:
            pattern_tokens = preprocess(pattern)
            if set(pattern_tokens).intersection(set(tokens)):
                return category
    return None

# Function to generate a response
def generate_response(user_input):
    category = match_category(user_input)
    if category:
        return random.choice(data[category]["responses"])
    else:
        return "I am sorry, I don't understand that."

# Main chatbot function
def chatbot():
    print("Chatbot: Hello! Ask me anything. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['bye', 'exit']:
            print("Chatbot: Goodbye!")
            speak_response("Goodbye!")
            break
        
        response = generate_response(user_input)
        print("Chatbot:", response)
        speak_response(response)

# Run the chatbot
chatbot()