# Basic Rule-Based Chatbot

def chatbot():
    print("Chatbot: Hello! Welcome to my chatbot.")
    print("Type 'bye' to end the chat.")

    while True:
        user = input("You: ").lower().strip()

        if user == "hello":
            print("Chatbot: Hi!")

        elif user == "how are you":
            print("Chatbot: I'm fine, thanks!")

        elif user == "what is your name":
            print("Chatbot: I am a Python chatbot.")

        elif user == "thank you":
            print("Chatbot: You're welcome!")

        elif user == "bye":
            print("Chatbot: Goodbye!")
            break

        else:
            print("Chatbot: Sorry, I don't understand.")

chatbot()