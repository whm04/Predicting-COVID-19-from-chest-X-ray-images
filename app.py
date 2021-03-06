
from flask import Flask, render_template, request
import cv2
import numpy as np


import tensorflow
from tensorflow.keras.models import load_model



def predict(image):
    
    image = np.array(cv2.resize(image, (224,224) ) ).reshape((1, 224, 224, 3)) /255.0
    return model.predict(image)[0]  



app = Flask(__name__)


@app.route('/', methods=['post', 'get'])
def homepage():
    

    return render_template('index.html')

@app.route('/predict', methods = ['GET', 'POST'])
def upload_file():
    
 


    from tensorflow.keras.preprocessing.image import img_to_array
    from tensorflow.keras.models import load_model
    
    positive="20"
    negative = "20"
    
    if request.method == 'POST':
        
        f = request.files['file']
        
        image = cv2.imdecode(np.frombuffer(f.stream.read() , np.uint8), -1)
        

        cv2.imwrite("static/a.jpg",image)
        positive,negative=predict(image)    
        
     
    return render_template('predict.html', positive=positive,negative=negative,user_image="static/a.jpg")


if __name__ == '__main__':
    app.run(debug=True)
