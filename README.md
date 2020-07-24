# BullCrack

Password Hashing Detector & Cracker - POC

This HASH cracker will crack any algorithm of the following:
* MD5
* SHA-256
* SHA-512
* SHA-1

Wordlist:
* rockyou - top100.txt (changable)

## Installation

git clone into this repository:

```python
git clone https://github.com/idanbuller/BullCrack.git
```

## Usage

```python
python3 bullcrack.py

# Enter HASH to BullCrack it:
test = Bullhash("203b70b5ae883932161bbd0bded9357e763e63afce98b16230be33f0b94c2cc5")
test.cracker()
```
