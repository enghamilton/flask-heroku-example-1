"""Flask App Project."""

from flask import Flask, jsonify

import requests
from lxml import html

USERNAME = "enghamilton"
PASSWORD = "*******7"

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
		try:
			#with open(filename) as f:
			f = open("demofile.txt","w")
			f.write(r.content)
		except:
			print("Something went wrong when writing to the file")
		finally:
			f.close()
		  
    return (r.content)

app = Flask(__name__)


@app.route('/')
def index():
    """Return homepage."""
    json_data = main()
    return json_data


if __name__ == '__main__':
    app.run()
