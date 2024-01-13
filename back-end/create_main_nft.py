from algosdk.v2client import algod

def check_algorand_connection():
    # Replace these values with your Algorand node information
    algod_address = "YOUR_ALGOD_API_ADDRESS"
    algod_token = "YOUR_ALGOD_API_TOKEN"

    try:
        # Create an Algod client
        client = algod.AlgodClient(algod_token, algod_address)

        # Check the status of the Algorand node
        status = client.status()
        print("Algorand node status:", status)

        # If you reach this point without errors, the connection is successful
        print("Connection to Algorand node successful")

    except Exception as e:
        # Print any exception that occurred during the connection attempt
        print("Error connecting to Algorand node:", e)

if __name__ == "__main__":
    check_algorand_connection()
