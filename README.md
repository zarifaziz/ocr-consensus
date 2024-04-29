# OCR Extraction Challenge

## Overview

This repository contains the codebase for the OCR Extraction Challenge, where the goal is to accurately extract text from a set of 75 images using three different OCR tools: EasyOCR, PyTesseract, and TrOCR. The extracted text is analyzed, discrepancies are resolved, and the most accurate output is determined and stored in a JSON file.

## Features

- 3 independent text extraction pipelines using EasyOCR, PyTesseract, and TrOCR. 
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

## Issues Encountered during the extraction process

- Installing Tesseract separately on my mac was a challenge as it required XCode and some additional dependencies.
- Researched on consensus-based approaches was interesting. Ended up choosing Levenshtein distance algorithm to calculate similarity between the strings and it worked out very well.
- Initialising the extractors for trOCR and EasyOCR took some time to initialise. I was happy with the design decision to run each extraction pipeline independently that produced it's own JSON output. Decoupling the extractors from the consensus pipeline made things a lot simpler.
