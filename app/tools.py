import hashlib

def generate_hash(*args):
    hash = hashlib.sha1()
    for arg in args:
        hash.update(arg)
    return hash.hexdigest()