import json
from collections import Counter
from typing import List

def list_to_count(arr: List) -> str:
    """
    Counts the occurrences of each element in the list and returns a JSON string.

    Args:
        arr (List): The input list containing hashable elements.

    Returns:
        str: A JSON-formatted string representing the counts.
    """
    counts = Counter(arr)
    return json.dumps(counts )

def string_to_dict(s: str) -> dict:
    """
    Converts a JSON string to a dictionary.

    Args:
        s (str): The JSON-formatted string.

    Returns:
        dict: The resulting dictionary.

    Raises:
        ValueError: If the input string is not valid JSON.
    """
    try:
        return json.loads(s)
    except json.JSONDecodeError as e:
        raise ValueError("Invalid JSON string") from e


