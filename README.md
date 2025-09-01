# Bank of Anthos Agent SDK

A Python SDK for interacting with the Bank of Anthos microservices architecture using Google's Agent Development Kit (ADK). This project provides intelligent agents that can authenticate users and retrieve their financial information.

## Overview

Bank of Anthos Agent SDK creates AI-powered agents that interact with Bank of Anthos services to provide users with account information, balance details, and contact management through a conversational interface.

## Architecture

The SDK implements a multi-agent architecture:

- **Root Agent** (`bank_of_anthos_agent`): Main orchestrator that handles authentication and routing
- **Balance Reader Agent**: Specializes in retrieving account balance information
- **Contacts Agent**: Manages user contact information

## Features

- **Authentication**: Secure JWT-based login system
- **Balance Inquiries**: Retrieve account balance information
- **Contact Management**: Access user contact information
- **Service Health Checks**: Monitor API readiness across all services
- **Multi-Agent Architecture**: Specialized agents for different banking operations

## Prerequisites

- Python 3.7+
- Access to Bank of Anthos microservices
- Google ADK (Agent Development Kit)
- Valid service endpoints and authentication keys

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd adk-bank
```

2. Create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Configuration

1. Copy the example environment file:
```bash
cp bank_of_anthos/.env.example bank_of_anthos/.env
```

2. Update the `.env` file with your actual values:
```env
# Google AI Configuration
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=your_google_api_key_here

# Application Port
PORT=8080

# Microservice Endpoints
BALANCE_READER=your_balance_reader_ip
CONTACTS=your_contacts_service_ip
FRONTEND=your_frontend_service_ip
LEDGER_WRITER=your_ledger_writer_ip
TRANSACTION_WRITER=your_transaction_writer_ip
USER_SERVICE=your_user_service_ip

# JWT Configuration
CLUSTER_PUBLIC_KEY="-----BEGIN PUBLIC KEY-----\nYOUR_PUBLIC_KEY_HERE\n-----END PUBLIC KEY-----"
```

## Usage

### Basic Usage

```python
from bank_of_anthos.agent import root_agent

# Initialize the root agent
agent = root_agent

# The agent will handle authentication and route requests to appropriate sub-agents
# Users can ask questions like:
# - "What's my account balance?"
# - "Show me my contacts"
# - "Help me login to my account"
```

### Available Tools

#### User Service Tools
- `userservice_readiness_check()`: Check if User Service API is ready
- `login_to_bank()`: Authenticate user and obtain JWT token

#### Balance Reader Tools
- `balance_reader_readiness_check()`: Check if Balance Reader API is ready
- `get_balance()`: Retrieve account balance (requires authentication)

#### Contacts Tools
- `contact_readiness_check()`: Check if Contacts API is ready
- `get_contacts()`: Retrieve user contacts (requires authentication)

## API Services

The SDK integrates with the following Bank of Anthos microservices:

- **User Service**: Authentication and user management
- **Balance Reader**: Account balance retrieval
- **Contacts Service**: Contact information management
- **Ledger Writer**: Transaction recording
- **Transaction Writer**: Transaction processing
- **Frontend**: Web interface service

## Security

- All authenticated requests use JWT tokens
- Public key verification for token validation
- Secure credential management through environment variables
- No hardcoded sensitive information

## Development

### Project Structure

```
adk-bank/
├── bank_of_anthos/
│   ├── __init__.py
│   ├── agent.py                 # Main agent definitions
│   ├── utils.py                 # Utility functions
│   ├── user_service_tools.py    # User authentication tools
│   ├── balance_reader_tools.py  # Balance inquiry tools
│   ├── contacts_tools.py        # Contact management tools
│   ├── .env                     # Environment configuration
│   └── .env.example             # Example configuration
└── README.md
```

### Contributing

1. Ensure all environment variables are properly configured
2. Test authentication flows before implementing new features
3. Follow the existing agent pattern for new service integrations
4. Update documentation for any new tools or agents

## Troubleshooting

### Common Issues

**JWT Decode Error**: If you encounter `module 'jwt' has no attribute 'decode'`, ensure you're using the correct PyJWT version and parameter format.

**Service Connection Issues**: Verify that all service IPs in the `.env` file are correct and accessible.

**Authentication Failures**: Check that the `CLUSTER_PUBLIC_KEY` matches the key used by your Bank of Anthos deployment.

## License

This project is part of the Bank of Anthos ecosystem. Please refer to the main Bank of Anthos repository for licensing information.