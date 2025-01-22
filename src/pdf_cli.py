# pdf_cli.py
import click
from src.pdf_extractor import extract_text_from_pdf


@click.command()
@click.argument("pdf_path")
def main(pdf_path):
    """Extract text from PDF and print it."""
    extracted = extract_text_from_pdf(pdf_path)
    print(extracted)


if __name__ == "__main__":
    main()
