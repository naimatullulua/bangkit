import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Load your datasets
order_items= pd.read_csv("./data/order_items_dataset.csv")
order_reviews= pd.read_csv("./data/order_reviews_dataset.csv")

st.header("E-Commerce Dashboard")

with st.sidebar:
    st.title("Na'imatul Lu'lu'a")

page = st.sidebar.radio("Pilih Halaman:", ["Home", "Pertanyaan 1", "Pertanyaan 2"])

if page == "Home":
    st.write("Selamat datang di dashboard analisis data E-Commerce!")
    st.write("Di sini, Anda dapat mengeksplorasi dua pertanyaan bisnis yang telah ditentukan.")

elif page == "Pertanyaan 1":
    st.subheader("Freight Value VS Price")
    
    # Pertanyaan 1
    plt.figure(figsize=(10, 8))
    sns.scatterplot(x='price', y='freight_value', data=order_items)
    plt.title('Hubungan antara Freight Value dan Price')
    plt.xlabel('Price')
    plt.ylabel('Freight Value')
    
    # Show plot in Streamlit
    st.pyplot(plt)
    plt.clf()  # Clear the figure

elif page == "Pertanyaan 2":
    st.subheader("Jumlah Transaksi Berdasarkan Rating")
    
    # Hitung jumlah transaksi per rating
    transactions_per_rating = order_reviews.groupby('review_score')['order_id'].count()

    # Visualisasikan dengan bar chart
    plt.figure(figsize=(8, 6))
    sns.barplot(x=transactions_per_rating.index, y=transactions_per_rating.values)
    plt.title('Jumlah Transaksi per Rating')
    plt.xlabel('Rating')
    plt.ylabel('Jumlah Transaksi')
    
    # Show bar plot in Streamlit
    st.pyplot(plt)
    plt.clf()  # Clear the figure


