import json
import os
from typing import Dict, List

from loguru import logger

from .extractors import ExtractionProtocol


class OCRPipeline:
    """Pipeline to run an OCR extractor over all images in a directory and save the results."""

    def __init__(self, extractor: ExtractionProtocol, input_dir: str, output_dir: str):
        """Initialize the OCR pipeline with an extractor and directory paths."""
        self.extractor = extractor
        self.input_dir = input_dir
        self.output_dir = output_dir

    def process_images(self) -> List[Dict[str, str]]:
        """Process all images in the input directory with the extractor."""
        results = []
        for image_name in os.listdir(self.input_dir):
            if image_name.lower().endswith(".jpg"):
                image_path = os.path.join(self.input_dir, image_name)
                logger.info("Processing image: {}", image_path)
                text = self.extractor.extract(image_path)
                results.append({"image_name": image_name, "text": text})
        logger.info("Processed {} images", len(results))
        return results

    def save_results(self, results: List[Dict[str, str]]):
        """Save the OCR results to a JSON file."""
        extraction_method = type(self.extractor).__name__
        output_path = os.path.join(
            self.output_dir, f"{extraction_method.lower()}_results.json"
        )
        with open(output_path, "w") as json_file:
            json.dump(results, json_file, indent=4)
        logger.info("Results saved to {}", output_path)

    def run(self):
        """Run the OCR pipeline."""
        logger.info("OCR Pipeline started")
        results = self.process_images()
        self.save_results(results)
        logger.info("OCR Pipeline finished")
