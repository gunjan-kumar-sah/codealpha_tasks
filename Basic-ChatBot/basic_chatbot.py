def chatbot():
    print("=" * 40)
    print("🤖 Welcome to Basic Chatbot")
    print("Type 'bye' to exit.")
    print("=" * 40)

    while True:
        user = input("\nYou: ").lower()

        if user == "hello":
            print("Bot: Hi! How can I help you?")
        elif user == "how are you":
            print("Bot: I'm fine, thank you! 😊")
        elif user == "what is your name":
            print("Bot: My name is CodeBot.")
        elif user == "who created you":
            print("Bot: I was created using Python.")
        elif user == "help":
            print("Bot: You can say hello, how are you, or ask my name.")
        elif user == "bye":
            print("Bot: Goodbye! Have a great day. 👋")
            break
        else:
            print("Bot: Sorry, I don't understand that.")

# Run the chatbot
chatbot()