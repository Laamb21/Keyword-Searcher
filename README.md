# Keyword Searcher

Keyword Searcher is a Python project designed to scan through thousands of local documents (e.g., Word, Excel, PDF) and determine if they contain any predefined keywords. It uses Apache Tika (via the python-tika library) for text extraction and demonstrates logging, error handling, and modular design.

## Features
- **Multi-format support:** Leverages Apache Tika to extract text from various document types.
- **Keyword scanning:** Searches documents for predefined keywords.
- **Modular codebase:** Organized structure for easier maintenance and future extension.

## Setup Instructions

### 1. Create a virtual enviornment 

Open a terminal in the projcet directory and run:

- **Windows:** 
    '''bash
    python -m venv venv 
    venv\Scripts\activate

- **macOS/Linux**
python3 -m venv venv 
source venve/bin/activate

### 2. Install dependencies 

With the virtual enviornment activated, install the required packages:

    pip install -r requirements.txt

### 3. Configure the application 

Edit the config.py file to:

    - Set the list of keywords in the KEYWORDS variable
    - Update the FILE_ROOT variable to the directory containing your documents 
    - Adjust the logging using LOG_LEVEL if needed

### 4. Run the application 

Start the keyword scanning process by running:

    python main.py


## Testing 

To run unit tests (if available), execute: 

    python -m unittest discover


## Version Control 

For version control using Git, run these commands in your project folder:

    git init
    git add . 
    git commit -m "Initial commit: Setup Keyword Searcher codebase"

    