# filepath: python-login-cracker/python-login-cracker/src/password_cracker.py

import hashlib
import itertools
import time

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def brute_force_crack(hashed_password, max_length=4):
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    for length in range(1, max_length + 1):
        for attempt in itertools.product(characters, repeat=length):
            attempt_password = ''.join(attempt)
            if hash_password(attempt_password) == hashed_password:
                return attempt_password
    return None

def dictionary_crack(hashed_password, dictionary_file):
    with open(dictionary_file, 'r', encoding='utf-8', errors='ignore') as file:
        for line in file:
            password = line.strip()
            if hash_password(password) == hashed_password:
                return password
    return None

# Example usage:
hashed = 'cc8d951fa25a47594883b020ce7ee6013409a5678c66f14f140a22971f558755'  

start = time.time()
result = brute_force_crack(hashed)
end = time.time()
print(f"Brute-force result: {result} (Time: {end - start:.2f} seconds)")

start = time.time()
result = dictionary_crack(hashed, r'C:\Users\Admin\Downloads\python-login-cracker\rockyou.txt')  
end = time.time()
print(f"Dictionary result: {result} (Time: {end - start:.2f} seconds)")