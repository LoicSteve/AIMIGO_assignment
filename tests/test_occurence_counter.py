# tests/test_occurrence_counter.py
from src.occurence_counter import count_occurrences_in_text


def test_count_occurrences_in_text():
    text = """Georges is my name and I like python. Oh ! your name is georges? And you like Python!
Yes is is true, I like PYTHON
and my name is GEORGES"""
    # test with a little text.
    assert 3 == count_occurrences_in_text("Georges", text)
    assert 3 == count_occurrences_in_text("GEORGES", text)
    assert 3 == count_occurrences_in_text("georges", text)
    assert 0 == count_occurrences_in_text("george", text)
    assert 3 == count_occurrences_in_text("python", text)
    assert 3 == count_occurrences_in_text("PYTHON", text)
    assert 2 == count_occurrences_in_text("I", text)
    assert 0 == count_occurrences_in_text("n", text)
    assert 1 == count_occurrences_in_text("true", text)
    # regard ' as text:
    assert 0 == count_occurrences_in_text("maley", "John O'maley is my friend")

    # Test it but with a BIG length file.
    text = (
        """The quick brown fox jump over the lazy dog.The quick brown fox jump over the lazy dog."""
        * 500
    )
    text += """The quick brown fox jump over the lazy dog.The quick brown Georges jump over the lazy dog."""
    text += """esrf sqfdg sfdglkj sdflgh sdflgjdsqrgl """ * 4000
    text += """The quick brown fox jump over the lazy dog.The quick brown fox jump over the lazy python."""
    text += (
        """The quick brown fox jump over the lazy dog.The quick brown fox jump over the lazy dog."""
        * 500
    )
    text += """The quick brown fox jump over the lazy dog.The quick brown Georges jump over the lazy dog."""
    text += """esrf sqfdg sfdglkj sdflgh sdflgjdsqrgl """ * 4000
    text += """The quick brown fox jump over the lazy dog.The quick brown fox jump over the lazy python."""
    text += (
        """The quick brown fox jump over the lazy dog.The quick brown fox jump over the lazy dog."""
        * 500
    )
    text += """The quick brown fox jump over the lazy dog.The quick brown Georges jump over the lazy dog."""
    text += """esrf sqfdg sfdglkj sdflgh sdflgjdsqrgl """ * 4000
    text += """The quick brown fox jump over the lazy dog.The quick brown fox jump over the lazy python."""
    text += """The quick brown fox jump over the true lazy dog.The quick brown fox jump over the lazy dog."""
    text += (
        """The quick brown fox jump over the lazy dog.The quick brown fox jump over the lazy dog."""
        * 500
    )
    text += """ I vsfgsdfg sfdg sdfg sdgh sgh I sfdgsdf"""
    text += (
        """The quick brown fox jump over the lazy dog.The quick brown fox jump over the lazy dog."""
        * 500
    )

    assert 3 == count_occurrences_in_text("Georges", text)
    assert 3 == count_occurrences_in_text("GEORGES", text)
    assert 3 == count_occurrences_in_text("georges", text)
    assert 0 == count_occurrences_in_text("george", text)
    assert 3 == count_occurrences_in_text("python", text)
    assert 3 == count_occurrences_in_text("PYTHON", text)
    assert 2 == count_occurrences_in_text("I", text)
    assert 0 == count_occurrences_in_text("n", text)
    assert 1 == count_occurrences_in_text("true", text)
    assert 1 == count_occurrences_in_text(
        "'reflexion mirror'",
        "I am a senior citizen and I live in the Fun-Plex 'Reflexion Mirror' in Sopchoppy, Florida",
    )
    assert 1 == count_occurrences_in_text(
        "reflexion mirror",
        "I am a senior citizen and I live in the Fun-Plex (Reflexion Mirror) in Sopchoppy, Florida",
    )
    assert 1 == count_occurrences_in_text(
        "reflexion mirror", 'Reflexion Mirror" in Sopchoppy, Florida'
    )
    assert 1 == count_occurrences_in_text(
        "reflexion mirror",
        "I am a senior citizen and I live in the Fun-Plex «Reflexion Mirror» in Sopchoppy, Florida",
    )
    assert 1 == count_occurrences_in_text(
        "reflexion mirror",
        "I am a senior citizen and I live in the Fun-Plex \u201cReflexion Mirror\u201d in Sopchoppy, Florida",
    )
    assert 1 == count_occurrences_in_text(
        "legitimate",
        "who is approved by OILS is completely legitimate: their employees are of legal working age",
    )
    assert 0 == count_occurrences_in_text(
        "legitimate their",
        "who is approved by OILS is completely legitimate: their employees are of legal working age",
    )
    assert 1 == count_occurrences_in_text(
        "get back to me",
        "I hope you will consider this proposal, and get back to me as soon as possible",
    )
    assert 1 == count_occurrences_in_text(
        "skin-care",
        "enable Delavigne and its subsidiaries to create a skin-care monopoly",
    )
    assert 1 == count_occurrences_in_text(
        "skin-care monopoly",
        "enable Delavigne and its subsidiaries to create a skin-care monopoly",
    )
    assert 0 == count_occurrences_in_text(
        "skin-care monopoly in the US",
        "enable Delavigne and its subsidiaries to create a skin-care monopoly",
    )
    assert 1 == count_occurrences_in_text(
        "get back to me", "When you know:get back to me"
    )
    assert 1 == count_occurrences_in_text(
        "don't be left",
        """emergency alarm warning.
Don't be left unprotected. Order your SSSS3000 today!""",
    )
    assert 1 == count_occurrences_in_text(
        "don",
        """emergency alarm warning.
Don't be left unprotected. Order your don SSSS3000 today!""",
    )
    assert 1 == count_occurrences_in_text(
        "take that as a 'yes'", "Do I have to take that as a 'yes'?"
    )
    assert 1 == count_occurrences_in_text(
        "don't take that as a 'yes'", "I don't take that as a 'yes'?"
    )
    assert 1 == count_occurrences_in_text(
        "take that as a 'yes'", "I don't take that as a 'yes'?"
    )
    assert 1 == count_occurrences_in_text("don't", "I don't take that as a 'yes'?")
    assert 1 == count_occurrences_in_text(
        "attaching my c.v. to this e-mail", "I am attaching my c.v. to this e-mail."
    )
    assert 1 == count_occurrences_in_text(
        "Linguist", "'''Linguist Specialist Found Dead on Laboratory Floor'''"
    )
    assert 1 == count_occurrences_in_text(
        "Linguist Specialist",
        "'''Linguist Specialist Found Dead on Laboratory Floor'''",
    )
    assert 1 == count_occurrences_in_text(
        "Laboratory Floor", "'''Linguist Specialist Found Dead on Laboratory Floor'''"
    )
    assert 1 == count_occurrences_in_text(
        "Floor", "'''Linguist Specialist Found Dead on Laboratory Floor'''"
    )
    assert 1 == count_occurrences_in_text(
        "Floor", "''Linguist Specialist Found Dead on Laboratory Floor''"
    )
    assert 1 == count_occurrences_in_text(
        "Floor", "__Linguist Specialist Found Dead on Laboratory Floor__"
    )
    assert 1 == count_occurrences_in_text(
        "Floor", "'''''Linguist Specialist Found Dead on Laboratory Floor'''''"
    )
    assert 1 == count_occurrences_in_text(
        "Linguist", "'''Linguist Specialist Found Dead on Laboratory Floor'''"
    )
    assert 1 == count_occurrences_in_text(
        "Linguist", "''Linguist Specialist Found Dead on Laboratory Floor''"
    )
    assert 1 == count_occurrences_in_text(
        "Linguist", "__Linguist Specialist Found Dead on Laboratory Floor__"
    )
    assert 1 == count_occurrences_in_text(
        "Linguist", "'''''Linguist Specialist Found Dead on Laboratory Floor'''''"
    )
