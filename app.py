from flask import Flask, render_template, request
import pickle
import numpy as np

# setup application
app = Flask(__name__)

def prediction(lst):
  filename = 'model/predictor.pickle'
  with open(filename,'rb') as file:
    model = pickle.load(file)
  pred = model.predict([lst])
  return pred
  
@app.route('/',methods=['POST','GET'])
def index():
    pred = 0
    if request.method == 'POST':
       ratings = request.form['Ratings']
       ram = request.form['RAM']
       rom = request.form['ROM']
       mobile_size = request.form['Mobile_Size']
       primary_cam = request.form['Primary_Cam']
       selfie_cam = request.form['Selfi_Cam']
       battery_power = request.form['Battery_Power']
       brand = request.form['brand']
       

       feature_list = []

       feature_list.append(float(ratings))
       feature_list.append(float(ram))
       feature_list.append(float(rom))
       feature_list.append(float(mobile_size))
       feature_list.append(float(primary_cam))
       feature_list.append(float(selfie_cam))
       feature_list.append(float(battery_power))
       

       brand_list=['Apple IPhone 11','Apple iPhone 12','Nokia  216','Nokia  415','Oppo  A17','Oppo  A9','Redmi A9','Redmi K20','Samsung  Galaxy A50','Samsung Galaxy','Vivo  V21','Vivo  Y81']
    
       def traverse(lst,value):
         for item in lst:
          if item == value:
           feature_list.append(1)
          else:
           feature_list.append(0)


       traverse(brand_list,brand)

    
       pred = prediction(feature_list)
       pred = np.round(pred[0],2)


    return render_template("index.html", pred = pred)


if __name__ =='__main__':
     app.run(debug=True)