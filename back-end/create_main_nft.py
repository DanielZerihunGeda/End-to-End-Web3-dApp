import os
from dotenv import load_dotenv
from algosdk import account, transaction
from algosdk.v2client import algod
# Load environment variables from .env file
load_dotenv()

# Get values from environment variables
creator_private_key = os.getenv("CREATOR_PRIVATE_KEY")
creator_address = os.getenv("CREATOR_ADDRESS")
algod_token = os.getenv("ALGOD_TOKEN")
algod_address = os.getenv("ALGOD_ADDRESS")

# Generate main asset named "Certificate"
def create_main_asset():
    # Set up Algorand client
    client = algod.AlgodClient(algod_token, algod_address)

    # Get suggested transaction parameters
    params = client.suggested_params()

    # Create AssetConfigTxn for the main asset "Certificate"
    txn = transaction.AssetConfigTxn(
        sender=creator_address,
        sp=params,
        total=1,  # Total units of the main asset
        default_frozen=False,
        unit_name="CERT",
        asset_name="Certificate",
        manager=creator_address,
        reserve=creator_address,
        freeze=creator_address,
        clawback=creator_address,
    )

    # Sign the transaction with the main asset creator's private key
    signed_txn = txn.sign(creator_private_key)

    # Submit the transaction to the Algorand blockchain
    txid = client.send_transaction(signed_txn)
    print(f"Main asset 'Certificate' created - Transaction ID: {txid}")

# Example usage:
create_main_asset()
