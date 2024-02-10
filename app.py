import sys
from configparser import ConfigParser
from bot import Chatbot

def main():
    config = ConfigParser()
    config.read('credemtials.ini')
    api_key = config['gemini_ai']['API_KEY']
    chatbot = Chatbot(api_key=api_key)
    chatbot.start_conversation()
    print("Welcome to Guru chatbot CLI. Type 'quit' to exit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            sys.exit("Exiting ChatBot CLI...")

        try:
            response = chatbot.send_prompt(user_input)
            print(f"{chatbot.CHATBOT_NAME}: {response}")
        except Exception as e:
            import traceback
            traceback.print_exc()
            print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()
