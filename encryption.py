import tenseal as ts

def generate_encryption_context():
    """Generate a homomorphic encryption context."""
    context = ts.context(ts.SCHEME_TYPE.CKKS, poly_modulus_degree=8192, coeff_mod_bit_sizes=[60, 40, 40, 60])
    context.generate_galois_keys()
    context.generate_relin_keys()
    return context

def encrypt_data(data, context):
    """Encrypt data using CKKS."""
    return ts.ckks_vector(context, data)

def decrypt_data(encrypted_data):
    """Decrypt data."""
    return encrypted_data.decrypt()