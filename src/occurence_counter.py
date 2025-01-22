# src/occurrence_counter.py
from .text_tokenizer import tokenize


def count_occurrences_in_text(word: str, text: str) -> int:
    """
    Return the number of occurrences of `word` (case-insensitive)
    in `text`, matching whole tokens or consecutive tokens for multi-word
    phrases.
    """
    search_tokens = tokenize(word)
    text_tokens = tokenize(text)

    if not search_tokens:
        return 0

    count = 0
    wlen = len(search_tokens)
    tlen = len(text_tokens)

    for i in range(tlen - wlen + 1):
        if text_tokens[i : i + wlen] == search_tokens:
            count += 1

    return count
