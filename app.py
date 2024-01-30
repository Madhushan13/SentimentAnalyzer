from flask import Flask, render_template, request, redirect
from My_helper import preprocessing, vectorizer, get_prediction
from logger import logging
app = Flask(__name__)

logging.info("Flask server start" )
data = dict()
reviews = []
positive = 0
negative = 0

@app.route("/")
def index():
    data["reviews"] = reviews
    data["positive"] = positive
    data["negative"] = negative
    logging.info("Open Home page" )
    return render_template("index.html", data=data)

@app.route("/", methods = ['post'])
def my_post():
    global positive, negative 

    text = request.form['text']
    logging.info(f'Text : {text}')
    preprocessed_txt = preprocessing(text)
    logging.info(f'preprocessed Text : {preprocessed_txt}' )
    vectorized_txt = vectorizer(preprocessed_txt)
    logging.info(f'vectorized Text : {vectorized_txt}' )
    prediction = get_prediction(vectorized_txt)
    logging.info(f'prediction : {prediction}')

    if prediction == 'negative':
        negative += 1
    else:
        positive += 1
    
    reviews.insert(0, text)
    return redirect(request.url)

if __name__ == "__main__":
    app.run()