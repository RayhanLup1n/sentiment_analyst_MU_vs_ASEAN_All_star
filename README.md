# 🧠 Sentiment Analysis on Manchester United’s Defeat Against ASEAN All Stars

This is a personal NLP project that analyzes public sentiment in response to Manchester United's unexpected loss to the ASEAN All Stars. The current stage focuses on **data collection**, while modeling and deployment will be completed in later phases.

---

## 🚀 Project Goals

- **Sentiment Collection**: Gather public reactions from multiple online platforms regarding the match.
- **Future Modeling Plan**:
  - Develop a sentiment classification model to categorize users as:
    - **Supporters** (positive sentiment)
    - **Haters** (negative sentiment)
    - **Neutral** (objective/no sentiment)
  - Deploy the model via a Streamlit app.

---

## 📊 Data Collection Summary

### ✅ News Articles
- **5** news articles were manually scraped due to dynamic and inconsistent HTML structures that made automatic scraping unreliable.

### ✅ News Comments
- Only **2** out of 5 news portals contained comment sections.
- All comments were manually copied since automated scraping was not feasible.

### ✅ YouTube Comments (using Google API)
Comments were retrieved via the official YouTube Data API.

| Video ID        | Actual Comments | Comments Retrieved |
|----------------|------------------|---------------------|
| hFIMNthZ6ow     | 445              | 404                 |
| 8p-pFSN17n0     | 9                | 9                   |
| NYS5HSUVdz8     | 8971             | 1000 (API limited)  |

### ✅ TikTok Comments (using [cubernetes](https://github.com/cubernetes/TikTokCommentScraper))
Comments were retrieved using the Cubernetes browser-based TikTok scraper.

| Video Link                                                                                 | Actual Comments | Comments Retrieved |
|-------------------------------------------------------------------------------------------|------------------|---------------------|
| https://www.tiktok.com/@kylectrix/video/7509509579127000328 (VT1)                         | 4483             | 3381                |
| https://www.tiktok.com/@nayeemutd1/video/7509507904832048406 (VT2)                        | 2280             | 1725                |
| https://www.tiktok.com/@kylectrix/video/7509828777682455816 (VT3)                         | 919              | 510                 |

---

## 🧱 Project Structure

```plaintext
project_root/
│
├── data/
│   └── raw/                         # All collected raw data
│       ├── raw_data.csv
│       ├── raw_data.xlsx
│       ├── raw_comment_data.csv
│       ├── raw_comment_data.xlsx
│       ├── youtube_comments.csv
│       ├── tiktok_comments_raw_1.xlsx
│       ├── tiktok_comments_raw_2.xlsx
│       └── tiktok_comments_raw_3.xlsx
│
├── notebook/
│
│
├── notebook_dev/
│   └── 01_scraping_experiment.ipynb
│   └── 02_scraping_youtube_comment.ipynb
│
└── README.md
```

---

## ⚙️ Tech Stack

- `pandas` – Data manipulation  
- `requests`, `BeautifulSoup` – Web scraping (news sites)  
- `google-api-python-client` – YouTube comment API  
- `cubernetes` – TikTok comment scraper  
- `openpyxl`, `xlsxwriter` – Spreadsheet formatting  

---

## 🧪 Next Steps

- Clean and preprocess all collected comments  
- Apply rule-based or clustering methods for semi-supervised labeling  
- Train classification models (e.g., Logistic Regression, Naive Bayes)  
- Deploy model as an interactive Streamlit app  

---

## 👤 Author

**Rayhan Ananda Resky**  
[LinkedIn](https://www.linkedin.com/in/rayhanananda/) | [GitHub](https://github.com/RayhanLup1n)
