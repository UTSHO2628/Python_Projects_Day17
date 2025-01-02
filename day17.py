import datetime
import random
import re

# Chatbot with Enhanced Features
def enhanced_chatbot():
    print("Chatbot: Hi there! I'm your mini chatbot. Ask me anything!")
    print("Type 'exit' to end the conversation.\n")

    responses = {
        "hello": ["Hello! How can I assist you?", "Hi there! What's on your mind?", "Hey! Need any help?"],
        "how are you": ["I'm just a bot, but I'm doing great! How about you?", "Feeling fantastic! How can I help?"],
        "what is your name": ["I am your smart chatbot, created by Utsho Kumar Dey!", "You can call me ChatBotUKD!,created by Utsho Kumar Dey! "],
        "time": ["The current time is "],
        "joke": ["Why don't scientists trust atoms? Because they make up everything!",
                 "Why did the math book look sad? It had too many problems.",
                 "Why did the scarecrow win an award? Because he was outstanding in his field!"],
        "bye": ["Goodbye! Have a nice day!", "Bye! Take care!", "See you later!"],
        "default": ["I'm sorry, I didn't understand that.", "Could you rephrase your question?", "Hmm, I'm not sure about that."]
    }

    def calculate(expression):
        try:
            result = eval(expression)
            return f"The answer is {result}."
        except:
            return "I couldn't understand the calculation. Please try again."

    while True:
        user_input = input("You: ").lower()
        
        if user_input == "exit":
            print("Chatbot: Chat session ended. Goodbye!")
            break

        elif "time" in user_input:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            print(f"Chatbot: {responses['time'][0]}{current_time}.")
        
        elif "joke" in user_input:
            joke = random.choice(responses["joke"])
            print(f"Chatbot: {joke}")

        elif re.search(r'\d+[\+\-\*/]\d+', user_input):
            print(f"Chatbot: {calculate(user_input)}")
        
        else:
            matched_responses = [responses[key] for key in responses if key in user_input]
            if matched_responses:
                response = random.choice(matched_responses[0])
            else:
                response = random.choice(responses["default"])
            print(f"Chatbot: {response}")

enhanced_chatbot()
