import bcrypt


def generate_hash(psw):
     # Convert password to bytes
    byte_psw = psw.encode('utf-8')
    # Generate a random salt
    salt = bcrypt.gensalt()
    # Create a hashed password using bcrypt
    hash = bcrypt.hashpw(byte_psw, salt)
    return hash.decode('utf-8')


def is_valid_hash(psw, hash):
    hash = generate_hash(psw)
    # Convert plain password to bytes
    byte_psw = psw.encode('utf-8')
    # Check if the password matches the stored hash
    is_valid = bcrypt.checkpw(byte_psw, hash.encode('utf-8'))
    return is_valid