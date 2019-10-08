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
		'''
		try:
			#with open(filename) as f:
			f = open("demofile.txt","w")
			f.write(r.content)
		except:
			print("Something went wrong when writing to the file")
		finally:
			f.close()
		'''
    return (r.content.text)

app = Flask(__name__)


@app.route('/')
def index():
    """Return homepage."""
    json_data = {'pid':'1', 'pid':'2', 'pid':'3'}
    x = requests.get('https://w3schools.com/python/demopage.htm')
    #return jsonify(json_data)
    return x
    
    '''response = make_response(main())
    response.headers["content-type"] = "text/plain"
    return response'''

if __name__ == '__main__':
    app.run()
