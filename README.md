Chatbot with Text-to-Speech using NLTK and pyttsx3

Objective:
To build a simple chatbot capable of responding to user input and using text-to-speech to vocalize the responses.

Implementation:

Libraries Used:

nltk: For text preprocessing (tokenization and lemmatization).
pyttsx3: For text-to-speech functionality.
Steps:

Dataset of Greetings and Responses:
A small dataset of user input patterns and responses is used.

Preprocessing Input:
The user's input is tokenized and lemmatized to standardize the text.

Response Matching:
The chatbot matches user input against predefined patterns and returns a random response from the relevant category.

Text-to-Speech:
The chatbot's responses are vocalized using pyttsx3 with the espeak driver.

Design Choices:

Lemmatization helps in standardizing the input, making it easier to match user queries.
Adding a text-to-speech engine gives the chatbot an interactive and dynamic feel.
Challenges Faced:

Managing TTS with dynamic user input required handling edge cases where the input doesn’t match any patterns.
