#!/usr/bin/python3
from asyncore import write
from flask import Flask, redirect, request, render_template, url_for, Response
from pythonping import ping
import os
import requests
import telnetlib

picto_server_ip = os.getenv('PICTO_SERVER_IP_ADDRESS')

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def ping_to_server():

    if request.method == "GET":
        user_email = request.args.get('email')

        try:
            telnetlib.Telnet(str(picto_server_ip), "80")
            picto_uri = "http://"+picto_server_ip+"/monster/"+str(user_email)+"?size=200"

            pictography = requests.get(url=str(picto_uri))
            image = pictography.content

            return image
        except:
            return "", 504
            
@app.route("/hello_world/")            
def hello():
    return 'Hello, World!'

if __name__ == "__main__":
  app.run(debug=False, host="0.0.0.0", port=80)


