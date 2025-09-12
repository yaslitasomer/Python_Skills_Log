from flask import Flask, request

app = Flask(__name__)

# This will be our secret API key
VALID_TOKEN = 'faaalc97bd3f4bd9b024c708c979feca'

@app.route("/albums")
def get_albums():
    # 1. First, check the Authorization header
    auth_header = request.headers.get('Authorization')
    if auth_header and auth_header.startswith('Bearer '):
        access_token = auth_header.split(" ")[1]
        if access_token == VALID_TOKEN:
            return "Success! Access granted with Bearer token."
    
    # 2. If there's no Authorization header, check the query parameter
    access_token = request.args.get('access_token')
    if access_token == VALID_TOKEN:
        return "Success! Access granted with query parameter."
    
    # If neither method works, deny access
    return "Access Denied: Invalid token.", 401
    
if __name__ == "__main__":
    app.run(port=5000, debug=True)