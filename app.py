from flask import Flask,render_template,request
import pickle
import numpy as np

model = pickle.load(open('model.pkl','rb'))

with open('model.pkl', 'rb') as file:
    model = pickle.load(file)


app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

@app.route('/')
def home():
    return render_template('index.html')  # Landing page for sentiment analysis

@app.route('/predict', methods=['POST'])
def predict_review():
    # Get the review text from the form
    MOVIE_REVIEW = request.form.get("MOVIE_REVIEW", "").strip()  # Match the form field's name

    # Handle missing input
    if not MOVIE_REVIEW:
        return render_template('index.html', result="Please enter a valid movie review.")

    try:
        # Prediction
        result = model.predict(np.array([MOVIE_REVIEW]))[0]  # Assuming model.predict returns an array
        if result == 1:
            result = "POSITIVE"
        else:
            result = "NEGATIVE"
    except Exception as e:
        result = f"Error during prediction: {e}"

    return render_template('index.html', result=result, review=MOVIE_REVIEW)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080)