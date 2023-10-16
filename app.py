from flask import Flask, render_template, request
import pickle
import numpy as np

# setup application
app = Flask(__name__)

def prediction(lst):
    filename = 'model/predictor.pickle'
    with open(filename, 'rb') as file:
        model = pickle.load(file)
    pred_value = model.predict([lst])
    return pred_value

@app.route('/', methods=['POST', 'GET'])
def index():
    # return "Hello World"
    pred_value = 0
    if request.method == 'POST':
        ram = request.form['ram']
        rom = request.form['rom']
        rating = request.form['rating']
        batterypower = request.form['batterypower']
        mobilesize = request.form['mobilesize']
        primarycam = request.form['primarycam']
        selficam = request.form['selficam']
        brandname = request.form['brandname']

        mobilesize_list = ['3.4','3.7','5.8','6.0','6.1','6.2','6.3','6.4','6.5']
        primarycam_list = ['12','16','36','48','64']
        selficam_list = ['8','12','24','32','84']
        brandname_list = ['apple','nokia','oppo','redmi','samsung','vivo']



 
        
        feature_list = []
        
        feature_list.append(float(rating))
        feature_list.append(int(ram))
        feature_list.append(int(rom))
        


        def traverse_list1(lst, value):
            for item in lst:
                if item == value:
                    feature_list.append(float(item))

        traverse_list1(mobilesize_list,mobilesize)
        
      
        feature_list.append(int(batterypower))

        traverse_list1(primarycam_list,primarycam)
        traverse_list1(selficam_list,selficam)
      
        # for item in company_list:
        #     if item == company:
        #         feature_list.append(1)
        #     else:
        #         feature_list.append(0)

        def traverse_list(lst, value):
            for item in lst:
                if item == value:
                    feature_list.append(1)
                else:
                    feature_list.append(0)
        
        traverse_list(brandname_list, brandname)

        

    
        print(feature_list)

        pred_value = prediction(feature_list)
        pred_value = np.round(pred_value[0],2)

    return render_template('index.html', pred_value=pred_value)


if __name__ == '__main__':
    app.run(debug=True)