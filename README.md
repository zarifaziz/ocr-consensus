# OCR Extraction Challenge

## Overview

This repository contains the codebase for the OCR Extraction Challenge, where the goal is to accurately extract text from a set of 75 images using three different OCR tools: EasyOCR, PyTesseract, and TrOCR. The extracted text is analyzed, discrepancies are resolved, and the most accurate output is determined and stored in a JSON file.

## Features

- Text extraction using EasyOCR, PyTesseract, and TrOCR.
- Analysis of OCR results to resolve discrepancies.
- Consensus-based approach for determining the most accurate text.
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

## Output

The final output will be a JSON file located in `data/final_results.json` with the following structure:

```json
[
{
"image_name": "image1.jpg",
"text": "Extracted text content."
},
...
]
```
