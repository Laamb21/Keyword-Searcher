# tests/test_extractors.py

import unittest
from extractors.tika_extractor import extract_text
from main import extract_found_keywords  # Make sure main.py is importable
from config import KEYWORDS

class TestTikaExtractor(unittest.TestCase):
    def test_extract_keywords(self):
        sample_file = 'tests/sample.txt'
        text = extract_text(sample_file)
        # Print the entire extracted text for reference
        print("Extracted text:")
        print(text)
        # Now get only the keywords
        found_keywords = extract_found_keywords(text,KEYWORDS)
        print("Found keywords:")
        print(found_keywords)
        # Assert that at least one keyword was found (adjust your expected condition)
        self.assertGreater(len(found_keywords), 0, "No keywords were extracted from the sample file")

if __name__ == '__main__':
    unittest.main()

