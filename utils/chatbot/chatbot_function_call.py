from utils.openai.chatgpt import generate_gpt_response
from states.chat_log import message_log
import re

from utils.send_email.send_email import send_email
from utils.openweather.obtain_weather import get_weather_desc
from utils.report_gen.report_gen import generate_weekly_financial_report

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

    #function_call_pattern = re.compile(r"functionCall:\s([a-zA-Z_]\w*)\(([^|)]+)(\|[^|)]+)*\)")
    function_call_pattern = re.compile(r"functionCall:\s([a-zA-Z_]\w*)\(([^)]*)\)")
    match = function_call_pattern.search(function_call_str)

    # Extract function name and parameters from pattern
    if match and match.group(1):
        function_name = match.group(1) 
        print("Function called:", function_name)

        function_params = match.group(2)
        print("Function params:", function_params)
    else:
        return "Function call failed. Please contact it@happycashier.com"

    # Functions
    # ---------------------------

    # obtainWeatherInfo()
    if function_name == "obtainWeatherInfo":
        weather = get_weather_desc(function_params)

        message_log.append({"role": "developer", "content": f"Respond to user's request for weather base on the following information: {weather}"})
        respond: str = generate_gpt_response(message_log, "")

    # createWeeklyFinancialReport()
    if function_name == "createWeeklyFinancialReport": 
        respond: str = generate_weekly_financial_report(function_params)

    # sendEmail()
    if function_name == "sendEmail": 
        recipient, recipient_email, cc_addresses, subject, content = function_params.split("|")
        respond: str = send_email(recipient, recipient_email, cc_addresses, subject, content)
        

    return respond
        
        
