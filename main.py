import logging
import os
from config import KEYWORDS, FILE_ROOT, LOG_LEVEL
from extractors.tika_extractor import extract_text
from utils.file_utils import get_all_files

# Configure logging to output to both console and file
logging.basicConfig(
    level=getattr(logging, LOG_LEVEL),
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('output.log', mode='w')
    ]
)
logger = logging.getLogger(__name__)

def extract_found_keywords(text, keywords):
    """
    Perform a case-insensitive search of keywords in the extracted text.
    Returns a list of keywords (as found) or an empty list if none are found.
    """
    text_lower = text.lower()
    found = [keyword for keyword in keywords if keyword.lower() in text_lower]
    return found

def process_file(file_path):
    """
    Process a single file:
      - Attempt to extract its text.
      - If extraction fails (and file is non-empty), mark as "Error extracting text".
      - Otherwise, search for keywords in a case-insensitive manner.
    Returns a tuple (file_path, result) where result is:
      - A comma-separated string of keywords found, or
      - "No keywords found" if extraction succeeded but nothing matched, or
      - "Error extracting text" if extraction failed.
    """
    logger.info(f"Processing file: {file_path}")

    try:
        text = extract_text(file_path)
    except Exception as e:
        logger.error(f"Unexpected error extracting text from {file_path}: {e}")
        return file_path, "Error extracting text"

    # Check for extraction failure:
    # If the file has a non-zero size but we got an empty result, assume extraction error.
    if not text:
        if os.path.getsize(file_path) > 0:
            logger.error(f"Extraction failed for non-empty file: {file_path}")
            return file_path, "Error extracting text"
        else:
            # File is empty; consider that as no keywords found.
            return file_path, "No keywords found"

    found_keywords = extract_found_keywords(text, KEYWORDS)
    if found_keywords:
        logger.info(f"Keywords found in {file_path}: {found_keywords}")
        return file_path, "|".join(found_keywords)
    else:
        logger.debug(f"No keywords found in {file_path}")
        return file_path, "No keywords found"

def scan_directory(root_path):
    """
    Traverse the root directory and process all files.
    Returns a list of tuples (file_path, result) for every file.
    """
    results = []
    all_files = get_all_files(root_path)
    logger.info(f"Found {len(all_files)} files to process.")
    for file_path in all_files:
        result = process_file(file_path)
        results.append(result)
    return results

if __name__ == '__main__':
    results = scan_directory(FILE_ROOT)

    # Write a summary file with the results
    summary_filename = 'summary.txt'
    with open(summary_filename, 'w', encoding='utf-8') as summary_file:
        summary_file.write("Files Summary:\n\n")
        for file_path, outcome in results:
            summary_file.write(f"{file_path}:\n")
            summary_file.write(f"  Keywords: {'|'.join(outcome)}\n\n")
    
    logger.info(f"Summary written to {summary_filename}")

    # Also log the summary to the console
    for file_path, outcome in results:
        logger.info(f"{file_path}: {outcome}")
