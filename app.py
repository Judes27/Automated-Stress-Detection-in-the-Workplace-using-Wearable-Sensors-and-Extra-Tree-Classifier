from flask import Flask,render_template,Markup
import requests
import json
from keras.models import load_model
from mod import *


model=load_model("model.h5")
print("Hi")

app = Flask(__name__)

Depr={'Sad': """Think Your Happiness in Your life""",
    'Happy':"""Enjoy the life""",
    'Neutral':"""Be Cool""" ,
    'Depression':"""calm yourself"""

}


@app.route("/")
def Dep():
     
     return render_template("home.html")
    



@app.route('/new')
def app1():
    depre=[]
    while True:
        response = requests.get('https://iotcloud22.in/2209_depression/light.json')
        # https://iotcloud22.in/2209_depression/light.json
        if response.status_code == 200:
            # print(response.json())

            data = json.loads(response.text)

        
            value1 = data['temperature']
            value2 = data['heart']
            value3 = data['gsr']

            value2=int(value2)
            value2=value2/6
            
            print(value1, value2, value3)

            v2=float(value2)

            a = predict(v2)
                
            # print("Temp :",value1+" "+"Heart :",v2+" "+"GSR :",value3)
            v2=str(v2)
            depre.append(a)
            depre=depre[-1]
            print("Depression Status : ",depre)
            prediction = Markup(str(Depr[depre]))
            print(prediction)
            return render_template("index.html",Temp=value1,Heart=v2,Gsr=value3,Dep=a,pred=prediction)
        continue
    # else:
    #     print('Error: {}'.format(response.status_code))




if __name__ == "__main__":
    app.run(debug=True)
