from flask import Flask, jsonify
import netifaces as ip
import requests
import socket


app = Flask(__name__)
getawsip = "0.0.0.0"
getcount = -1

try:
    getawsip = requests.get('http://169.254.169.254/latest/meta-data/public-ipv4').text
    pass
except Exception as exc:
    getawsip = "0.0.0.0"


@app.route("/")
def path():
 return "Tiger Enterprises Web API v1.0\n"


@app.route("/aws-ip")
def awsip():
    return jsonify({'aws-ip' : getawsip})


@app.route("/container-ip")
def conip():
    getconip = ip.ifaddresses("eth0")[ip.AF_INET][0]['addr']
    return jsonify({'container-ip': getconip})


@app.route("/container-hostname")
def conhost():
    getconhost = socket.gethostname()
    return jsonify({'container-hostname': getconhost})


@app.route("/local-count")
def count():
    global getcount
    getcount = getcount + 1
    return jsonify({'local-count':getcount})


 @app.route("/all")
def allinfo():
    global getcount
    getcount += 1
    getconip = ip.ifaddresses("eth0")[ip.AF_INET][0]['addr']
    return jsonify({'aws-ip': getawsip, 'container-ip': getconip, 'container-hostname': socket.gethostname(), 'local-count': getcount})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
