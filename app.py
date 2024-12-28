from flask import Flask, render_template, request, jsonify
from parallel import crawl_websites  # your parallel function
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
    # Read the top-level param: Are we using CSV or custom?
    url_mode = request.form.get('url_mode', '').strip()  # "csv" or "custom"

    depth = int(request.form.get('depth', 1))
    max_sublinks = int(request.form.get('max_sublinks', 20))
    num_processes = int(request.form.get('num_processes', 4))

    list_of_urls = []

    # If user picks "custom", just read from textarea
    if url_mode == 'custom':
        custom_urls_text = request.form.get('custom_urls', '').strip()
        list_of_urls = [u.strip() for u in custom_urls_text.splitlines() if u.strip()]

    # Otherwise, user wants CSV
    elif url_mode == 'csv':
        # Now read the sub-choice: file_all or file_some
        url_source = request.form.get('url_source', '').strip()  # could be "file_all", "file_some"
        uploaded_file = request.files.get('file')

        if url_source == 'file_some':
            # The user picked some of the URLs (front-end pass them in "some_urls")
            some_urls = request.form.get('some_urls', '').strip()
            list_of_urls = [u.strip() for u in some_urls.splitlines() if u.strip()]

        elif url_source == 'file_all':
            # The user wants all URLs from CSV, so we read the file
            if not uploaded_file:
                return jsonify({'error': 'No CSV file uploaded'}), 400

            file_path = 'uploaded_file.csv'
            uploaded_file.save(file_path)

            df = pd.read_csv(file_path)
            if 'Website' not in df.columns:
                return jsonify({'error': 'CSV must have a "Website" column.'}), 400

            list_of_urls = df['Website'].dropna().astype(str).str.strip().tolist()

        else:
            # If sub-choice is missing or invalid
            return jsonify({
                'error': 'Please select either "Use all from CSV" or "Pick some from CSV".'
            }), 400

    else:
        # If url_mode is neither "csv" nor "custom", it's an error
        return jsonify({
            'error': 'Please select "Upload CSV File" or "Custom URLs" at the top.'
        }), 400

    # If no URLs found, return an error or empty result
    if not list_of_urls:
        return jsonify({
            'error': 'No URLs provided or selected.',
            'wordcloud_url': "",
            'scraped_urls': [],
            'not_scraped_urls': [],
            'top_keywords_labels': [],
            'top_keywords_counts': []
        })

    # --- Now we do the crawling via parallel.py ---
    results = crawl_websites(
        websites=list_of_urls,
        depth=depth,
        max_sublinks=max_sublinks,
        num_processes=num_processes
    )
    
    # Separate scraped vs not scraped
    scraped_urls = []
    not_scraped_urls = []
    for url, keywords_found in zip(list_of_urls, results):
        if keywords_found:
            scraped_urls.append(url)
        else:
            not_scraped_urls.append(url)

    # Flatten keywords
    keywords = [k.strip() for sublist in results for k in sublist]

    # Generate a word cloud
    wordcloud_url = ""
    if keywords:
        wc = WordCloud(width=800, height=400, background_color='white').generate(' '.join(keywords))
        img = io.BytesIO()
        wc.to_image().save(img, format='PNG')
        img.seek(0)
        wordcloud_url = base64.b64encode(img.getvalue()).decode()

    # Top Keywords
    top_keywords_labels = []
    top_keywords_counts = []
    if keywords:
        keyword_series = pd.Series(keywords)
        top_keywords = keyword_series.value_counts().head(10)
        top_keywords_labels = top_keywords.index.tolist()
        top_keywords_counts = top_keywords.values.tolist()

    return jsonify({
        'wordcloud_url': f"data:image/png;base64,{wordcloud_url}",
        'scraped_urls': scraped_urls,
        'not_scraped_urls': not_scraped_urls,
        'top_keywords_labels': top_keywords_labels,
        'top_keywords_counts': top_keywords_counts
    })

if __name__ == "__main__":
    app.run(debug=True)
