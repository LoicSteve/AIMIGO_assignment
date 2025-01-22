# Makefile

# --------------------------------------------------------------------------------
# VARIABLES
# --------------------------------------------------------------------------------

PROJECT_NAME := "Aimigo_assignment"
PYTHON := python
PIP := pip

# Directory containing tests
TEST_DIR := ./tests

# --------------------------------------------------------------------------------
# TARGETS
# --------------------------------------------------------------------------------

# INSTALL
install:
	@echo "Installing dependencies..."
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

# TEST
test:
	pytest _etl_a9number_v3.py
	pytest --cov=$(TEST_DIR)
 

# FORMAT
format:
	@echo "Running Black formatter..."
	black src tests

# LINT
lint:
	@echo "Running pylint..."
	pylint src tests \
		--disable=R,C,W0612,E1120
# RUN
run:
	@echo "Running the main program..."
	$(PYTHON) -m src.main

# ALL
all: install lint test format