import pyshorteners
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Initialize a dictionary to store the mappings between short URLs and original URLs
url_mappings = {}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/shorten', methods=['POST'])
def shorten_url():
    original_url = request.form['original_url']
    s = pyshorteners.Shortener()
    short_url = s.tinyurl.short(original_url)
    url_mappings[short_url] = original_url
    return render_template('shortened.html', original_url=original_url, short_url=short_url)


@app.route('/<string:short_url>')
def redirect_to_original(short_url):
    if short_url in url_mappings:
        original_url = url_mappings[short_url]
        return redirect(original_url)
    else:
        return "Short URL not found."


if __name__ == '__main__':
    app.run()
