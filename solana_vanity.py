#!/usr/bin/env python3
"""
CPU brute-force Solana vanity generator.
"""

import sys
import time
import json
from solana.keypair import Keypair

def save_keypair_secretkey_bytes(secret_key_bytes, filename):
    arr = list(secret_key_bytes)
    with open(filename, "w") as f:
        json.dump(arr, f)
    print(f"Saved keypair to {filename}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 solana_vanity.py PREFIX")
        sys.exit(1)

    prefix = sys.argv[1]
    print(f"Searching for Solana address starting with: '{prefix}'")
    tries = 0
    t0 = time.time()
    try:
        while True:
            tries += 1
            kp = Keypair()
            pub = str(kp.public_key)
            if pub.startswith(prefix):
                elapsed = time.time() - t0
                print(f"FOUND after {tries} tries in {elapsed:.1f}s: {pub}")
                fname = f"{pub}.json"
                save_keypair_secretkey_bytes(kp.secret_key, fname)
                print(f"Run: solana-keygen pubkey {fname}")
                return
            if tries % 5000 == 0:
                rate = tries / max(1.0, time.time() - t0)
                print(f"tries={tries}  rate={rate:.1f} k/s  last={pub[:12]}...")
    except KeyboardInterrupt:
        print("\nInterrupted. Attempts:", tries)

if __name__ == "__main__":
    main()