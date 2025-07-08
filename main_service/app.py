from flask import Flask, request, render_template, send_file
import time, cv2, numpy as np
import requests
from io import BytesIO

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    processed_image = None

    if request.method == 'POST':
        delay = int(request.form.get('delay', 10))
        file = request.files['image']
        image_bytes = file.read()

        # If expected delay > 60 → offload immediately
        if delay > 60:
            res = requests.post(
                'http://fast_microservice:5001/fast-process',
                files={'image': image_bytes}
            )
            processed_image = BytesIO(res.content)
            result = {
                'status': 'Offloaded to fast microservice',
                'latency': 'fast (~5s)'
            }
        else:
            # Simulate slow local processing
            start_time = time.time()
            time.sleep(delay)
            latency = time.time() - start_time

            # Convert to grayscale
            np_img = np.frombuffer(image_bytes, np.uint8)
            img = cv2.imdecode(np_img, cv2.IMREAD_COLOR)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            _, buf = cv2.imencode('.jpg', gray)
            processed_image = BytesIO(buf.tobytes())

            result = {
                'status': 'Processed by main service',
                'latency': latency
            }

        return send_file(processed_image, mimetype='image/jpeg')

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
