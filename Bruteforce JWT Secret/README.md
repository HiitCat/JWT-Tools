# JWT Secret Brute Forcer 🔒

This script checks each entry from a given file to see if it's a valid secret key for a provided JWT (JSON Web Token). This tool can be used to understand how secure the 'secret' of a JWT is, and how susceptible it might be to brute force attacks.

**This script is intended for educational purposes only.**

In this repository you can find the **rockyou.txt** file, which is a list of the most common passwords.

## 👨‍💻 Author

- [Maxence ZOLNIERUCK](https://github.com/mxcezl)

## 📝 Requirements

Python 3.6 or above and the following packages:

- jwt
- argparse
- time
- colorama

Please refer to the `requirements.txt` file for the exact versions of these packages.

## 💻 Usage

```
python3 jwt-brute.py -t [TOKEN] -f [FILE]
```

Replace `[TOKEN]` with your JWT token and `[FILE]` with your file containing potential secret keys.

## 📖 Example

```
python3 jwt-brute.py -t eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoibG9sIiwiaWF0IjoxNjg1OTkxMTUyfQ.5KL4Gq43dIiuHbmruad2uJex4GjjUonf1u8TeMT-vog -f rockyou.txt
```

This script will iterate over each entry in the provided file and attempt to verify the JWT using that secret key. If a valid key is found, the script will print it out.

Please use this script responsibly and ethically. Misuse can lead to legal consequences.