# 🧠 Sentiment Analysis on Manchester United’s Defeat Against ASEAN All Stars

This is a collaborative NLP project that analyzes public sentiment in response to Manchester United's unexpected loss to the ASEAN All Stars. The project involves data collection, manual data cleaning, exploratory data analysis (EDA), sentiment labeling, and future model development.

---

## 🚀 Project Overview

- **Sentiment Collection**: Gather public reactions from multiple online platforms regarding the match.
- **Sentiment Modeling (Next Phase)**:
  - Build a sentiment classification model to categorize comments into:
    - **Positive (Supporters)**
    - **Negative (Haters)**
    - **Neutral (Observers)**
  - Deploy the trained model via an interactive web application.

---

## 👥 Team Collaboration Roles

- **Rayhan Ananda Resky**: Data collection, data preprocessing, modeling
- **Team Member 1**: Model evaluation, deployment
- **Team Member 2**: Deployment environment preparation (HTML, CSS, JS frontend)

---

## 📊 Data Collection Summary

### ✅ News Articles
- 5 news articles were manually scraped due to dynamic HTML structures.

### ✅ News Comments
- Only 2 out of 5 news portals contained comment sections.
- All comments were manually copied.

### ✅ YouTube Comments (via Google API)
| Video ID    | Actual Comments | Comments Retrieved |
|-------------|------------------|---------------------|
| hFIMNthZ6ow | 445              | 404                 |
| 8p-pFSN17n0 | 9                | 9                   |
| NYS5HSUVdz8 | 8971             | 1000 (API limit)    |

### ✅ TikTok Comments (using [cubernetes](https://github.com/cubernetes/TikTokCommentScraper))
| Video Link | Actual Comments | Comments Retrieved |
|------------|------------------|---------------------|
| VT1 | 4483 | 3381 |
| VT2 | 2280 | 1725 |
| VT3 | 919  | 510  |

---

## 🧹 Data Cleaning & Preprocessing

- ✅ Raw data consolidation from multiple formats (.csv, .xlsx)
- ✅ Unicode normalization
- ✅ Emoji and non-alphabetic character removal
- ✅ Basic noise removal
- ✅ Language filtering (Indonesian)
- ✅ Manual cleaning for sensitive content (e.g. gambling-related comments)
- ✅ Final dataset ready for manual labeling

---

## 🏷️ Manual Sentiment Labeling

- All comments were labeled manually due to sarcasm, humor, and subtle context not well captured by automated methods.
- Cleaned and labeled dataset: `all_comments_for_labeling_cleaned.csv`
- Label categories:
  - `positive`
  - `negative`
  - `neutral`

---

## 📊 Exploratory Data Analysis (EDA Summary)

- **Total comments**: 1867
- **Platform distribution**:
  - TikTok: 1502
  - YouTube: 340
  - News: 25

- **Average word count per platform**:
  - TikTok: 6.94 words
  - YouTube: 9.91 words
  - News: 10.36 words

- **Maximum word count per platform**:
  - TikTok: 37 words
  - YouTube: 100 words
  - News: 35 words

- **Insights:**
  - TikTok dominates the dataset with very short comments.
  - YouTube has longer, more detailed comments.
  - Manual cleaning has successfully removed irrelevant or sensitive content.
  - Dataset fully cleaned and ready for modeling.

---

## 📂 Project Structure (Updated)

```bash
project_root/
│
├── Data/
│   ├── Raw/
│   │   ├── raw_data.csv
│   │   ├── raw_comment_data.csv
│   │   ├── youtube_comments.csv
│   │   ├── tiktok_comments_raw_*.csv / .xlsx
│   └── Cleaned/
│       ├── news_comments_clean.csv
│       ├── youtube_comments_clean.csv
│       ├── tiktok_comments_clean.csv
│       └── all_comments_for_labeling_cleaned.csv
│
├── Models/
│   └── lid.176.bin
│
├── Notebook/
│   ├── 01_scraping_experiment.ipynb
│   ├── 02_scraping_youtube_comment.ipynb
│   ├── 03_data_preprocessing.ipynb
│   ├── 04_data_merging.ipynb
│   └── 05_exploratory_data_analysis.ipynb
│
└── README.md

```
---

## ⚙️ Tech Stack

- `pandas` – Data manipulation  
- `requests`, `BeautifulSoup` – Web scraping (news sites)  
- `google-api-python-client` – YouTube comment API  
- `cubernetes` – TikTok comment scraper  
- `openpyxl` – Spreadsheet formatting  
- `Matplotlib`, `seaborn`, `wordcloud` - Visualization
---

## 🚀 Next Steps

- Text preprocessing (tokenization, stopwords removal, stemming/lemmatization)
- Model training (Logistic Regression, Naive Bayes, SVM, etc.)
- Deployment via web app

---

## 👤 Author

**Rayhan Ananda Resky**  
[LinkedIn](https://www.linkedin.com/in/rayhanananda/) | [GitHub](https://github.com/RayhanLup1n)
```
