
# ETL for SEO Watch by Anass Kemmoune


## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Clone the Repository](#clone-the-repository)
  - [Set Up Virtual Environment](#set-up-virtual-environment)
  - [Install Dependencies](#install-dependencies)
  - [Download NLTK Data](#download-nltk-data)
- [Usage](#usage)
  - [Running the Flask Application](#running-the-flask-application)
  - [Using the Web Interface](#using-the-web-interface)
- [Project Structure](#project-structure)
- [License](#license)
- [Contact](#contact)

## Introduction

**ETL for SEO Watch** is a comprehensive data pipeline and analysis tool designed for web scraping and SEO analytics. Leveraging Python's powerful libraries, this project enables users to scrape multiple websites, extract and clean textual data, perform keyword frequency analysis, generate visualizations like word clouds, and conduct advanced topic modeling. The user-friendly Flask-based web interface allows for easy configuration, execution, and visualization of scraping results.

## Features

- **Web Scraping:** Efficiently crawl and scrape multiple websites and their subpages up to a specified depth.
- **Parallel Processing:** Utilize multiprocessing to speed up the scraping process while respecting ethical scraping practices.
- **Data Cleaning:** Extract meaningful textual content by removing HTML tags, punctuation, and stopwords.
- **Keyword Analysis:** Generate frequency counts of keywords and visualize them using word clouds and bar charts.
- **Topic Modeling:** Implement Latent Dirichlet Allocation (LDA) to identify hidden topics within the scraped data.
- **Keyword Search:** Enable users to search for specific keywords within the scraped results, displaying relevant URLs and keyword counts.
- **Interactive Web Interface:** Modern and responsive UI built with Flask, featuring dynamic forms and real-time analytics.

## Installation

### Prerequisites

Ensure you have the following installed on your system:

- **Python 3.11**: [Download Python](https://www.python.org/downloads/)
- **Git**: [Download Git](https://git-scm.com/downloads)

### Clone the Repository

```bash
git clone https://github.com/yourusername/etl-for-seo-watch.git
cd etl-for-seo-watch
```

### Set Up Virtual Environment

It's recommended to use a virtual environment to manage project dependencies.

```bash
# Create a virtual environment named 'venv'
python3 -m venv venv

# Activate the virtual environment
# On Unix or MacOS
source venv/bin/activate

# On Windows
venv\Scripts\activate
```

### Install Dependencies

Ensure you have `pip` updated:

```bash
pip install --upgrade pip
```

Install all required Python packages using the provided `requirements.txt`:

```bash
pip install -r requirements.txt
```

### Download NLTK Data

The project utilizes NLTK for natural language processing tasks. Download the necessary datasets:

```bash
python download_ntlk.py
```




## Usage

### Running the Flask Application

Start the Flask server to launch the web interface.

```bash
python app.py
```



### Using the Web Interface

1. **Access the Dashboard:**
   Open your web browser and navigate to `http://localhost:5000` (or the port you've configured).

2. **Configure Scraping:**
   - **Source Selection:**
     - **Upload CSV File:** Provide a CSV with a `Website` column containing URLs to scrape.
     - **Custom URLs:** Enter URLs manually, one per line.
   - **CSV Sub-Choice (if CSV is selected):**
     - **Use All from CSV:** Scrape all listed URLs.
     - **Pick Some from CSV:** Select specific URLs from the uploaded CSV.
   - **Scraping Parameters:**
     - **Depth:** Define how deep the crawler should navigate from the root URLs.
     - **Max Sublinks:** Set the maximum number of sublinks to scrape per url.
     - **Number of Processes:** Determine how many parallel processes to use.

3. **Start Scraping:**
   Click the **Start Scraping** button. A loading spinner will indicate the scraping progress.

4. **View Results and Analytics:**
   Once scraping is complete:
   - **Scraped Websites:** List of successfully scraped URLs.
   - **Not Scraped Websites:** List of URLs that couldn't be scraped.
   - **Analytics:** Visualizations including pie charts, word clouds, bar charts for top keywords, and topic modeling results.
   - **Keyword Search:** Search for specific keywords within the scraped data to find relevant URLs and their keyword counts.

## Project Structure

```
ETLforSEO/
├── app.py
├── cleanHTML.py
├── parallel.py
├── webCrawler.py
├── requirements.txt
├── download_nltk.py
├── static/
│   ├── output.csv
├── utils/
│   ├── countUtils.py
├── templates/
│   └── index.html
├── README.md
├── .gitignore
└── report.pdf

```

- **app.py:** Main Flask application file.
- **cleanHTML.py:** Contains the cleaning functions.
- **parallel.py:** Contains the parallelism functions.
- **webCrawler.py:** Contains the web crawling functions.
- **requirements.txt:** Lists all Python dependencies.
- **download_nltk.py:** Script to download NLTK datasets.
- **static/:** Contains  the generated `output.csv`.
- **templates/:** HTML templates for the Flask app.
- **README.md:** Project documentation.
- **.gitignore:** Specifies files and directories to ignore in Git.
- **report.pdf** Contains the project report in PDF format.



## License

This project is licensed under the [MIT License](LICENSE).

## Contact

**Anass Kemmoune**

- **Email:** anass.kemmoune@um6p.ma
- **LinkedIn:** [linkedin.com/in/anass-kemmoune](https://https://www.linkedin.com/in/anass-kemmoune/)
- **GitHub:** [github.com/anassKEMMOUNE/ETLforSEO](https://github.com/anassKEMMOUNE/ETLforSEO)

Feel free to reach out for any questions, suggestions, or collaborations!

---

*Thank you for using ETL for SEO Watch! We hope this tool enhances your SEO analytics and web scraping endeavors.*
```