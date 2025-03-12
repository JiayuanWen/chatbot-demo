from utils.chatbot.chatbot import generate_bot_intro, generate_bot_response
from states.chat_log import message_log
from utils.user_input.user_input import u_input

if __name__ == "__main__":
    print("\n(To end the chat, simply say\"quit\", \"exit\", or \"bye\".)")

    generate_bot_intro()

    while True:
            # User enter message
            user_input = u_input("\nYou: ")

            # User may quit at any time
            if user_input.lower() in ["quit", "exit", "bye"]:
                break

            # Chatbot receive user message and generate respond
            respond: str = generate_bot_response(user_input)