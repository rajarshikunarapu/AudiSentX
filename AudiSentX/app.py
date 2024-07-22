from flask import Flask, render_template, request, jsonify
from textblob import TextBlob

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/emoji', methods=['POST'])
def emoji():
    data = request.get_json()
    value = data['value']
    
    # Perform sentiment analysis
    analysis = TextBlob(value)
    sentiment = analysis.sentiment.polarity
    
    # Determine emoji based on sentiment
    if sentiment > 0.5:
        emoji = '😊'
    elif sentiment < -0.5:
        emoji = '😡'
    else:
        emoji = '😐'
    
    response = {
        'message': value,
        'emoji': emoji,
        'sentiment': sentiment,
        'analysis': analysis.sentiment
    }
    
    return jsonify(result=response)

if __name__ == '__main__':
    app.run(debug=True)
