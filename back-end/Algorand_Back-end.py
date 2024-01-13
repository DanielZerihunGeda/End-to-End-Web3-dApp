from flask import Flask, request, jsonify
from algosdk import algod, account, mnemonic, transaction, util
import json
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Algorand node connection parameters
algod_address = os.getenv("ALGOD_ADDRESS")
algod_token = os.getenv("ALGOD_TOKEN")

# Algorand account details 
creator_address = os.getenv("CREATOR_ADDRESS") #Public key of creator
creator_mnemonic = os.getenv("CREATOR_MNEMONIC")
creator_private_key = os.getenv("CREATOR_PRIVATE_KEY")
creator_public_key = os.getenv("CREATOR_PUBLIC_KEY")

@app.route('/Create_NFT', methods=['POST'])
def create_nft():
    try:
        # Extract parameters from the request
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')

        # Combine first and last name with an underscore
        asset_name = f"{first_name}_{last_name}"

        # Initialize Algorand client
        algod_client = algod.AlgodClient(algod_token, algod_address)

        # Retrieve creator account information
        creator_private_key_bytes = mnemonic.to_private_key(creator_mnemonic)
        creator_public_key_bytes = account.address_from_private_key(creator_private_key_bytes)

        # Ensure the provided private and public keys match the mnemonic
        if (
            creator_private_key_bytes != bytes.fromhex(creator_private_key)
            or creator_public_key_bytes != bytes.fromhex(creator_public_key)
        ):
            return jsonify({'error': 'Invalid private/public key or mnemonic'}), 400

        # Create a new unique asset ID
        asset_id = util.asset_id_from_name(asset_name.encode())

        # Check if the asset already exists
        if not algod_client.asset_exists(asset_id):
            # Create NFT asset
            txn = transaction.AssetConfigTxn(
                sender=creator_public_key,
                sp=algod_client.suggested_params(),
                total=1,  # Only one NFT per call
                decimals=0,
                unit_name="NFT",
                asset_name=asset_name,
                default_frozen=False,
                manager=creator_public_key,
                reserve=creator_public_key,
                freeze=creator_public_key,
                clawback=creator_public_key,
                url=json.dumps(request.form.to_dict()),
                metadata=json.dumps(request.form.to_dict()),
            )

            # Sign the transaction
            signed_txn = txn.sign(creator_private_key_bytes)

            # Submit the transaction
            tx_id = algod_client.send_transaction(signed_txn)

            # Return the transaction ID as a response
            return jsonify({'transaction_id': tx_id})
        else:
            return jsonify({'error': f'Asset with name {asset_name} already exists'}), 400

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
