# ETL/Pipeline engineer missions
[![CI](https://github.com/LoicSteve/AIMIGO_assignment/actions/workflows/main.yml/badge.svg)](https://github.com/LoicSteve/AIMIGO_assignment/actions/workflows/main.yml)

Notes
If all you need is to verify the solution, just run:
   ```bash
   python -m pytest _etl_a9number_v3.py
   ```
to confirm mission #1 and #2 are satisfied.
If you’d like a more production-ready approach, explore our enhanced modular code and Docker setup below.

A Python-based project that demonstrates:
- Extracting text from a PDF (excluding figure captions),
- Tokenizing and counting occurrences of specific words or phrases,
- Unit testing (Pytest) for correctness,
- Code formatting (Black, isort),
- Linting (Pylint or flake8),
- Packaging everything in Docker for an easy, reproducible environment.

---

## Table of Contents
1. [Overview](#overview)  
2. [Features](#features)  
3. [Project Structure](#project-structure)  
4. [Requirements](#requirements)  
5. [Installation](#installation)  
6. [Running Tests](#running-tests)  
7. [Linting & Formatting](#linting--formatting)  
8. [Profiling](#profiling)  
9. [Docker Usage](#docker-usage)  
10. [CI Pipeline](#ci-pipeline)  

---

## Overview

This project extracts text from a PDF file (omitting figure captions), tokenizes the text, and counts how many times a word (or multi-word phrase) appears, respecting punctuation nuances like apostrophes and dashes. It also has a performance profiling script and uses best practices (linting, formatting, testing) for maintainable code.
Offering a clean pipeline (via **Makefile**, **Docker**, and **CI**) for an efficient developer experience.

---

## Features

- **PDF Extraction**: Reads and strips out figure captions using a regular expression.  
- **Tokenization**: Splits text on whitespace, handles punctuation carefully, preserves internal apostrophes/dashes.  
- **Occurrence Counting**: Matches consecutive tokens (case-insensitive).  
- **Modular**: Each piece (PDF extraction, tokenization, counting logic, etc.) is in its own module.  
- **Continuous Integration Friendly**: With a `Makefile`, you can easily install dependencies, format code, lint, and test in one step.  
- **Docker**: Containerize the project for consistent development and testing.
- **Integrated CI Pipeline**: GitHub Actions workflow to run tests and checks on every push.

---

## Project Structure

A suggested structure might look like:

```
.
├── _etl_a9number_v3.py
├── Dockerfile
├── Makefile
├── README.md
├── requirements.txt
├── src/
│   ├── pdf_extractor.py
│   ├── text_tokenizer.py
│   ├── occurrence_counter.py
│   ├── main.py
├──  tests/
│   ├── test_occurrence_counter.py
│    ├── __init__.py
└── .github/
   └── workflows/
       └── main.yml   (GitHub Actions CI workflow)

```



---

## Requirements

- **Python** 3.10+ (3.11 recommended; 3.13 may work but some linting tools can be buggy)  
- **pip** (to install dependencies)  
- **Make** (optional, for using the provided Makefile)  
- **Docker** (optional, for containerized builds/tests)

---

## Installation

1. **Clone** the repository or download the ZIP:
   ```bash
   git clone https://github.com/LoicSteve/AIMIGO_assignment.git
   cd AIMIGO_assignment
   ```
2. **Create** and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # on macOS/Linux
   .venv\Scripts\activate     # on Windows
   ```
3. **Install** Python dependencies:
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```
4. **Verify** installation by running:
   ```bash
   make test
   ```
   (or `pytest` directly if you prefer).

---

## Running Tests

I use **pytest** for all unit tests. To run the tests:

```bash
make test
```

Or directly:

```bash
pytest
```

If all tests pass, you should see something like:

```
========================== test session starts ==========================
collected X items

tests/test_occurrence_counter.py . . .
... all tests pass ...
==========================  X passed in 0.XXs ===========================
```

---

## Linting & Formatting

I use:
- **pylint** for linting  
- **black** for code formatting  

To lint & format your code:

```bash
make format   # runs black + isort on src/ and tests/
make lint     # runs pylint (or flake8) on src/ and tests/
```

Or run everything (install, format, lint, test) in one step:

```bash
make all
```

---

## Profiling

We have a profiling function `test_profile()` that uses **cProfile** to measure performance of the code:

```bash
python -c "from src.main import test_profile; test_profile()"
```

This will print out timing statistics so you can see if your code is performant.

---

## Docker Usage

You can build and run the project inside a Docker container to ensure a reproducible environment.

1. **Build the Docker image**:
   ```bash
   docker build -t my-python-app .
   ```
2. **Run tests** (by default, the container runs `pytest`):
   ```bash
   docker run --rm my-python-app
   ```
3. **Run lint or other commands** by overriding the default command:
   ```bash
   docker run --rm my-python-app make lint
   docker run --rm my-python-app make format
   ```

This ensures your code runs the same way on any machine with Docker installed.


## CI Pipeline

This repository leverages **GitHub Actions** to **automatically**:
1. Install dependencies,  
2. Run lint checks,  
3. Execute the test suite,  
4. (Optionally) build and push Docker images or gather coverage artifacts.

The current status of the pipeline is shown by the badge below:

[![CI](https://github.com/LoicSteve/AIMIGO_assignment/actions/workflows/main.yml/badge.svg)](https://github.com/LoicSteve/AIMIGO_assignment/actions/workflows/main.yml)

---

