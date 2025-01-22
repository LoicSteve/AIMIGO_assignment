# src/main.py
import cProfile
from .pdf_extractor import extract_text_from_pdf
from .occurence_counter import count_occurrences_in_text

# 1) Extract the text from the PDF
PDF_PATH = "etl_sample.pdf"
SAMPLE_TEXT_FOR_BENCH = extract_text_from_pdf(PDF_PATH)


def doit() -> int:
    """
    Run count_occurrences_in_text on a few examples
    to produce some integer result for performance profiling.
    """
    i = 0
    for x in range(400):
        i += count_occurrences_in_text("word", SAMPLE_TEXT_FOR_BENCH)
        i += count_occurrences_in_text("sugar", SAMPLE_TEXT_FOR_BENCH)
        i += count_occurrences_in_text("help", SAMPLE_TEXT_FOR_BENCH)
        i += count_occurrences_in_text("heavily", SAMPLE_TEXT_FOR_BENCH)
        i += count_occurrences_in_text("witfull", SAMPLE_TEXT_FOR_BENCH)
        i += count_occurrences_in_text("dog", SAMPLE_TEXT_FOR_BENCH)
        i += count_occurrences_in_text("almost", SAMPLE_TEXT_FOR_BENCH)
        i += count_occurrences_in_text("insulin", SAMPLE_TEXT_FOR_BENCH)
        i += count_occurrences_in_text("attaching", SAMPLE_TEXT_FOR_BENCH)
        i += count_occurrences_in_text("asma", SAMPLE_TEXT_FOR_BENCH)
        i += count_occurrences_in_text("neither", SAMPLE_TEXT_FOR_BENCH)
        i += count_occurrences_in_text("won't", SAMPLE_TEXT_FOR_BENCH)
        i += count_occurrences_in_text("green", SAMPLE_TEXT_FOR_BENCH)
        i += count_occurrences_in_text("parabole", SAMPLE_TEXT_FOR_BENCH)
    return i


def test_profile():
    """
    A function to profile performance of `doit`.
    """
    with cProfile.Profile() as pr:
        assert doit() == 3600
        pr.print_stats()


if __name__ == "__main__":

    print("Count from doit() ->", doit())
