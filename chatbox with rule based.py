import re
def respond_to_input(user_input):
    """Generate response based on user input."""
    
    # Convert input to lowercase for uniform matching
    user_input = user_input.lower()

    # Define responses for certain patterns
    if re.search(r'\bhello\b|\bhi\b|\bhey\b', user_input):
        return "Hello! How can I assist you today?"
    
    elif re.search(r'\bhow are you\b|\bhows it going\b|\bhow are you doing\b', user_input):
        return "I'm just a chatbot, but I'm doing great! How about you?"
    
    elif re.search(r'\bbye\b|\bexit\b|\bquit\b', user_input):
        return "Goodbye! Have a great day!"
    
    elif re.search(r'\bname\b|\byour name\b', user_input):
        return "I am a simple chatbot. I don't have a personal name, but you can call me Chatbot!"
    
    elif re.search(r'\bhelp\b|\bassist\b|\bcan you\b', user_input):
        return "I can help with simple questions or have a chat. Try asking about my name or how I work!"
    
    elif re.search(r'\bwhat\b.*\btime\b', user_input):
        return "Sorry, I can't tell the time right now, but I hope you're having a good one!"
    
    elif re.search(r'\bthanks\b|\bthank you\b', user_input):
        return "You're welcome! I'm happy to help."
    
    else:
        return "Sorry, I didn't quite understand that. Could you ask something else?"

def chatbot():
    """Main function to handle the chatbot conversation."""
    print("Hello! I'm a simple chatbot. Type 'exit' or 'quit' to end the conversation.")
    
    while True:
        # Get user input
        user_input = input("You: ")
        
        # Exit condition
        if user_input.lower() in ['exit', 'quit']:
            print("Chatbot: Goodbye! Have a great day!")
            break
        
        # Get the chatbot's response
        response = respond_to_input(user_input)
        
        # Display the chatbot's response
        print(f"Chatbot: {response}")

# Run the chatbot
if __name__ == "__main__":
    chatbot()

