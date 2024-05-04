from django.http import JsonResponse
import requests
import json
from mnemonic import Mnemonic
from eth_account import Account
from django.http import JsonResponse
from mnemonic import Mnemonic
from eth_account import Account

# Configuration
NODE_URL = "https://sepolia.infura.io/v3/095abe2ee7b4475b8a91649cdca18213"
FACTORY_CONTRACT_ADDRESS = "0x9406Cc6185a346906296840746125a0E44976454"
BUNDLER_API_URL = "https://api.stackup.sh/v1/node/bb59f8d1080b7c6f6b08afa1ac4d0fc21ea1a49bd14c6f9068b8c1dcbb57174e"
MNEMONIC = "2AB995365BA418B95885AA4AB7029D6D"

# Util function to interact with Ethereum node
def call_rpc(method: str, params: list) -> dict:
    headers = {'content-type': 'application/json'}
    data = {
        "jsonrpc": "2.0",
        "method": method,
        "params": params,
        "id": 1
    }
    response = requests.post(NODE_URL, headers=headers, data=json.dumps(data))
    return response.json()

# Util function to generate Ethereum address from mnemonic
# def generate_address_from_mnemonic(mnemonic: str) -> str:
#     entropy = Mnemonic().to_entropy(mnemonic)
#     private_key = Account.from_key(entropy)
#     return private_key.address

# Util function to submit EIP-4337 user operation to bundler
def submit_user_operation(address: str, to: str, value: int) -> dict:
    payload = {
        "address": address,
        "to": to,
        "value": value
    }
    response = requests.post(BUNDLER_API_URL, json=payload)
    return response.json()


def create_account(request):
    if request.method == 'GET':
        try:
            # Enable Mnemonic features
            Account.enable_unaudited_hdwallet_features()

            # Generate a valid mnemonic phrase
            mnemonic = Mnemonic("english").generate(strength=128)  # Use the desired language and strength
            
            # Generate private key from mnemonic
            private_key = Account.from_mnemonic(mnemonic).key.hex()
            address = Account.from_key(private_key).address
            
            return JsonResponse({"mnemonic": mnemonic, "private_key": private_key, "address": address})
        except ValueError as e:
            return JsonResponse({"error": str(e)}, status=500)
    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)
    
def generate_address_from_mnemonic(mnemonic):
    try:
        # Convert mnemonic to private key
        private_key = mnemonic_to_private_key(mnemonic)
        # Generate address from private key
        address = Account.from_key(private_key).address
        return address
    except ValueError as e:
        return str(e)

def mnemonic_to_private_key(mnemonic):
    try:
        # Convert mnemonic to entropy
        entropy = Mnemonic().to_entropy(mnemonic)
        # Use entropy to generate private key
        private_key = Account.from_key(entropy)
        return private_key
    except ValueError as e:
        raise ValueError("Error converting mnemonic to private key: " + str(e))