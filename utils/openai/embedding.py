import math
from typing import Union
from clients.openai_client import client as client_openAI

def text_embedding(text_input: Union[list[str], str]) -> None:
    """
    Convert strings into vectors so AI models can process.

    Args:
        text_input (list[str] | str): An list of strings or just a string.

    Returns:
        None
    """
    response = client_openAI.embeddings.create(
        model="text-embedding-ada-002",
        input=text_input,
        encoding_format="float"
    )

    print(response.data[1])

def cos_similarity(vec1: list[float], vec2: list[float]) -> float:
    """
    Calculate the cosine similarity between two vectors.

    Args:
        vec1 (list[float]): The first vector.
        vec2 (list[float]): The second vector.

    Returns:
        float: The cosine similarity between the two vectors.
    """
    dot_product = sum(a * b for a, b in zip(vec1, vec2))
    magnitude_a = math.sqrt(sum(a ** 2 for a in vec1))
    magnitude_b = math.sqrt(sum(b ** 2 for b in vec2))
    similarity = dot_product / (magnitude_a * magnitude_b)

    return similarity

def text_ranking(text_query: str, cases: list[str]) -> list[dict[str, str]]:
    """
    Rank a list of cases based on their similarity to a given query.

    Args:
        text_query (str): The text query to rank cases against.
        cases (list[str]): A list of cases to rank.

    Returns:
        list[dict[str, str]]: A desend sorted list of dictionaries, where each dictionary contains the original case and its corresponding rank (similarity score).
    """
    rankings: list = []

    embedded_text_query = text_embedding()

    for i in enumerate(cases):
        similarity: float = cos_similarity(embedded_text_query[0], cases[i].vector)
        rankings.append({**item, 'rank': similarity})

    rankings.sort(key=lambda x: x.rank, reverse=True)

    return rankings