from flask import Flask, request, send_file
import cv2
import numpy as np
from io import BytesIO
import time

app = Flask(__name__)

@app.route('/fast-process', methods=['POST'])
def fast_process():
    image = request.files['image'].read()
    np_img = np.frombuffer(image, np.uint8)
    img = cv2.imdecode(np_img, cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, buf = cv2.imencode('.jpg', gray)
    time.sleep(5)  # Simulate fast processing
    return send_file(BytesIO(buf.tobytes()), mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
