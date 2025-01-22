# src/text_tokenizer.py
import re


def _space_around_punct(text: str) -> str:
    """
    Insert spaces around punctuation marks so that e.g.
    'legitimate: their' -> 'legitimate : their'
    'georges?' -> 'georges ?'
    """
    return re.sub(r'([:;\.,\?\!\(\)"])', r" \1 ", text)


def tokenize(text: str) -> list[str]:
    """
    1) Lowercase text.
    2) Insert spaces around punctuation (see above).
    3) Split on whitespace.
    4) Strip leading/trailing quotes (' " « » “ ”) and underscores,
       but preserve them if they appear in the middle
       (e.g. "don't", "skin-care", "some_var").
    5) Return list of cleaned tokens.
    """
    # 1) lowercase
    text = text.lower()

    # 2) Insert spaces around punctuation
    text = _space_around_punct(text)

    # 3) Split
    raw_tokens = text.split()

    cleaned_tokens = []
    for token in raw_tokens:
        # 4) Remove leading/trailing quotes & underscores
        token = re.sub(r"^['\"«»\u201c\u201d_]+|['\"«»\u201c\u201d_]+$", "", token)
        if token:  # keep if not empty
            cleaned_tokens.append(token)

    return cleaned_tokens
