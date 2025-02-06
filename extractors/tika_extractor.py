# extractors/tika_extractor.py

from tika import parser
import logging

logger = logging.getLogger(__name__)

def extract_text(file_path):
    """
    Extract text from a file using Apache Tika.
    Returns the text content as a string.
    """
    try:
        parsed = parser.from_file(file_path)
        text = parsed.get("content", "")
        if text:
            return text.strip()
        else:
            logger.debug(f"No content extracted from: {file_path}")
            return ""
    except Exception as e:
        logger.error(f"Error extracting text from {file_path}: {e}")
        return ""
