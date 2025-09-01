import requests
from dotenv import load_dotenv
import os
from .utils import process_response

load_dotenv()

balance_reader_ip = os.getenv('BALANCE_READER')
port = os.getenv('PORT')
balance_reader_base_url = f'http://{balance_reader_ip}:{port}'

def balance_reader_readiness_check() -> bool :
    """
    Check readiness for the Balance Reader API of Bank of Athos.

    Returns:
        bool : True if the API is ready, False otherwise.
    """
    response = requests.get(f'{balance_reader_base_url}/ready')
    if response.status_code == 200 :
        return True
    return False

def get_balance(account_id: str, jwt_token: str) -> dict :
    """
    Get account balance of the user, given the username.

    Args:
        account_id (str) : Account number of the user
        jwt_token (str) : JWT token during login.

    Returns:
        dict : contains balance of user
    """

    headers = {'Authorization': f'Bearer {jwt_token}'}
    response = requests.get(f'{balance_reader_base_url}/balances/{account_id}', headers=headers)
    return process_response(response)