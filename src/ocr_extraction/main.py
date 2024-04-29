import typer

from .consensus import ConsensusPipeline
from .extractors import EasyOCRExtractor, PyTesseractExtractor, TrOCRExtractor
from .ocr_pipeline import OCRPipeline

app = typer.Typer()


@app.command()
def pytesseract():
    """Run the OCR pipeline using PyTesseract."""
    extractor = PyTesseractExtractor()
    pipeline = OCRPipeline(extractor, "data/selected_images", "data")
    pipeline.run()


@app.command()
def easyocr():
    """Run the OCR pipeline using EasyOCR."""
    extractor = EasyOCRExtractor()
    pipeline = OCRPipeline(extractor, "data/selected_images", "data")
    pipeline.run()


@app.command()
def trocr():
    """Run the OCR pipeline using TrOCR."""
    extractor = TrOCRExtractor()
    pipeline = OCRPipeline(extractor, "data/selected_images", "data")
    pipeline.run()

@app.command()
def consensus():
    """Run the OCR consensus pipeline."""
    pipeline = ConsensusPipeline("data/selected_images", "data")
    pipeline.run()

if __name__ == "__main__":
    app()
