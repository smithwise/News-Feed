'''below is a basic Flask app from ChatGPT to get started, copy paste as needed. 
-=-=-=- START APP -=-=-=-
from flask import Flask, render_template
import feedparser

app = Flask(__name__)

RSS_FEEDS = {
    "security": "https://feeds.feedburner.com/TheHackersNews",
    "tech": "https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml"
}

@app.route("/")
def home():
    return "<h1>Welcome to My RSS Feed Aggregator</h1><p>Use /feed/security or /feed/tech</p>"

@app.route("/feed/<category>")
def get_feed(category):
    feed_url = RSS_FEEDS.get(category, None)
    if not feed_url:
        return "<h1>Category Not Found</h1>", 404

    feed = feedparser.parse(feed_url)
    return render_template("feed.html", feed=feed)

if __name__ == "__main__":
    app.run(debug=True)

-=-=-=- END APP -=-=-=-
'''
