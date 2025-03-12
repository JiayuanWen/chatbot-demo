from utils.openweather.obtain_weather import get_weather_desc
from utils.openai.chatgpt import generate_gpt_response
from states.chat_log import message_log
import re

def function_call(function_call_str: str) -> str:
    """
    Parse a function call string and execute the corresponding function.

    Args:
        function_call_str (str): A string representing a function call, in the format "functionCall:function_name(params|optional_params)".

    Returns:
        str: The result of the executed function.
    """
    function_name: str = ""
    function_params: str = ""

    function_call_pattern = re.compile(r"functionCall:\s([a-zA-Z_]\w*)\(([^|)]+)(\|[^|)]+)*\)")
    match = function_call_pattern.search(function_call_str)

    # Extract function name and parameters from pattern
    if match and match.group(1):
        function_name = match.group(1) 
        #print("Function called:", function_name)

        function_params = match.group(2)
        #print("Function params:", function_params)

    # Functions
    # ---------------------------
    if function_name == "obtainWeatherInfo":
        weather = get_weather_desc(function_params)

        message_log.append({"role": "developer", "content": f"Respond to user's request for weather base on the following information: {weather}"})
        respond: str = generate_gpt_response(message_log, "")

        return respond
        