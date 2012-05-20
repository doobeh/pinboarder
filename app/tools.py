import hashlib

def generate_hash(*args):
    hash = hashlib.sha1()
    for arg in args:
        arg = arg.encode('ascii','ignore')
        hash.update(arg)
    return hash.hexdigest()