import hashlib


def sha_256(n):
    return hashlib.sha256(n.encode()).hexdigest()
