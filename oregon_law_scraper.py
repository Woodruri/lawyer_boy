"""
Law Scraper for lawyer boy RAG
"""

"""
IMPORTS
"""
import requests
from bs4 import BeautifulSoup
import json
import time
from pathlib import Path
from datetime import datetime
import logging


"""
FUNCS
"""
def test_connection():
    '''
    test that we are properly connecting to the court website
    returns True if found
    returns False if not found
    '''

    #starting with just https://www.courts.oregon.gov/publications/sc/pages/default.aspx
    url = "https://www.courts.oregon.gov/publications/sc/pages/default.aspx"

    try:
        response = requests.get(url, timeout=10)
        print(f"Connection successful, status code: {requests.status_codes}")
        return True
    except Exception as e:
        print(f"connection failed: {e}")
        return False
    
def main_wrapper():
    print("testing connection to oregon courts website")
    test_connection()

"""
MAIN
"""
if __name__ == "__main__":
    main_wrapper()