from flask import Flask, request
import subprocess
import shlex
import sys

rpi_ip_addr = "100.10.24.70"

p = subprocess.Popen(shlex.split('/home/pi/dog_treat/mjpg-streamer/mjpg-streamer-experimental/mjpg_streamer -o "output_http.so -w ./www" -i "input_raspicam.so"'))


app = Flask(__name__)

@app.route('/')
def treat_ready():
    p2 = subprocess.Popen(["omxplayer", "test.mp3"])
    return '<html><head><title>Treat Dispenser</title></head>'+ \
    '<body><form action="/dispense" method="post"><input type="submit" name="submit" value="dispense some treats">'+ \
    '</form></body></html>'
    
@app.route('/dispense', methods=['POST','GET'])
def dispense_treat():
    if request.method == 'POST':
        if request.form['submit'] == "dispense some treats":
            p = subprocess.Popen([sys.executable, "stepper_motor.py"]) 
            return '<html><head><title>Dispensing</title></head><body><h1>Dispensing treats!'+\
                '</h1><a href="/">Head Back</a></body></html>'
        
if __name__=="__main__":
    try:
        app.run(host='0.0.0.0')
    except KeyboardInterrupt:
        1+1
        p.terminate()
        
