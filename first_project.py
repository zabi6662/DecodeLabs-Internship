responses = {
    "hello": "Hello! Nice to meet you.",
    "hi": "Hello! Nice to meet you.",
    "hey": "Hello! Nice to meet you.",
    "how are you": "I am fine. Thank you for asking!",
    "what is your name": "My name is AI Chatbot.",
    "who created you": "I was created using Python.",
    "help": "You can ask: hello, how are you, what is your name, who created you, bye"
}

print("=== Rule-Based AI Chatbot ===")
print("Type 'bye' or 'exit' to quit.\n")

while True:
    user = input("You: ").lower()

    if user == "bye" or user == "exit":
        print("Bot: Goodbye! Have a great day.")
        break

    print("Bot:", responses.get(user, "Sorry, I don't understand that."))


# print("=== Rule-Based AI Chatbot ===")
# print("Type 'bye' to exit.\n")

# while True:
#     user = input("You: ").lower()

#     if user == "hello" or user == "hi":
#         print("Bot: Hello! How can I help you?")

#     elif user == "how are you":
#         print("Bot: I am fine. Thank you for asking!")

#     elif user == "what is your name":
#         print("Bot: My name is AI Chatbot.")

#     elif user == "who created you":
#         print("Bot: I was created using Python.")

#     elif user == "help":
#         print("Bot: You can ask me simple questions.")

#     elif user == "bye" or user == "exit":
#         print("Bot: Goodbye! Have a nice day.")
#         break

#     else:
#         print("Bot: Sorry, I don't understand that.")


# Rule-Based AI Chatbot using get() method

