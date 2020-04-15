
import cv2
import numpy as np

import cv2

from flask import Flask, render_template, request
#from flask_ngrok import run_with_ngrok
import os
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
model = load_model('covid19.model')
# summarize model.
#model.summary()
def predict(image):
    
    image = np.array(cv2.resize(image, (224,224) ) ).reshape((1, 224, 224, 3)) /255.0
    return model.predict(image)[0]  

  



app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
#run_with_ngrok(app)
@app.route('/', methods=['post', 'get'])
def login():
    
    message = ''
    
    #if request.method == 'POST':
        
        
        #f = request.files['file']
      #  f.save(secure_filename("e1.jpg"))
      #print(len(f.stream.read() ))
      #decoded = cv2.imdecode(np.frombuffer(image_bytes, np.uint8), -1)
        #decoded = cv2.imdecode(np.frombuffer(f.stream.read() , np.uint8), -1)
       # a=cv2.imread("e1.jpg")
       # print('OpenCV:\n', a)
        #print(a.shape)
       # message="8888888888888888888888"
       
       
        
    
    return render_template('index.html')





@app.route('/predict', methods = ['GET', 'POST'])
def upload_file():
    
    
    
  



    positive="20"
    negative = "20"
    
    if request.method == 'POST':
        
        f = request.files['file']
        
        image = cv2.imdecode(np.frombuffer(f.stream.read() , np.uint8), -1)
        #f.save("D:/deep learn/p_pr/project 2/static/images/"+nom_image)

        cv2.imwrite("static/a.jpg",image)
        positive,negative=predict(image)    
        #f.save("static/a.png")

        #import os
        #try:
         #   os.remove("static/a.png")
        #except:pass
        #f.save(secure_filename(f.filename))
        #print(len(f.stream.read() ))
        #decoded = cv2.imdecode(np.frombuffer(image_bytes, np.uint8), -1)
        #decoded = cv2.imdecode(np.frombuffer(f.stream.read() , np.uint8), -1)
        #f.save(secure_filename(os.path.join(app.config['UPLOAD_FOLDER'],f.filename))
       # print('OpenCV:\n', decoded)
        #print(image.shape)
      #
     
    return render_template('predict.html',positive=positive,negative=negative,user_image="static/a.jpg")
    
    
if __name__=='__main__':
    app.run(debug=True, use_reloader=True)
