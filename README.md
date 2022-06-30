# Encrypt/Decrypt Messages

A simple Encryption/Decryption Python Program. Encrypt or Decrypt messages using the terminal in Visual Studio Code. 

## How It Works
Type in the message you want to encrypt in the terminal, and the program will output the secret message.

```
Input:
This is a secret message.

Output:
Gsrh rh z hvxivg nvhhztv-
```
Decrypting a message works the same.
```
Input:
Gsrh rh z hvxivg nvhhztv?

Output:
This is a secret message.
```

### Limitations:
1. Many special characters are not encrypted/decrypted, and they stay the same in both the input and output.
2. The conversion data is fixed (check [conversionData.py](https://github.com/RishiHub-S/Secret-Message-Decoder-Encoder/blob/bde71860185fca77414f5e7ef975db5fa85d8ba9/conversionData.py))
and does not change with every message that is encrypted/decrypted.
