
from flask import Flask, render_template, request
import cv2
import numpy as np



from tensorflow.keras.models import load_model



def predict(image):
    
    image = np.array(cv2.resize(image, (224,224) ) ).reshape((1, 224, 224, 3)) /255.0
    return model.predict(image)[0]  

app = Flask(__name__)




@app.route('/', methods=['post', 'get'])
def homepage():
    

    return render_template('index.html', title = "Welcome", paragraph = 'Lorem ipsum dolor sit amet')

@app.route('/predict', methods = ['GET', 'POST'])
def upload_file():
    
    import cv2
    import numpy as np


    from tensorflow.keras.preprocessing.image import img_to_array
    from tensorflow.keras.models import load_model
    
    
    
  



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
     
    return render_template('predict.html', title = "hey Welcome", paragraph = 'Lorem ipsum dolor sit amet',positive=positive,negative=negative,user_image="static/a.jpg")


if __name__ == '__main__':
    app.run(debug=True)
