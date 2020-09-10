import json
import requests

data = {'test1':1, 'test2':2}

#filename = '/Users/kiran/Desktop/HALF_MOON_RANCH_RESERVATION.PNG'

filename = '/Users/kiran/Desktop/img2txt/iphone_img2txt_sample.jpg'

# with open(filename, 'w') as f:
#     f.write('this is a test file\n')

url = "http://192.168.1.121:8080/extract_text_from_image"

files = [
    ('document', (filename, open(filename, 'rb'), 'application/octet')),
    ('data', ('data', json.dumps(data), 'application/json')),
]

r = requests.post(url, files=files)

print("r.status_code",r.status_code)

if r.status_code == 200:
    print("+===========================:Text content extracted from image:===========================================+")
    print(r.content.decode("utf-8"))
    print("+=========================================================================================================+")
else:
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print("Not able to extract text out of the image that is sent: ", filename)
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
