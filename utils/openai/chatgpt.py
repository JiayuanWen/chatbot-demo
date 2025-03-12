import os
from clients.openai_client import client as client_openAI

def generate_gpt_response(message_log: list[dict[str, str]], prompt: str) -> str:
    """
    Generate a response using the GPT-3.5 model based on the provided message log and prompt.

    Args:
        message_log (list[dict[str, str]]): A list of dictionaries representing the conversation history.
        prompt (str): The prompt to use for generating the response.

    Returns:
        str: The generated response from the GPT-3.5 model.
    """
    response = client_openAI.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=message_log,
        max_tokens=1000,
        temperature=0.6,
    )
    
    return response.choices[0].message.content.strip()