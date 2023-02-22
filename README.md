# restful-api.dev Automated Testing

### About
This project validates API (https://restful-api.dev/) requests using Python.

### Test cases
All test cases can be found here --> [Test Cases Google Drive Spreadsheet](https://docs.google.com/spreadsheets/d/1L1iMLvqR2pIhWtosHN5n9aBJv2TSCWrx7HEyHp5Ao3I/edit?usp=sharing)

### Installation
1. Ideally create a new virtual environment.
2. Install all packages according to the configuration file --> requirements.txt.
```commandline 
pip install -r requirements.txt
```
3. Run the tests.
```commandline
pytest -s -v test_cases/test_cases.py
```
