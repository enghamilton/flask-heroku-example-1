"""Flask App Project."""

from flask import Flask, jsonify, requests
app = Flask(__name__)

USERNAME = "enghamilton"
PASSWORD = "1234567"

LOGIN_URL = "https://github.com/login?return_to=%2Fenghamilton"
URL = "https://github.com/enghamilton?tab=repositories"

def main():
    #session_requests = requests.session()

    # Create payload
    payload = {
        "login": USERNAME, 
        "password": PASSWORD
    }

	#https ://pybit.es/requests-session.html
    with requests.Session() as session:
		post = session.post(LOGIN_URL, data=payload)
		r = session.get(URL)
    
    return (r.content)

@app.route('/')
def index():
    """Return homepage."""
    json_data = {'Hello': 'World!'}
    return jsonify(json_data)

@app.route('/login')
def index():
    """Return logged github page."""
    return main()

if __name__ == '__main__':
    app.run()
