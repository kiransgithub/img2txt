import os
import PIL.Image as Image
import cv2
import flask
import numpy as np
import pytesseract as pytesseract
from flask import request, jsonify
from werkzeug.utils import secure_filename
from ML_product_prediction import MLPrediction

app = flask.Flask(__name__)

app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return """<h1>Python Flask api - it will read the image and extract the text out of the image</h1>
              <h3>POST endpoint to be used: /extract_text_from_image with image as input document</h3>"""


@app.route('/extract_text_from_image', methods=['GET', 'POST'])
def test_api():
    req_status = 'success'
    if request.method == 'POST':
        print("request.files", request.files)
        uploaded_file = request.files['document']
        # data = json.load(request.files['data'])
        filename = secure_filename(uploaded_file.filename)
        uploaded_file.save(os.path.join('/Users/kiran/Desktop/img2txt', filename))
        # print(data, filename)
        print(filename)
        # print(img2txt(filename))
        req_status = img2txt(filename)
    else:
        req_status = 'Please use POST call to post the image!!'
    return jsonify(req_status)


# @app.route('/img2txt', methods=['POST'])
def img2txt(imgPath):
    """
    :type imgPath: Path to image file
    """
    path = '/Users/kiran/Desktop/img2txt/'

    # Read image with opencv
    img = cv2.imread(path + imgPath)

    # print(img)
    # Covert to gray
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply dilation and erosion to remove the noise
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)

    # Write image after removed noise
    cv2.imwrite("removed_noise.png", img)

    # Apply threshold to get image with only black and white
    # img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,31, 2)

    # Write the image after apply opencv to do some ..
    cv2.imwrite(imgPath, img)

    # Setting path to tesseract.exe
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    # Recognize text with tesseract for python
    result = pytesseract.image_to_string(Image.open(imgPath))
    print("result:", result)

    tempList = '\n'.join(MLPrediction.findCategory(result)).split('-')
    # Predict category based on the extracted text
    print("Category:",'\n'.join(MLPrediction.findCategory(result)).split('-')[0])

    resultDict = {
        'extracted_text': result,
        'category': tempList[0],
        'product' : tempList[1]
    }

    return resultDict


app.run(host='0.0.0.0', port=8080)
