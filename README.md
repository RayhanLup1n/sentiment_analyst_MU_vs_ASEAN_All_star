# ⚽ Sentiment Analysis on Manchester United’s Defeat Against ASEAN All Stars

This NLP project analyzes public sentiment surrounding Manchester United's unexpected defeat against the ASEAN All Stars. It includes data scraping, manual cleaning, exploratory analysis, sentiment classification, and a live web app for public interaction.

---

## 🚀 Project Highlights

- ✅ Collected over 1.800+ public comments from **news**, **YouTube**, and **TikTok**
- ✅ Cleaned, normalized, and labeled data manually to reduce sarcasm/noise bias
- ✅ Trained and evaluated multiple models (Logistic Regression, Naive Bayes, SVM)
- ✅ Final model deployed via [Streamlit App](https://your-streamlit-url-here)

---

## 🧠 Sentiment Classification

Comments are categorized into:
- **Positive** → MU Supporters
- **Negative** → Critics / Haters
- **Neutral** → Objective observers

Final model used:
> **Logistic Regression** with `class_weight='balanced'` trained on TF-IDF features.

---

## 🖥️ Try It Live

> **📌 [Click here to try the app →]([https://your-streamlit-url-here](https://mu-vs-asean-all-stars.streamlit.app/))**  
Enter your opinion and see how it’s classified!

---

## 📊 Data Collection Summary

| Source     | Method                     | Total Comments | Used |
|------------|----------------------------|----------------|------|
| News       | Manual scrape              | 5 articles     | 25   |
| YouTube    | YouTube API                | 3 videos       | 1400 |
| TikTok     | [cubernetes](https://github.com/cubernetes/TikTokCommentScraper) | 3 videos | 1500 |

---

## 🧹 Preprocessing Summary

- Text cleaning (lowercase, punctuation, emoji, number removal)
- Stopword removal (Indonesian)
- Labeling: `positive`, `negative`, `neutral`
- Final dataset: `all_comments_for_labeling_cleaned.csv`

---

## 🧪 Model Evaluation Snapshot

| Model                     | Accuracy | Macro F1 | Positive F1 |
|---------------------------|----------|----------|-------------|
| Logistic Regression       | 0.74     | 0.63     | 0.35–0.40   |
| Multinomial Naive Bayes   | 0.64     | 0.54     | 0.33        |
| Linear SVM                | 0.75     | 0.63     | 0.39        |
| PyCaret AutoML (ExtraTrees)| 0.72    | 0.71     | *N/A*       |

Final model chosen based on balance between precision, recall, and interpretability.

---

## 🧾 Project Files

```
project_root/
│
├── Data/
│   ├── Raw/
│       ├── raw_comment_data.csv
│       ├── raw_data.csv
│       ├── youtube_comments.csv
│       ├── tiktok_comments_raw_*.csv / .xlsx
│   ├── Cleaned/
│       ├── news_comments_clean.csv
│       ├── youtube_comments_clean.csv
│       ├── tiktok_comments_clean.csv
│   ├── all_comments_for_labeling_cleaned.csv
│   └── all_comments_for_labeling.csv
│
│
├── Notebook/
│   ├── 01_scraping_experiment.ipynb
│   ├── 02_scraping_youtube_comment.ipynb
│   ├── 03_data_preprocessing.ipynb
│   ├── 04_data_merging.ipynb
│   ├── 05_exploratory_data_analysis.ipynb
│   └── 06_data_modelling.ipynb
│
│
├── Notebook/
│   ├── all_comments_for_labeling_cleaned.csv
│   ├── app.py
│   ├── final_model.pkl
│   ├── mu_asean_all_stars.jpg
│   ├── mu_vs_asean.png
│   ├── MU.jpeg
│   ├── mu.png
│   ├── stopwords_id.pkl
│   └── tfidf_vectorizer.pkl
│
│
├── logs.log
├── requirements.txt
└── README.md
```


---

## ⚙️ Tech Stack

- `streamlit`, `scikit-learn`, `pandas`, `nltk`
- `google-api-python-client` for YouTube
- `cubernetes` for TikTok
- Visualization with `matplotlib`, `seaborn`, `wordcloud`

---

## 👤 Author

**Rayhan Ananda Resky**  
[LinkedIn](https://www.linkedin.com/in/rayhanananda/) | [GitHub](https://github.com/RayhanLup1n)

---

## 🙌 Acknowledgement

Thanks to netizen creativity and MU’s unexpected results that inspired this public sentiment project 😄
