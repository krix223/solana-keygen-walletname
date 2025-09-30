# Solana Vanity Address Generator

Generate Solana wallets with a desired starting prefix.

## Features
- CPU brute force address generation
- Saves wallet as JSON compatible with `solana-keygen`
- Shows progress stats while searching

## Requirements
- Python 3.9+
- [`solana-py`](https://github.com/michaelhly/solana-py)
- [`base58`](https://pypi.org/project/base58/)

## Install

```bash
git clone https://github.com/YOUR-USERNAME/solana-vanity-gen.git
cd solana-vanity-gen
pip install -r requirements.txt
```

## Usage

```bash
python solana_vanity.py PREFIX
```

Replace `PREFIX` with your desired wallet address prefix.

### Example

```bash
python solana_vanity.py SOL
```

When a match is found, the script will output something like:

```
FOUND after 34021 tries in 7.2s: SOL8ZpX1LQW...
Saved keypair to SOL8ZpX1LQW....json
```

You can verify the generated address with:

```bash
solana-keygen pubkey SOL8ZpX1LQW....json
```

Wallet files are saved in JSON format compatible with `solana-keygen`.

## License

MIT