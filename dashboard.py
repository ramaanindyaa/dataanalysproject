import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from babel.numbers import format_currency

# Memuat data yang sudah dibersihkan
day_df = pd.read_csv('day_cleaned.csv')
hour_df = pd.read_csv('hour_cleaned.csv')


# Menampilkan beberapa baris pertama dari dataset untuk memastikan data dimuat dengan benar
st.write("Day Data:")
st.write(day_df.head())

st.write("Hour Data:")
st.write(hour_df.head())

# Menyiapkan filter berdasarkan tanggal
min_date = day_df["dteday"].min()  
max_date = day_df["dteday"].max()

with st.sidebar:
    st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png")
    start_date, end_date = st.date_input(
        label='Rentang Waktu', min_value=min_date, max_value=max_date,
        value=[min_date, max_date]
    )

# Filter data berdasarkan tanggal yang dipilih
main_df = day_df[(day_df["dteday"] >= str(start_date)) & (day_df["dteday"] <= str(end_date))]

# Fungsi untuk menyiapkan data berdasarkan musim
def create_season_df(df):
    season_df = df.groupby('season')['cnt'].mean().reset_index()
    return season_df

# Fungsi untuk menyiapkan data berdasarkan hari kerja vs libur
def create_workingday_df(df):
    workingday_df = df.groupby('workingday')['cnt'].mean().reset_index()
    return workingday_df

# Fungsi untuk menyiapkan data berdasarkan suhu
def create_temperature_df(df):
    temp_df = df[['temp', 'cnt']].groupby('temp').mean().reset_index()
    return temp_df

# Fungsi untuk menyiapkan data berdasarkan hari dalam seminggu
def create_weekday_df(df):
    weekday_df = df.groupby('weekday')['cnt'].mean().reset_index()
    return weekday_df

# Fungsi untuk menyiapkan data berdasarkan kondisi cuaca
def create_weather_df(df):
    weather_df = df.groupby('weathersit')['cnt'].mean().reset_index()
    return weather_df

st.subheader('Pengaruh Musim terhadap Jumlah Sewa Sepeda')

season_df = create_season_df(main_df)
fig, ax = plt.subplots(figsize=(8, 6))
sns.barplot(x='season', y='cnt', data=season_df, palette='viridis', ax=ax)
ax.set_xlabel('Musim')
ax.set_ylabel('Jumlah Sewa Sepeda')
ax.set_title('Pengaruh Musim terhadap Jumlah Sewa Sepeda')

st.pyplot(fig)

st.subheader('Pengaruh Hari Kerja vs Hari Libur terhadap Jumlah Sewa Sepeda')

workingday_df = create_workingday_df(main_df)
fig, ax = plt.subplots(figsize=(8, 6))
sns.barplot(x='workingday', y='cnt', data=workingday_df, palette='Blues', ax=ax)
ax.set_xlabel('Hari Kerja (1 = Ya, 0 = Tidak)')
ax.set_ylabel('Jumlah Sewa Sepeda')
ax.set_title('Pengaruh Hari Kerja vs Hari Libur terhadap Jumlah Sewa Sepeda')

st.pyplot(fig)

st.subheader('Pengaruh Suhu terhadap Jumlah Sewa Sepeda')

temp_df = create_temperature_df(main_df)
fig, ax = plt.subplots(figsize=(8, 6))
sns.scatterplot(x='temp', y='cnt', data=temp_df, color='orange', ax=ax)
ax.set_xlabel('Suhu (Normalisasi)')
ax.set_ylabel('Jumlah Sewa Sepeda')
ax.set_title('Pengaruh Suhu terhadap Jumlah Sewa Sepeda')

st.pyplot(fig)

st.subheader('Pengaruh Hari dalam Seminggu terhadap Jumlah Sewa Sepeda')

weekday_df = create_weekday_df(main_df)
fig, ax = plt.subplots(figsize=(8, 6))
sns.barplot(x='weekday', y='cnt', data=weekday_df, palette='Pastel1', ax=ax)
ax.set_xlabel('Hari dalam Seminggu')
ax.set_ylabel('Jumlah Sewa Sepeda')
ax.set_title('Pengaruh Hari dalam Seminggu terhadap Jumlah Sewa Sepeda')

st.pyplot(fig)

st.subheader('Pengaruh Kondisi Cuaca terhadap Jumlah Sewa Sepeda')

weather_df = create_weather_df(main_df)
fig, ax = plt.subplots(figsize=(8, 6))
sns.barplot(x='weathersit', y='cnt', data=weather_df, palette='coolwarm', ax=ax)
ax.set_xlabel('Kondisi Cuaca')
ax.set_ylabel('Jumlah Sewa Sepeda')
ax.set_title('Pengaruh Kondisi Cuaca terhadap Jumlah Sewa Sepeda')

st.pyplot(fig)
