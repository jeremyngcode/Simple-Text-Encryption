Simple Text Encryption
======================

Encryption ([Encrypt_Msg.py](Encrypt_Msg.py))
---------------------------------------------
For message encryption, run this file.

The first thing that gets printed in the terminal will be..

### `Do you need a fresh Fernet Secret Key? (y/n)`
If you don't already have an existing key or need a new one, input `yes` and a fresh one will be generated for you. Otherwise, input `no`.

Keep this key some place safe.

### `Enter the text you want to encrypt: `
Example: `a secret message revealed only to those who have the secret key!`

### `Enter your Secret Key: `
This same key will also be used for decryption.

### `Enter filename: `
A Fernet Token (basically a string of characters) will be saved in a new text file. You will need this token together with your Secret Key to reveal the original plaintext message.

### `Encryption complete, Fernet Token saved to "{file_path}"`
You should see this message printed if all went well!

Decryption ([Decrypt_Msg.py](Decrypt_Msg.py))
---------------------------------------------
To reveal the original plaintext message of a Fernet Token, run this file.

The first thing that gets printed in the terminal will be..

### `Enter your Secret Key: `
Enter it.

### `Is the Fernet Token in a file? (y/n)`
`yes` to decrypt from a file outputted from this app previously; `no` to key in your token manually by copy-pasting. If `yes`, you will be prompted to enter the file path.

At this point, if the token is valid, you should see the original plaintext message printed.

---

- [cryptography](https://pypi.org/project/cryptography/)
