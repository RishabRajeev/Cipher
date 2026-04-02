import math

def simple_hash(text):
    # A simple polynomial rolling hash function.
    # It returns a fixed-length integer.
    
    hash_val = 0
    prime = 31 # A small prime commonly used in hashing
    mod = 10**9 + 7 # A large prime to keep the hash within bounds
    
    for i, char in enumerate(text):
        # (ASCII value * prime^position) % mod
        hash_val = (hash_val + ord(char) * pow(prime, i, mod)) % mod
    return hash_val

def gcd(a, b):
    while b: a, b = b, a % b
    return a

def inverse(k, m):
    for i in range(1, m):
        if (k * i) % m == 1: return i
    return None

def mult_cipher(text, key, mode='encrypt'):
    m = 26
    res = ""
    if mode == 'decrypt': key = inverse(key, m)
    
    for char in text.upper():
        if char.isalpha():
            x = ord(char) - ord('A')
            res += chr(((x * key) % m) + ord('A'))
        else:
            res += char  
    return res

# --- Execution Flow ---
msg = "HELLO WORLD"
key = 7

# 1. Generate the 'Fingerprint' using our custom hash
original_hash = simple_hash(msg)

# 2. Encrypt
encrypted = mult_cipher(msg, key, mode='encrypt')

# 3. Decrypt
decrypted = mult_cipher(encrypted, key, mode='decrypt')

# 4. Verify Integrity
decrypted_hash = simple_hash(decrypted)

print(f"Message:   {msg}")
print(f"Hash:      {original_hash}")
print(f"Encrypted: {encrypted}")
print(f"Decrypted: {decrypted}")

if original_hash == decrypted_hash:
    print("Success: The hash matches. Data is authentic.")
else:
    print("Error: Hash mismatch! Data was corrupted.")