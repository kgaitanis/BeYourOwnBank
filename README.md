# Be Your Own Bank #
A tool to help you store your crypto wallet's seed phrase in a physical, secure and distributed way.

## What it does ##
Be Your Own Bank will encrypt your seed phrase with a password of your choice, and then it will split the encrypted seed phrase into as many parts as you like. You can specify how many of these parts are needed in order to reconstruct the original seed phrase.

For example, you can split your seed phrase in 3 parts and require that 2 of those are needed for reconstruction. This way you can keep these parts in separate places and even if one of them gets lost or destroyed, you can still recover your seed phrase.

Furthermore, owning any of these parts alone, does not provide any information whatsoever of the seed phrase. This means that a hacker who accessed one of these parts, will still require the same time to brute-force your seed phrase.

Even if someone gets access to a sufficient number of parts, he still needs the password in order to decrypt the seed phrase.

Finally, a PDF is generated for all the parts of the keys containing the hex value of the key as well as a QRCode which you can scan in order to recover your key. These PDFs can be printed, plastified and then stored in a safe physical location without worrying if someone might have a look at them.

## How it works
The splitting uses Shamir's Secret Sharing Scheme (https://en.wikipedia.org/wiki/Shamir%27s_Secret_Sharing)

... TBD ...

## Tips ##
You need to understand that when your seed phrase is being typed on your keyboard or displayed on your screen, it is a very dangerous moment where you are vulnerable to any kind of attacks. There's malware out there that can catch the content of your clipboard, track your keyboard strokes, read your screen, etc...

Make sure you take the necessary protections against all these threat vectors. Your computer must be absolutely trustworthy and preferentially not connected to the internet during that time.

* Verify this code before using it! Don't trust me, I might be sending your seed phrase on the internet...
* Avoid as much as possible typing your seed phrase in your computer. Best is to launch this script on a Virtual Machine with no internet connection.
* Clean the terminal output when you're done. Most terminals use the `Ctrl+K` shortcut.
* When printing the PDFs, connect to your printer with a cable instead of the WiFi if possible.
* Make sure you delete the PDF files after printing them and empty the trash. You don't want to leave those on your computer.
* Plastify the printed QRCodes to avoid deterioration over time. This is supposed to be long term storage.
* Store the QRCodes in separate trusted physical locations. Think about all possible scenarios : theft, fire, etc...
* Store the QRCodes inside a sealed envelope. Use wax and a seal to detect if anyone has opened the envelope.

## Setup ##
You will need Git and PIP already installed.

1. Clone the repository
`git clone https://`
2. Install dependencies
`./install-dependencies.sh`

## Usage ##
### Encryption
Open a terminal and do the following :
1. `./encrypt.py`
2. Enter total number of keys
3. Enter number of keys required for recomposing
4. Enter the secret that you wish to protect. This is usually your seed phrase.
5. Enter password that is used to encrypt the secret

Done!
The different parts of your keys are displayed on the terminal and PDF files with QRCode have been generated. They are named `key-N.pdf` with `N` going from `0` to the total number of parts.

Print the PDF files and make sure to delete them and empty the trash once you're done.

### Decryption
You first need to either scan the QRCodes from the printed papers, or manually enter them.
Make sure your internet connection is turned off when scanning the QRCodes since you will be using a 3rd party app for that.
Once you have the keys, in a terminal :
1. `./decrypt.py`
2. Enter the number of keys required to recompose the secret.
3. Enter the keys one by one in any order.
4. Enter the password you used to encrypt the secret.

Done!

Your secret seed phrase is now displayed on the terminal. Use it to restore your wallet and then make sure to clean the terminal output (`Ctrl+K` on most terminals).

## Licence ##
This software is delivered as is with no guarantees. Use at your own risk.
