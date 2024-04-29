import json
import Levenshtein

class ConsensusPipeline:
    """Pipeline to run OCR extractors and determine the most accurate text using consensus."""

    def __init__(self, input_dir: str, output_dir: str):
        """Initialize the consensus pipeline with directory paths."""
        self.input_dir = input_dir
        self.output_dir = output_dir

    def read_results(self, extractor_name):
        """Read the results from a JSON file for a given extractor."""
        file_path = f"{self.output_dir}/{extractor_name}_results.json"
        with open(file_path, 'r') as file:
            return json.load(file)

    def determine_most_accurate(self, texts):
        """Determine the most accurate text using Levenshtein distance."""
        scores = {}
        for i, text1 in enumerate(texts):
            for j, text2 in enumerate(texts):
                if i < j:
                    # Calculate similarity score and store it
                    score = Levenshtein.ratio(text1, text2)
                    scores[(i, j)] = score
        # Select the text with the highest average similarity score
        avg_scores = [sum(scores.get((min(i, j), max(i, j)), 0) for j in range(len(texts))) / (len(texts) - 1) for i in range(len(texts))]
        most_accurate_index = avg_scores.index(max(avg_scores))
        return texts[most_accurate_index]

    def run(self):
        """Run the consensus algorithm on the extractor outputs."""
        # Read the results from the JSON files
        easyocr_results = self.read_results('easyocrextractor')
        pytesseract_results = self.read_results('pytesseractextractor')
        trocr_results = self.read_results('trocrextractor')

        # Ensure the results are in the same order and have the same image names
        assert len(easyocr_results) == len(pytesseract_results) == len(trocr_results), "Results length mismatch"

        final_results = []
        for i, easyocr_result in enumerate(easyocr_results):
            image_name = easyocr_result['image_name']
            assert image_name == pytesseract_results[i]['image_name'] == trocr_results[i]['image_name'], "Image name mismatch"

            texts = [easyocr_result['text'], pytesseract_results[i]['text'], trocr_results[i]['text']]
            most_accurate_text = self.determine_most_accurate(texts)
            final_results.append({'image_name': image_name, 'text': most_accurate_text})

        # Write the final results to a JSON file
        with open(f"{self.output_dir}/ocr_results.json", 'w', encoding='utf-8') as file:
            json.dump(final_results, file, indent=4)
