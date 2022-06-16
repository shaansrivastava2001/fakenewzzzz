from flask import Flask, escape, request, render_template
import pickle


vector = pickle.load(open("vectorizer.pkl" , 'rb'))
LR = pickle.load(open("finalized__model.pkl", 'rb'))
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/prediction', methods=['GET', 'POST'])
def prediction():
    if request.method == "POST":
        news = request.form['news']
        print(news)
        predict = str(LR.predict(vector.transform([news]))[0])
        print(predict,type(predict))
        if predict == '1.0':
            predict = 'REAL'
        
        else:
            predict = 'FAKE'
        

        return render_template("prediction.html", prediction_text="News Headline is : {}".format(predict))
    
    
    else:
        return render_template("prediction.html")
    


if __name__ == '__main__':
    app.run()