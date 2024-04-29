import easyocr
import pytesseract
from PIL import Image
from transformers import TrOCRProcessor, VisionEncoderDecoderModel
from typing import Protocol, runtime_checkable
from loguru import logger


@runtime_checkable
class ExtractionProtocol(Protocol):
    """Define the interface for text extraction from images."""
    
    def __init__(self, *args, **kwargs):
        """Initialize the protocol with optional arguments."""
        pass

    def extract(self, *args, **kwargs):
        """Extract text from an image; must be implemented by subclasses."""
        raise NotImplementedError()

class PyTesseractExtractor(ExtractionProtocol):
    """Implements the ExtractionProtocol using PyTesseract to extract text from images."""

    def __init__(self, *args, **kwargs):
        """Initialize the PyTesseract extractor."""
        pytesseract.pytesseract.tesseract_cmd = kwargs.get(
            "tesseract_cmd", "/usr/bin/tesseract"
        )
        logger.info("PyTesseractExtractor initialized with tesseract_cmd: {}", pytesseract.pytesseract.tesseract_cmd)

    def extract(self, image_path: str):
        """Extract text from the given image while retaining case sensitivity and punctuation."""
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image, lang="eng")
        return text


class TrOCRExtractor(ExtractionProtocol):
    """Implements the ExtractionProtocol using TrOCR to extract text from images."""

    def __init__(self, *args, **kwargs):
        """Initialize the TrOCR processor and model."""
        self.processor = TrOCRProcessor.from_pretrained("microsoft/trocr-base-stage1")
        self.model = VisionEncoderDecoderModel.from_pretrained(
            "microsoft/trocr-base-stage1"
        )
        logger.info("TrOCRExtractor initialized with pretrained models")

    def extract(self, image_path: str):
        """Extract text from the given image while retaining case sensitivity and punctuation."""
        image = Image.open(image_path).convert("RGB")
        pixel_values = self.processor(images=image, return_tensors="pt").pixel_values
        generated_ids = self.model.generate(pixel_values)
        text = self.processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
        return text


class EasyOCRExtractor(ExtractionProtocol):
    """Implements the ExtractionProtocol using EasyOCR to extract text from images."""

    def __init__(self, *args, **kwargs):
        """Initialize the EasyOCR reader."""
        self.reader = easyocr.Reader(["en"], *args, **kwargs)
        logger.info("EasyOCR reader initialized")

    def extract(self, image_path: str):
        """Extract text from the given image while retaining case sensitivity and punctuation."""
        results = self.reader.readtext(image_path, detail=0)
        return " ".join(results)
