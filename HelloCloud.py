from flask import Flask
server = Flask(__name__)

@server.route("/")
def hello():
    return "TEST Hello Nitigan KMUTNB PRACHIN from Server"

if __name__ == "__main__":
    server.run(host='0.0.0.0', port=80)