import json
import os
import capsolver
import requests
from urllib.parse import urlparse


capsolver.api_key = "your capsolver.com key"
PAGE_URL = "https://www.latamairlines.comr"
PAGE_KEY  = "6LcWzLoiAAAAAGJqY_Qn6XCssS6v6mlGqNg0qa3b"
PAGE_ACTION = "SEARCH_OFFERS"

def solve_recaptcha_v3(url,key,pageAction):
    solution = capsolver.solve({
        "type": "ReCaptchaV3EnterpriseTaskProxyless",
        "websiteURL": url,
        "websiteKey":key,
        "pageAction":pageAction
    })
    return solution


def main():
    
    print("Solving reCaptcha v3")
    solution = solve_recaptcha_v3(PAGE_URL, PAGE_KEY, PAGE_ACTION)
    print("Solution: ", solution)

if __name__ == "__main__":
    main()
