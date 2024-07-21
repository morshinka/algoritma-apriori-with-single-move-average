import streamlit as st
import pandas as pd
import os
from st_aggrid import AgGrid, GridOptionsBuilder

def load_furniture_items():
    # Periksa apakah file CSV modified_file_jan_to_jun.csv sudah ada
    if os.path.isfile("modified_file_jan_to_jun.csv"):
        df = pd.read_csv("modified_file_jan_to_jun.csv")
        return df['Item'].unique()
    else:
        st.error("File 'modified_file_jan_to_jun.csv' not found.")
        return []

def append_item_data(data):
    # Periksa apakah file CSV data_barang.csv sudah ada, jika tidak buat file kosong
    if not os.path.isfile("data_barang.csv"):
        df = pd.DataFrame(columns=["nama_barang", "qty"])
        df.to_csv("data_barang.csv", index=False)
    else:
        df = pd.read_csv("data_barang.csv")
    
    df = pd.concat([df, data], ignore_index=True)
    df.to_csv("data_barang.csv", index=False)

def show_adding_item_furniture_page():
    st.title("Adding Item Furniture")

    # Load nama_barang dari file modified_file_jan_to_jun.csv
    items = load_furniture_items()

    with st.form(key='item_form'):
        nama_barang = st.selectbox('Nama Barang', items)
        qty = st.number_input('Quantity', min_value=1, step=1)
        submit_button = st.form_submit_button(label='Submit')

    if submit_button:
        new_data = {
            "nama_barang": [nama_barang],
            "qty": [qty]
        }
        new_data_df = pd.DataFrame(new_data)
        append_item_data(new_data_df)
        st.success('Data has been added successfully!')
        st.write(new_data_df)
