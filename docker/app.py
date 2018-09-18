#!/usr/bin/env python
from   flask import Flask, request
import os
from   time  import sleep

app = Flask("Process Data")

@app.route('/')
def process_this_data():
    data     = request.data.decode()
    # DATA PROCESSING GOES HERE!
    sleep(5)
    response = "Container '{hostname}' processing '{data}'.\n"
    response = response.format(hostname=os.environ['HOSTNAME'], data=data)
    return response
