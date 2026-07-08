def chatbot():
    responses = {
        "hello": "Hello!",
        "hi": "Hi!",
        "how are you": "I'm fine. Thanks!",
        "what is your name": "I'm ChatBot.",
        "python": "Python is an easy programming language.",
        "resume": "A resume shows your skills and experience.",
        "interview": "Practice coding and be confident.",
        "internship": "Keep learning and apply regularly.",
        "help": "Ask me about Python, resume, interview, or internship.",
        "thank you": "You're welcome! 😊"
    }

    print("=" * 40)
    print("🤖 Simple ChatBot")
    print("Type 'bye' to exit.")
    print("=" * 40)

    while True:
        user = input("\nYou: ").lower()

        if user == "bye":
            print("Bot: Goodbye! 👋")
            break

        elif user in responses:
            print("Bot:", responses[user])

        else:
            print("Bot: Sorry, I don't understand.")


chatbot()