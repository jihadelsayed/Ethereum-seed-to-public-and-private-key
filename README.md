
# Ethereum Keypair Generator

A simple script to generate Ethereum keypairs and derive public keys from mnemonic phrases using Python.

## Features

- Generate an Ethereum keypair from a mnemonic phrase
- Derive an Ethereum address and private key
- Display the generated address and private key

## Prerequisites

- Python 3.x
- `mnemonic`, `bip32`, and `eth-account` libraries

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/jihadelsayed/BreadcrumbsEthereum-seed-to-public-and-private-key.git
   cd ethereum-keypair-generator
   ```

2. Install the required dependencies:
   ```bash
   pip install mnemonic bip32 eth-account
   ```

## Usage

1. Run the script:
   ```bash
   python ethereum_keypair_generator.py
   ```

2. Enter your mnemonic phrase when prompted:
   ```
   Please enter your seed phrase: your-seed-phrase-here
   ```

3. The script will generate a new keypair and display the Ethereum address and private key:
   ```
   Address: <generated-address>
   Private Key: <generated-private-key>
   ```

## License

This project is licensed under the MIT License.
