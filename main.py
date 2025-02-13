# main.py

import logging
from config import KEYWORDS, FILE_ROOT, LOG_LEVEL
from extractors.tika_extractor import extract_text
from utils.file_utils import get_all_files

# Configure logging
logging.basicConfig(
    level=getattr(logging, LOG_LEVEL),
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),  # Output to console
        logging.FileHandler('output.log', mode='w')  # Also log to a file
    ]
)
logger = logging.getLogger(__name__)

def extract_found_keywords(text, keywords):
    """
    Given the full text and a list of keywords,
    return a list of keywords that are found in the text.
    This example uses a simple substring match (case-sensitive).
    """
    found = []
    for keyword in keywords:
        if keyword in text:
            found.append(keyword)
    return found

def process_file(file_path):
    """
    Process a single file: extract its text, find keywords, and return a tuple.
    Returns:
        (file_path, [list of found keywords]) if any keyword is found,
        or None if no keywords were found or text extraction failed.
    """
    logger.info(f"Processing file: {file_path}")
    text = extract_text(file_path)
    if text:
        found_keywords = extract_found_keywords(text, KEYWORDS)
        if found_keywords:
            logger.info(f"Keywords found in {file_path}: {found_keywords}")
            return file_path, found_keywords
        else:
            logger.debug(f"No keywords found in {file_path}")
    else:
        logger.warning(f"No text extracted from: {file_path}")
    return None

def scan_directory(root_path):
    """
    Traverse the root directory and process all files.
    Returns a list of tuples (file_path, found_keywords) for files with matches.
    """
    results = []
    all_files = get_all_files(root_path)
    logger.info(f"Found {len(all_files)} files to process.")
    for file_path in all_files:
        result = process_file(file_path)
        if result is not None:
            results.append(result)
    return results

if __name__ == '__main__':
    results = scan_directory(FILE_ROOT)

    # Write a summary file with the results
    summary_filename = 'summary.txt'
    with open(summary_filename, 'w', encoding='utf-8') as summary_file:
        summary_file.write("Files containing keywords:\n\n")
        for file_path, keywords in results:
            summary_file.write(f"{file_path}:\n")
            summary_file.write(f"  Keywords: {' | '.join(keywords)}\n\n")
    
    logger.info(f"Summary written to {summary_filename}")

    # Also log the summary to the console
    for file_path, keywords in results:
        logger.info(f"{file_path}: {', '.join(keywords)}")

