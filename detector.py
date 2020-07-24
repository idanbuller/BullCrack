import re

HASH_TYPE_REGEX = {
    re.compile(r"^[a-f0-9]{32}(:.+)?$", re.IGNORECASE):  ["MD5"],
    re.compile(r"^[a-f0-9]{64}(:.+)?$", re.IGNORECASE):  ["SHA-256"],
    re.compile(r"^[a-f0-9]{128}(:.+)?$", re.IGNORECASE): ["SHA-512"],
    re.compile(r"^[a-f0-9]{56}$", re.IGNORECASE):        ["SHA-224"],
    re.compile(r"^[a-f0-9]{40}(:.+)?$", re.IGNORECASE):  ["SHA-1"],
    re.compile(r"^[a-f0-9]{96}$", re.IGNORECASE):        ["SHA-384"],
    re.compile(r"^[a-f0-9]{16}$", re.IGNORECASE):        ["MySQL323"],
    re.compile(r"^[a-f0-9]{48}$", re.IGNORECASE):        ["Haval-192"]
}


def obtain_hash_type(check_hash):
    for algorithm, items in HASH_TYPE_REGEX.items():
        if algorithm.match(check_hash):
            for i in range(1):
                for item in items:
                    return item
