# Python-Login-Cracker
The project had two main parts:
🔑 1. Login & Authentication System
Built a simple login page in Python (login_system.py).
Usernames and passwords were stored securely as SHA-256 hashes (not plain text).
Included an authentication form that verifies user credentials and returns “Login successful” when correct.
🛠 2. Password Cracker (Brute Force + Dictionary Attack)
Implemented a password cracker (password_cracker.py) that takes hashed passwords from the login database and attempts to recover them.
Brute Force Attack: Tested all possible combinations up to a max length of 4 characters... (Trust me, 6 characters was a nightmare 😂😂)
Dictionary Attack: Leveraged a wordlist from rockyou.txt to instantly crack common passwords. (It has commonly used passwords, like think of any commonly used password and you would find it there... In fact, I would advise to go and check rockyou.txt, you just might find that the password you think is strong is very common)

📊 Key Findings:
Brute force could only crack very short passwords (≤4 characters) – because of the limit I placed. Anything longer consistently failed, though it still consumed 28–46 seconds searching.
Dictionary attacks were extremely effective against weak, common passwords, often succeeding in under 0.1 seconds. 
Strong, complex passwords with symbols and mixed cases (like Phello$hip_34) resisted both methods.

💡 Takeaway:
 This small project highlighted the real-world importance of using strong, non-dictionary, uncommon and complex passwords. Even with hashing in place, poor password practices remain the biggest vulnerability.

 You can download the password dictionary from this site: https://weakpass.com/wordlists/rockyou.txt

