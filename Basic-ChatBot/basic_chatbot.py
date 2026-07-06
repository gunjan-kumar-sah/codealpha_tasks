def chatbot():
    print("=" * 50)
    print("🤖 Welcome to HR Assistant Chatbot")
    print("Type 'bye' to exit.")
    print("=" * 50)

    while True:
        user = input("\nYou: ").lower()

        if user == "hello":
            print("Bot: Hello! Welcome. How can I assist you today?")

        elif user == "hi":
            print("Bot: Hi! It's great to meet you. 😊")

        elif user == "how are you":
            print("Bot: I'm doing great! Thank you for asking.")

        elif user == "what is your name":
            print("Bot: My name is HRBot, your virtual recruitment assistant.")

        elif user == "who created you":
            print("Bot: I was developed using Python as a beginner chatbot project.")

        elif user == "what can you do":
            print("Bot: I can answer basic career, resume, interview, and recruitment-related questions.")

        elif user == "help":
            print("Bot: You can ask about resumes, interviews, internships, skills, or career guidance.")

        elif user == "tell me about yourself":
            print("Bot: I'm an AI-based HR Assistant chatbot created to help candidates prepare for interviews and careers.")

        elif user == "resume":
            print("Bot: A good resume should include your education, skills, projects, certifications, and achievements.")

        elif user == "interview":
            print("Bot: Prepare your introduction, revise core concepts, practice coding, and be confident.")

        elif user == "internship":
            print("Bot: Build projects, strengthen your GitHub profile, and keep applying consistently.")

        elif user == "skills":
            print("Bot: Learn Python, SQL, Git, GitHub, Data Structures, OOP, and Communication Skills.")

        elif user == "github":
            print("Bot: Keep your GitHub updated with clean projects and proper README files.")

        elif user == "linkedin":
            print("Bot: Maintain a professional LinkedIn profile and share your learning journey regularly.")

        elif user == "projects":
            print("Bot: Projects demonstrate your practical skills. Build real-world applications to impress recruiters.")

        elif user == "career":
            print("Bot: Focus on continuous learning, consistency, and practical experience.")

        elif user == "python":
            print("Bot: Python is an excellent programming language for automation, web development, data science, and AI.")

        elif user == "ai":
            print("Bot: Artificial Intelligence enables machines to perform tasks that usually require human intelligence.")

        elif user == "thank you":
            print("Bot: You're most welcome! Best of luck with your career. 😊")

        elif user == "bye":
            print("Bot: Goodbye! Wishing you success in your career. 👋")
            break

        else:
            print("Bot: Sorry, I couldn't understand that. Please ask about resumes, interviews, internships, skills, Python, AI, or career guidance.")

# Run the chatbot
chatbot()