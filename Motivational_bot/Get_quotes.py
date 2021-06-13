import requests
import json
from Constants import quotesAPI


# helper function to return quotes from the api
def get_quote():
    response = requests.get(quotesAPI)
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return quote
