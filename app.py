from flask import Flask
import requests

#x = requests.get('https://w3schools.com/python/demopage.htm')
x = requests.get('http://pizzaria2.000webhostapp.com/android_connect/get_all_products.php')

app = Flask(__name__)

@app.route("/")
def hello():
    #return "Hello World!"
	return x.text

if __name__ == "__main__":
    app.run()
