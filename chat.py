import re

def chatbot_response(user_input):
    responses = {
        r'hi': 'Hi man! How can I assist you today?',
        r'hello': 'Hello! How can I help you today?',
        r'iam fine': 'sounds good,How can i assist you today?',
        r'bye|goodbye|see you': 'Goodbye! Have a great day!',
        r'how are you|how are you doing': 'I am just a bot, but I am functioning as expected. How about you?',
        r'what is your name|who are you': 'I am a simple chatbot created to assist you with basic questions.',
        r'help|support': 'Sure, I am here to help. What do you need assistance with?',
        r'(.*)': 'I am not sure how to respond to that. Could you please elaborate?'
    }

    for pattern, response in responses.items():
        if re.search(pattern, user_input, re.IGNORECASE):
            return response
    
    return "I am not sure how to respond to that."

def main():
    print("Chatbot: Hello! I am your chatbot. for exit the chat,Type 'bye'.")
    
    while True:
        user_input = input("You: ")
        if re.search(r'bye|goodbye|see you', user_input, re.IGNORECASE):
            print("Chatbot: Goodbye! Have a great day!")
            break
        else:
            response = chatbot_response(user_input)
            print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()
