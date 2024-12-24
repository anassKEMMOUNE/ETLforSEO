from flask import Flask, render_template, request, jsonify
from parallel import crawl_websites  # Import the function from parallel.py
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import io
import base64

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    file = request.files['file']
    depth = int(request.form.get('depth', 1))
    max_sublinks = int(request.form.get('max_sublinks', 20))
    num_processes = int(request.form.get('num_processes', 4))
    num_urls = int(request.form.get('num_urls', -1))  # Default to -1 for all URLs

    # Save the uploaded file to a temporary path
    file_path = 'uploaded_file.csv'
    file.save(file_path)

    # Call the crawl_websites function
    results = crawl_websites(
        file_path,
        depth=depth,
        max_sublinks=max_sublinks,
        num_processes=num_processes,
        num_urls=num_urls
    )

    # Separate URLs into scraped and not scraped
    scraped_urls = [url for url, data in zip(pd.read_csv(file_path)['Website'], results) if len(data) > 0]
    not_scraped_urls = [url for url, data in zip(pd.read_csv(file_path)['Website'], results) if len(data) == 0]

    # Flatten the list of lists of keywords
    keywords = [keyword.strip() for sublist in results for keyword in sublist]
 

    # Generate a word cloud
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(' '.join(keywords))

    # Save word cloud as an image
    img = io.BytesIO()
    wordcloud.to_image().save(img, format='PNG')
    img.seek(0)
    wordcloud_url = base64.b64encode(img.getvalue()).decode()

    # --- Additional Analytics: Top Keywords (Frequency) ---
    if keywords:
        keyword_series = pd.Series(keywords)
        top_keywords = keyword_series.value_counts().head(10)  # Top 10
        top_keywords_labels = top_keywords.index.tolist()
        top_keywords_counts = top_keywords.values.tolist()
    else:
        top_keywords_labels = []
        top_keywords_counts = []

    return jsonify({
        'wordcloud_url': f"data:image/png;base64,{wordcloud_url}",
        'scraped_urls': scraped_urls,
        'not_scraped_urls': not_scraped_urls,
        'top_keywords_labels': top_keywords_labels,
        'top_keywords_counts': top_keywords_counts
    })

if __name__ == "__main__":
    app.run(debug=True)
