from flask import Flask , render_template , request
import pickle

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    product = request.form['product']
    reviews = reviews_data = [
    {"brand": "Apple", "product_name": "iPhone 14", "review_text": "Amazing camera and battery life!", "rating": 5},
    {"brand": "Apple", "product_name": "iPhone 14", "review_text": "Overpriced but works well.", "rating": 4},
    {"brand": "Apple", "product_name": "iPhone 14", "review_text": "Not worth the money.", "rating": 2},
    {"brand": "Apple", "product_name": "iPhone 14", "review_text": "Love the new features!", "rating": 5},
    {"brand": "Apple", "product_name": "iPhone 14", "review_text": "Battery drains too fast.", "rating": 2},
    {"brand": "Samsung", "product_name": "Galaxy S23", "review_text": "Excellent display and smooth performance.", "rating": 5},
    {"brand": "Samsung", "product_name": "Galaxy S23", "review_text": "Good phone but a bit expensive.", "rating": 4},
    {"brand": "Samsung", "product_name": "Galaxy S23", "review_text": "Average camera, nothing special.", "rating": 3},
    {"brand": "Samsung", "product_name": "Galaxy S23", "review_text": "Very satisfied with the purchase.", "rating": 5},
    {"brand": "Samsung", "product_name": "Galaxy S23", "review_text": "Stopped working after a month!", "rating": 1},
    {"brand": "OnePlus", "product_name": "OnePlus 11", "review_text": "Great value for money!", "rating": 5},
    {"brand": "OnePlus", "product_name": "OnePlus 11", "review_text": "Camera could be better.", "rating": 3},
    {"brand": "OnePlus", "product_name": "OnePlus 11", "review_text": "Performance is top-notch.", "rating": 5},
    {"brand": "OnePlus", "product_name": "OnePlus 11", "review_text": "Not impressed with the design.", "rating": 2},
    {"brand": "OnePlus", "product_name": "OnePlus 11", "review_text": "Amazing battery life.", "rating": 5},
]

    return render_template("result.html",product=product,reviews=reviews, sentiment="Neutral")

if __name__ == "__main__":
    app.run(debug=True)