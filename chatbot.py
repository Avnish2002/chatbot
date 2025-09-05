def chatbot():
    print("🤖 Chatbot: Hello! I'm your simple chatbot. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ").lower()  # Convert input to lowercase for easy comparison
        
        if user_input in ["hello", "hi", "hey"]:
            print("🤖 Chatbot: Hi there!")
        
        elif user_input in ["how are you", "how are you doing"]:
            print("🤖 Chatbot: I'm fine, thanks! How about you?")
        
        elif user_input in ["bye", "exit", "quit"]:
            print("🤖 Chatbot: Goodbye! Have a great day 👋")
            break
        
        elif user_input in ["what is your name", "who are you"]:
            print("🤖 Chatbot: I'm a simple chatbot created with Python!")
        
        else:
            print("🤖 Chatbot: Sorry, I don't understand that.")

# Run the chatbot
if __name__ == "__main__":
    chatbot()
