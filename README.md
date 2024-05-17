# OCR Text Extraction Tool

## Overview

This repository hosts an open-source OCR text extraction tool that utilizes three different OCR technologies: EasyOCR, PyTesseract, and TrOCR. It is designed to extract text from images, analyze the results for discrepancies, and use the Levenshtein distance as the consensus algorithm to determine the most accurate text extraction, which is then stored in a JSON file.

## Features

- Three independent text extraction pipelines using EasyOCR, PyTesseract, and TrOCR.
- Analysis of OCR results to identify and resolve discrepancies.
- Consensus-based approach using Levenshtein distance for determining the most accurate text extraction.
- JSON output of the final, correct text for each image.

## Requirements

- Python 3.11
- Poetry for dependency management

## Installation

To set up the project environment:

```
poetry install
```

## Usage

To run the OCR pipeline:

```
python -m src.ocr_extraction.main pytesseract
python -m src.ocr_extraction.main easyocr
python -m src.ocr_extraction.main trocr
```

Run the consensus pipeline to generate the final JSON
```
python -m src.ocr_extraction.main consensus
```

## Output

The final output will be a JSON file located in `data/ocr_results.json` with the following structure:

```json
[
    {
    "image_name": "image1.jpg",
    "text": "Extracted text content."
    },
    ...
]
```
