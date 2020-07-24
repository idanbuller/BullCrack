import hashlib
import detector


class Bullhash():

    def __init__(self, hashy):
        self.hashy = hashy
        self.hash_type = detector.obtain_hash_type(self.hashy)
        print(f"Hash type: {self.hash_type}")

    def cracker(self):
        with open('rockyou.txt', 'r') as f:
            for line in f:
                line = line.strip()
                if self.hash_type == "MD5":
                    hash_object = hashlib.md5(f"{line}".encode('utf-8'))
                    h = hash_object.hexdigest()
                if self.hash_type == "SHA-256":
                    hash_object = hashlib.sha256(f"{line}".encode('utf-8'))
                    h = hash_object.hexdigest()
                if self.hash_type == "SHA-512":
                    hash_object = hashlib.sha512(f"{line}".encode('utf-8'))
                    h = hash_object.hexdigest()
                if self.hash_type == "SHA-1":
                    hash_object = hashlib.sha1(f"{line}".encode('utf-8'))
                    h = hash_object.hexdigest()

                if h == self.hashy:
                    print(f"Found!\nthe password is -\n[*] {line} [*]")

# Enter HASH to BullCrack it:
test = Bullhash("203b70b5ae883932161bbd0bded9357e763e63afce98b16230be33f0b94c2cc5")
test.cracker()

