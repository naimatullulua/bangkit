import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Load your datasets
all_data = pd.read_csv("d:/KULIAH/SEMESTER VII/BANGKIT 2024/submission/dashboard/transaction_merged.csv")

st.header("E-Commerce Dashboard")

with st.sidebar:
    st.title("Na'imatul Lu'lu'a")

page = st.sidebar.radio("Pilih Halaman:", ["Home", "Pertanyaan 1", "Pertanyaan 2", "Pertanyaan 3"])

if page == "Home":
    st.write("Selamat datang di dashboard analisis data E-Commerce!")
    st.write("Di sini, Anda dapat mengeksplorasi dua pertanyaan bisnis yang telah ditentukan.")

elif page == "Pertanyaan 1":
    st.subheader("Freight Value VS Price")
    
    # Pertanyaan 1
    plt.figure(figsize=(10, 8))
    sns.scatterplot(x='price', y='freight_value', data=all_data)
    plt.title('Hubungan antara Freight Value dan Price')
    plt.xlabel('Price')
    plt.ylabel('Freight Value')
    
    # Show plot in Streamlit
    st.pyplot(plt)
    plt.clf()  # Clear the figure

elif page == "Pertanyaan 2":
    st.subheader("Jumlah Transaksi Berdasarkan Rating")
    
    # Hitung jumlah transaksi per rating
    transactions_per_rating = all_data.groupby('review_score')['order_id'].count()

    # Visualisasikan dengan bar chart
    plt.figure(figsize=(8, 6))
    sns.barplot(x=transactions_per_rating.index, y=transactions_per_rating.values)
    plt.title('Jumlah Transaksi per Rating')
    plt.xlabel('Rating')
    plt.ylabel('Jumlah Transaksi')
    
    # Show bar plot in Streamlit
    st.pyplot(plt)
    plt.clf()  # Clear the figure

elif page == "Pertanyaan 3":
    st.subheader("Jumlah Pesanan Berdasarkan Kota")

    order_per_kota = all_data.groupby('seller_city')['order_id'].count().sort_values(ascending=False).head(10)

    plt.figure(figsize=(12, 8))
    sns.barplot(x=order_per_kota.index, y=order_per_kota.values)
    plt.title('Jumlah Order per Kota (Top 10)')
    plt.xlabel('Kota')
    plt.ylabel('Jumlah Order')
    plt.xticks(rotation=90)
    
    # Show bar plot in Streamlit
    st.pyplot(plt)
    plt.clf()  # Clear the figure

