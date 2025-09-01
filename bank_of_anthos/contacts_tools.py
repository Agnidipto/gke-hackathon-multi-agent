import requests
from dotenv import load_dotenv
import os
from .utils import process_response

load_dotenv()

contact_ip = os.getenv('CONTACTS')
port = os.getenv('PORT')
contacts_base_url = f'http://{contact_ip}:{port}'

def contact_readiness_check() -> bool:
    """
    Check readiness for the Contacts API of Bank of Athos

    Returns:
        bool : True if the API is ready, False otherwise.
    """
    response = requests.get(f'{contacts_base_url}/ready')
    if response.status_code == 200 :
        return True
    return False

def get_contacts(username: str, jwt_token: str) :
    """
    Get the bank and account details of the contacts of the user. 
    Requires authentication.

    Args:
        username (str) : Username of the user
        jwt_token (str) : JWT token during login.
    """
    headers = {'Authorization': f'Bearer {jwt_token}'}
    url = f'{contacts_base_url}/contacts/{username}'
    response = requests.get(url, headers=headers)
    return process_response(response)
