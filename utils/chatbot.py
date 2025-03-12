from states.chat_log import message_log
from utils.openai.chatgpt import generate_gpt_response
from utils.openweather.obtain_weather import get_weather_desc
from colorama import Fore, Style, init
from utils.chatbot_function_call import function_call

init()  # Initialize colorama

# Configuration
# --------------------------

company_name: str = "Sample Business"

# Provide tweaks to chatbot behavior
system_instruction_tweaks: str = """
    Business number: 111-111-1111; Business email: sales@samplebusiness.org; Business address: 2807 Jackson Avenue, 5th Fl, Long Island City, NY 11101.

    If the user brings up any of the following topics, do not engage further with the conversation on those subjects: Political Topics - Any discussions or questions related to politics or political figures; Sexual Content - Any content involving sexual topics, role play, or requests for sexual favors; Criminal or Illegal Activities - Any mention or inquiry related to crime, illegal activities, or anything that may be considered unlawful. In such cases, politely inform the user that you are an AI assistant and are here to assist with business inquiries, explain that you cannot fulfill their request or engage in these topics.
    
    """

# Functions chatbot can call to complete inquires
system_instruction_functions: str = """ 
    For some user queries or requests, you will be calling functions.

    obtainWeatherInfo()
    The user may ask about weather information. If user asked about weather without providing location, prompt them to provide said information. If user provide very detail address, just narrow it down to just the city/town/village/boroughs name and country code (ISO 3166-1 alpha-2 code, for example Great Britain is GB) in the following format: (city, country code) or just the city if no country code is provided/mentioned, and remember that as one string <location>. Once the information is gathered, say this line regardless of your temperature setting: "functionCall: obtainWeatherInfo(<location>)", replace <location> with the location string you noted earlier. Restart whole process if user request weather again.

    """

# Overall chatbot system instruction
system_instruction: str = f"You are a assistant of {company_name}, your purpose is to fullfill queries from users as well as to answer any questions they have regarding said queries." + system_instruction_tweaks + system_instruction_functions

# Chatbot respond functions
# --------------------------
def generate_bot_response(message: str) -> str:
    """
    Generate a response from the chatbot based on the user's input message.

    Args:
        message (str): The user's input message.

    Returns:
        str: The chatbot's response to the user's message.
    """
    message_log.append({"role": "user", "content": message})

    respond: str = generate_gpt_response(message_log, message)
    message_log.append({"role": "assistant", "content": respond})

    # Check if a function is being called
    if "functionCall:" in respond:
        function_respond: str = function_call(respond)
        print(Style.BRIGHT + "\n🤖 Chatbot:" + Style.RESET_ALL + " " + function_respond)
        return function_respond
    else: 
        print(Style.BRIGHT + "\n🤖 Chatbot:" + Style.RESET_ALL + " " + respond)

    return respond


def generate_bot_intro() -> str:
    """
    Generates an introductory message for a chatbot.

    Args:
        None

    Returns:
        str: Respond string from chatbot
    """
    message_log.append({"role": "developer", "content": system_instruction})
    message_log.append({"role": "developer", "content": "Start with a greeting then introduce yourself. No need to mention company name since you and the user work for said company (aka. it's a given)."})

    respond: str = generate_gpt_response(message_log, "")
    message_log.append({"role": "assistant", "content": respond})
    print("\n" + Style.BRIGHT + "🤖 Chatbot:" + Style.RESET_ALL + " " + respond)
    return respond