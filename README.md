# 🧠 Sentiment Analysis on Manchester United’s Defeat Against ASEAN All Stars

This is a personal NLP project that analyzes public sentiment in response to the unexpected defeat of Manchester United against the ASEAN All Stars. It aims to classify online comments into **supportive**, **hateful**, or **neutral**, and deploy a working model for public interaction via **Streamlit**.

---

## 🚀 Project Goals

- **Portfolio Enhancement**: Showcase NLP and deployment skills in a real-world scenario.
- **Sentiment Detection**: Classify public opinions into 3 categories:
  - **Positive (Supporter)**: Comments supporting or defending Manchester United.
  - **Negative (Hater)**: Comments mocking or criticizing MU.
  - **Neutral (Observer)**: Comments that are objective or emotionless.
- **Public Interaction**: Let users input their opinion and see how the model classifies them.

---

## 📌 Project Features

- Scraping data from:
  - 5 online news articles
  - 3 YouTube videos (comment section)
  - 2 TikTok videos (comment section)
- Semi-unsupervised labeling using:
  - Keyword-based rules
  - Clustering (TF-IDF + KMeans)
- Classical machine learning model (e.g., Naive Bayes, Logistic Regression)
- Deployed via **Streamlit** with a form input system:
  - Users answer 3–5 football-related questions
  - Write a 1–2 paragraph comment about Manchester United
  - Model predicts sentiment type (Supporter / Hater / Neutral)

---

## 🧱 Project Structure

```plaintext
project-root/
│
├── data/                         # Raw and cleaned datasets
│   ├── raw/                      # Raw scraped data
│   └── processed/                # Cleaned and labeled data
│
├── notebooks/                    # Development and experimentation notebooks
│   ├── 01_scraping.ipynb         # Scraping news and comment data
│   ├── 02_preprocessing.ipynb    # Text normalization and cleaning
│   ├── 03_labeling.ipynb         # Rule-based and clustering sentiment labeling
│   ├── 04_modeling.ipynb         # Training and evaluation of ML models
│
├── app/                          # Streamlit deployment app
│   ├── streamlit_app.py          # Main Streamlit interface
│   └── model.pkl                 # Trained model for inference
│
├── README.md
└── requirements.txt              # Project dependencies
```

---

## 📈 Example Use Case (Streamlit)

Users will be asked to:
1. Answer several football-related questions.
2. Write a short opinion about Manchester United (1–2 paragraphs).
3. Click "Analyze Sentiment" to see if they are predicted as a **supporter**, **hater**, or **neutral** fan.

---

## ⚙️ Tech Stack

- **Python 3.10+**
- `BeautifulSoup`, `requests` – Web scraping
- `pandas`, `scikit-learn` – Data processing & ML
- `nltk`, `sastrawi` – NLP preprocessing (Bahasa Indonesia)
- `streamlit` – Model deployment
- `matplotlib`, `seaborn` – Data visualization

---

## 🧪 Future Improvements

- Add deep learning model using IndoBERTweet
- Improve labeling using semi-supervised learning
- Multilingual support (English + Indonesian)
- Live comment scraping via API (YouTube / TikTok)

---

## 📄 License

This project is open-source under the MIT License.

---

## 👤 Author

Rayhan Ananda Resky – [LinkedIn](https://www.linkedin.com/in/rayhanananda/) | [GitHub](https://github.com/RayhanLup1n)
