# AES Encryption/Decryption CBC Script 
Encrypt and Decrypt files (AES using CBC Mode) in Python. </br>
This script works well even in Windows devices because pycryptodome library is used in this project which works well in any O.S. 
## Getting Started

### Installation
* Python 3.x
* pycryptodome (Because pycrypto causes issue in windows devices that's why pycryptodome is used in this script)

You can install the missing dependencies thorugh `pip` or you can paste the below line in your cmd or terminal

`pip install pycryptodome`

### Tutorial
* Edit `config.json` file with desired key and iv
```json
{
    "key":"Enter Secret Key with size of 32",
    "iv":"Enter Secret Key with size of 16"
}
```
* Add your data which you want to encrypt or decrypt in input.txt file
* Run the script from terminal or cmd
`python aes_script.py'
* Select the desired option(Encryption or Decryption)
* You will get desired result in output.txt

## Contributing

1. Fork it
2. Create your feature branch: git checkout -b my-new-feature
3. Commit your changes: git commit -am 'Add some feature'
4. Push to the branch: git push origin my-new-feature
5. Submit a pull request

## Authors
* [RomReviewer(Script)](https://github.com/romreviewer)
* [Legrandin(pycryptodome)](https://github.com/Legrandin)
