from google.adk.agents import Agent

from .user_service_tools import userservice_readiness_check, login_to_bank
from .balance_reader_tools import balance_reader_readiness_check, get_balance
from .contacts_tools import contact_readiness_check, get_contacts

balance_reader_agent = Agent(
    name='balance_reader_agent',
    model="gemini-2.0-flash",
    description=(
        "Agent to help users see their account balance"
    ),
    instruction=(
        """You are an agent specializing in helping users login to their account balance.
        Tools you have access to:
        1. balance_reader_readiness_check : Checks if Bank of Anthos's Balance Reader API is ready for use.
        2. get_balance : Get user's account balance.

        If you don't have the JWT Token, return back to root agent.
        DO NOT ask user for JWT Token, or account number.
        """
    ),
    tools=[balance_reader_readiness_check, get_balance],
)

contacts_agent = Agent(
    name='contacts_agent',
    model="gemini-2.0-flash",
    description=(
        "Agent to help users see their account balance"
    ),
    instruction=(
        """You are an agent specializing in helping users get their contact information.
        Tools you have access to:
        1. contact_readiness_check : Checks if Bank of Anthos's Contacts API is ready for use.
        2. get_contacts : Get user's contacts. Requires JWT Token. 

        If you don't have the JWT Token, return back to root agent.
        DO NOT ask user for JWT Token, or account number.
        """
    ),
    tools=[contact_readiness_check, get_contacts],
)

root_agent = Agent(
    name="bank_of_anthos_agent",
    model="gemini-2.0-flash",
    description=(
        "Agent to help user access their financial information in the Bank of Anthos."
    ),
    instruction=(
        """You are an agent specializing in helping users access their financial information in the Bank of Anthos.

        ===================================================
        
        Sub-agents under you:

        1. balance_reader_agent : (AUTHENTICATION REQUIRED) Helps users get their account balance. 
        Transfer to this agent ONLY if you have the account number and the JWT token.
        DO NOT ask user for account number and token.

        2. contacts_agent : (AUTHENTICATION REQUIRED) Helps users get their contacts' information.
        Transfer to this agent ONLY if you have the username and JWT token.
        DO NOT ask user for username and token.

        ==================================================

        Tools under you:

        Tools you have access to:
        1. userservice_readiness_check : Checks if Bank of Anthos's User Service API function is ready to be used.
        2. login_to_bank : Login to Bank of Anthos. 
            From the login function, you get the following data:
            * jwt_token - Important for future API requests that require authentication
            * username
            * display name
            * account number - Important for future API requests that require an account number, like balance and transaction.
            * issued at
            * expires

        ==================================================

        You should run login_to_bank before transfering to a sub-agent, if not already run.

        """
    ),
    sub_agents=[balance_reader_agent, contacts_agent],
    tools=[userservice_readiness_check, login_to_bank]
)