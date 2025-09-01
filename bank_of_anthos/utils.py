from requests import Response
import jwt
import datetime
from decimal import Decimal
from dotenv import load_dotenv
import os 

load_dotenv()

CLUSTER_PUBLIC_KEY = os.getenv('CLUSTER_PUBLIC_KEY')
TIMESTAMP_FORMAT = os.getenv('TIMESTAMP_FORMAT')

def process_response(response: Response) -> dict :
    
    if response.status_code == 200 :
        return response.json()
    
    return {
        'success' : False,
        'status code' : response.status_code,
        'response' : response.text
    }

def decode_token(token):
    return jwt.decode(algorithms='RS256',
                    jwt=token,
                    options={"verify_signature": False})

def verify_token(token):
    """
    Validates token using userservice public key
    """
    if token is None:
        return False
    try:
        jwt.decode(token,
                   key=CLUSTER_PUBLIC_KEY,
                   algorithms=['RS256'],
                   options={"verify_signature": True})
        return True
    except jwt.exceptions.InvalidTokenError as err:
        return False
    
# register html template formatters
def format_timestamp_day(timestamp):
    """ Format the input timestamp day in a human readable way """
    # TODO: time zones?
    date = datetime.datetime.strptime(timestamp, TIMESTAMP_FORMAT)
    return date.strftime('%d')

def format_timestamp_month(timestamp): 
    """ Format the input timestamp month in a human readable way """
    # TODO: time zones?
    date = datetime.datetime.strptime(timestamp, TIMESTAMP_FORMAT)
    return date.strftime('%b')

def format_currency(int_amount):
    """ Format the input currency in a human readable way """
    if int_amount is None:
        return '$---'
    amount_str = '${:0,.2f}'.format(abs(Decimal(int_amount)/100))
    if int_amount < 0:
        amount_str = '-' + amount_str
    return amount_str