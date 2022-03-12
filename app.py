from flask import Flask, render_template, request,jsonify
from flask_cors import CORS,cross_origin
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle
from sklearn.metrics import  r2_score


app = Flask(__name__)   

@app.route('/',methods=['GET'])     
@cross_origin()
def homePage():
    return render_template("pages/form.html")

@app.route('/predict',methods=['POST','GET'])   
@cross_origin()
def index():
    if request.method == 'POST':
        try:
            #  reading the inputs given by the user
            gre_score=request.form['gre_score']
            toefl_score = request.form['toefl_score']
            university_rating = request.form['university_rating']
            sop = request.form['sop']
            lor = request.form['lor']
            cgpa = request.form['cgpa']
            is_research = request.form['research']
            filename = 'Admission_prediction.pkl'
            loaded_model = pickle.load(open(filename, 'rb'))    
            
            prediction=loaded_model.predict([[gre_score,toefl_score,university_rating,sop,lor,cgpa,is_research]])
            print('prediction is', prediction)
                
            return render_template('/pages/result.html',n=round(100*prediction[0]))
        except Exception as e:
            print('The Exception message is: ',e)
            return 'Something is wrong.Please try again after some time'
    else:
        return render_template('index.html')



if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8001, debug=True)
	#app.run(debug=True)