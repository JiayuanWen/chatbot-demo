from utils.chatbot import generate_bot_intro, generate_bot_response
from states.chat_log import message_log


if __name__ == "__main__":

    generate_bot_intro()

    while True:
            # User enter message
            user_input = input("\nYou: ")

            # User may quit at any time
            if user_input.lower() in ["quit", "exit", "bye"]:
                break

            # Chatbot receive user message and generate respond
            respond: str = generate_bot_response(user_input)