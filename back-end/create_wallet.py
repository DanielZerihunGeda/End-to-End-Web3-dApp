from algosdk import account

# Generate a new Algorand account (wallet)
private_key, address = account.generate_account()

print("Private Key:", private_key)
print("Public Address:", address)
