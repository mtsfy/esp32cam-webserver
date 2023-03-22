import picoweb
import ulogging as logging
import gc
import ujson
from cam import Cam
from wifi import Wifi

app = picoweb.WebApp("ESP32-CAM Webserver")

def send_frame():
    while True:
        buf=Cam.snap()
        yield (b' --frame\r\nContent-Type: image/jpeg\r\n\r\n' + buf)
        del buf
        gc.collect()

@app.route("/")
def index(req, resp):
    yield from picoweb.start_response(resp)
    q="""
    <!DOCTYPE html>
    <html lang=en>
        <head>
            <title>ESP32-CAMERA</title>
        </head>
        <body>
            <center>
                <h1>ESP32 CAMERA</h1>
                <img src="/mjpeg" width="640" height="480"/>
            </center>
         </body>
    </html>
    """
    yield from resp.awrite(q)
    gc.collect()
    
@app.route("/mjpeg")
def index_mjpeg(req, resp):
    yield from picoweb.start_response(resp, content_type="multipart/x-mixed-replace; boundary=frame")
    try:
        while True:
#             Cam.flash_on()
            yield from resp.awrite(next(send_frame()))
            gc.collect()
    except:
        Cam.flash_off()
        gc.collect()
        
        
@app.route('/img')
def index_img(req, resp):
    yield from picoweb.start_response(resp, content_type="image/jpeg")
    buf=Cam.snap()
    yield from resp.awrite(buf)
    gc.collect()
    
class Web:
    def run_server():
        Wifi.connect()
        Cam.start()
        logging.basicConfig(level=logging.INFO)
        app.run(debug=True, host='0.0.0.0', port='80')