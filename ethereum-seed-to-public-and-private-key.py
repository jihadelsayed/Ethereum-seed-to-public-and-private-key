import os
from mnemonic import Mnemonic
from bip32 import BIP32, HARDENED_INDEX
from eth_account import Account
import hashlib
os.system('color')
def copyRight():
        print('\033[95m' + """"
            ____   __ __       ____  ____  __ __   ____  ___          ___  _           _____  ____  __ __    ___  ___   
            |    \ |  |  |     |    ||    ||  |  | /    ||   \        /  _]| |         / ___/ /    ||  |  |  /  _]|   \  
            |  o  )|  |  |     |__  | |  | |  |  ||  o  ||    \      /  [_ | |        (   \_ |  o  ||  |  | /  [_ |    \ 
            |     ||  ~  |     __|  | |  | |  _  ||     ||  D  |    |    _]| |___      \__  ||     ||  ~  ||    _]|  D  |
            |  O  ||___, |    /  |  | |  | |  |  ||  _  ||     |    |   [_ |     |     /  \ ||  _  ||___, ||   [_ |     |
            |     ||     |    \  `  | |  | |  |  ||  |  ||     |    |     ||     |     \    ||  |  ||     ||     ||     |
            |_____||____/      \____||____||__|__||__|__||_____|    |_____||_____|      \___||__|__||____/ |_____||_____|
            look at www.neetechs.com for more script
            """ + '\033[0m')

# Replace with your mnemonic phrase
mnemonic_phrase = input("Please enter your seed phrase: ")

# Generate seed from mnemonic
mnemo = Mnemonic("english")
seed = mnemo.to_seed(mnemonic_phrase)

# Initialize BIP32
bip32 = BIP32.from_seed(seed)

# Derive the path m/44'/60'/0'/0/0
path = "m/44'/60'/0'/0/0"
derived_key = bip32.get_privkey_from_path(path)

# Convert the private key to hex
private_key = derived_key.hex()

# Create an Ethereum account from the private key
account = Account.from_key(private_key)

# Get the Ethereum address
address = account.address

print(copyRight())
print(f"Address: {address}")
print(f"Private Key: {private_key}")
