import requests
from dotenv import load_dotenv
import os
from typing import Dict
from .utils import decode_token

load_dotenv()

user_service_ip: str = os.getenv("USER_SERVICE")
port: str = os.getenv("PORT")
base_url: str = f'http://{user_service_ip}:{port}'

def userservice_readiness_check() -> bool:
    """
    Checks if Bank of Anthos's User Service API function is ready.

    Returns:
        bool: True if the API is ready, False otherwise.
    """
    response = requests.get(f'{base_url}/ready')
    if response.status_code == 200:
        return True
    return False
    
def login_to_bank(username: str, password: str) -> Dict[str, str]:
    """
    Login to Bank of Anthos with username and password. 
    Get a JWT token in return, which you need to save for future API requests to the Bank's backend system.

    Args:
        username (str): The username provided by user.
        password (str): The password provided by user.

    Returns:
        dict: Contains the token, username, account number, display name, issued at, and expires. 
        You need to save the token for future API authentication.
        You need to save the account number for api calls to see balance, transactions, etc.
    """

    params={'username': username, 'password': password}
    response: Dict[str, str] = requests.get(f'{base_url}/login', params=params)

    if response.status_code == 500:
        return {
            'success': False,
            'error': 'Internal Server Error'
        }
    
    if response.status_code == 401:
        return {
            'success': False,
            'error': 'Incorrect username or password'
        }
    
    if response.status_code == 200:
        token: str = response.json()['token']
        token_data = decode_token(token)

        data = {
            'jwt_token' : token,
            'display_name' : token_data['name'],
            'account_number' : token_data['acct'],
            'username' : token_data['user'],
            'issued' : token_data['iat'],
            'expires' : token_data['exp']
        }

        return data

