from flask import Flask, render_template, Response
import os
HOME = os.path.join('static', 'image')
server = Flask(__name__)
server.config['UPLOAD'] = HOME
server.config['SEND_FILEMAX_AGE_DEFAULT'] = 0
@server.route("/")
def index():
    full_filename = os.path.join(server.config['UPLOAD'], 'img1.jpg')
    full_filename1 = os.path.join(server.config['UPLOAD'], 'img2.jpg')
    return render_template('index.html', feed1 = full_filename, feed2 = full_filename1)

@server.after_request
def add_header(r):
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r
if __name__ == "__main__":
   server.run(host='0.0.0.0', port = 5000)

