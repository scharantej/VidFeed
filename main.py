 
# Import necessary libraries
from flask import Flask, render_template, request
import requests

# Create a Flask app
app = Flask(__name__)

# Define the main route
@app.route('/')
def index():
    # Fetch news articles related to YouTube from a news API
    news_api_url = 'https://newsapi.org/v2/everything?q=YouTube&apiKey=YOUR_API_KEY'
    response = requests.get(news_api_url)
    news_articles = response.json()['articles']

    # Render the index.html template and pass the news articles
    return render_template('index.html', news_articles=news_articles)

# Define the route to view a specific news article
@app.route('/article/<article_id>')
def article(article_id):
    # Fetch the specified news article from the news API
    news_api_url = 'https://newsapi.org/v2/everything?q=YouTube&apiKey=YOUR_API_KEY'
    response = requests.get(news_api_url)
    news_articles = response.json()['articles']

    # Find the news article with the specified ID
    article = next((article for article in news_articles if article['id'] == article_id), None)

    # Render the article.html template and pass the news article
    return render_template('article.html', article=article)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
