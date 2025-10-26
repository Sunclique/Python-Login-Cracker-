from flask import Flask, render_template_string, request
import hashlib

app = Flask(__name__)

# Dictionary to store usernames and their hashed passwords
user_db = {}

def hash_password(password):
    """Hashes a password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(username, password):
    """Registers a new user with a username and a hashed password."""
    user_db[username] = hash_password(password)

def authenticate_user(username, password):
    """Authenticates a user by verifying the provided password against the stored hash."""
    if username not in user_db:
        return "Username not found."
    if user_db[username] == hash_password(password):
        return "Login successful."
    return "Invalid password."

# Register users
register_user("John", "123456789")
register_user("Mary", "love")
register_user("Issy", "daddysgirl")
register_user("Faith", "SPONGEBOB")
register_user("Jay", "yougotserved")
register_user("Doe", "111111")
register_user("Mat", "password1")
register_user("Seth", "liverpool")
register_user("Joe", "Phello$hip_34")

HTML = """
<!doctype html>
<title>Login System</title>
<h2>Registered Users (hashed passwords)</h2>
<ul>
{% for user, pwd_hash in users.items() %}
  <li>{{ user }}: {{ pwd_hash }}</li>
{% endfor %}
</ul>
<h2>Login</h2>
<form method="post">
  Username: <input name="username"><br>
  Password: <input name="password" type="password"><br>
  <input type="submit" value="Login">
</form>
{% if result %}
  <p><strong>{{ result }}</strong></p>
{% endif %}
"""

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        result = authenticate_user(username, password)
    return render_template_string(HTML, users=user_db, result=result)

if __name__ == "__main__":
    app.run(debug=True)