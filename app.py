import streamlit as st
import pickle
import re
import string
import pandas as pd

import numpy as np


# Load Dataset
df = pd.read_csv('all_comments_for_labeling_cleaned.csv', delimiter=';')

# Load model dan vectorizer
with open('final_model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('tfidf_vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

with open('stopwords_id.pkl', 'rb') as f:
    stop_words = pickle.load(f)

# Stopwords dan fungsi preprocessing
from nltk.corpus import stopwords
from nltk import download
download('stopwords')
stop_words = set(stopwords.words('indonesian'))

def clean_text(text):
    text = text.lower()
    text = re.sub(r"http\S+|www.\S+", "", text)
    text = re.sub(r"@\w+|#\w+", "", text)
    text = re.sub(r"\d+", "", text)
    text = re.sub(rf"[{string.punctuation}]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

def remove_stopwords(text):
    tokens = text.split()
    filtered = [word for word in tokens if word not in stop_words]
    return " ".join(filtered)

def preprocess_input(text):
    cleaned = clean_text(text)
    filtered = remove_stopwords(cleaned)
    return filtered

# Streamlit UI
st.markdown(
    "<style>body { background-color: #1c1c1c; color: white; } .stButton>button { color: red; }</style>",
    unsafe_allow_html=True
)

st.title("MU Opinion Sentiment Analysis")
st.markdown('___')

st.sidebar.image('mu_vs_asean.png')
st.sidebar.markdown("### 📊 Dataset Info")
st.sidebar.write(f"Total Komentar: {len(df)}")
st.sidebar.write(df['label'].value_counts())
st.sidebar.markdown('---')

st.markdown("### 😱 Menggemparkan !!!, Kekalahan Mengejutkan MU dari ASEAN All Stars")
st.image("MU.png", caption="Skor Akhir: ASEAN All Stars 1 - 0 Manchester United", use_container_width=True)
st.markdown('---')


# Subtitle baru
st.markdown("## Bagaimana tanggapan anda? Tolong berikan pendapat anda mengenai berita tersebut.")


st.markdown("### 💬 Contoh Opini Warganet")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("##### 😠 Negatif")
    st.info("MU itu overrated banget")

with col2:
    st.markdown("##### 😐 Netral")
    st.info('Yang Golin siapa?')

with col3:
    st.markdown("##### ❤️ Positif")
    st.info("Tetep bangga dukung MU, sampai mati 🔴")

user_input = st.text_area("Tulis opini Anda di sini:")

if st.button("Prediksi"):
    if user_input.strip() == "":
        st.warning("Bagaimana menurut anda?")
    else:
        processed = preprocess_input(user_input)
        vectorized = vectorizer.transform([processed])
        prediction = model.predict(vectorized)[0]
        
        label_map = {
            "positive": "👍 Positif (Ternyata anda adalah Fans MU ya, ✌️)",
            "negative": "👎 Negatif (Nice bang, ngapain dukung MU ye kan ✌️)",
            "neutral": "😐 Netral (Fans Bola sejati nih keknya)"
        }
        
        st.subheader("Kategori Sentimen:")
        st.success(label_map.get(prediction, prediction))

uploaded_file = st.sidebar.file_uploader("Opininya kepanjangan? Upload aja CSV-nya", type="csv")

if uploaded_file:
    import pandas as pd
    df_uploaded = pd.read_csv(uploaded_file)
    df_uploaded['preprocessed'] = df_uploaded['text'].apply(preprocess_input)
    df_uploaded['sentiment'] = model.predict(vectorizer.transform(df_uploaded['preprocessed']))
    st.markdown("### Hasil Prediksi CSV")
    st.dataframe(df_uploaded[['text', 'sentiment']])

st.markdown("---")
st.markdown("Built by Rayhan Ananda Resky 🚀 | Follow me on [LinkedIn](https://www.linkedin.com/) | ✨ Project open source on [GitHub](https://github.com/)")