import streamlit as st
import pandas as pd
import os

def load_item_data():
    # Periksa apakah file CSV data_barang.csv sudah ada
    if os.path.isfile("data_barang.csv"):
        return pd.read_csv("data_barang.csv")
    else:
        return pd.DataFrame(columns=["nama_barang", "qty"])

def update_item_data(nama_barang, qty):
    df = load_item_data()
    df.loc[df['nama_barang'] == nama_barang, 'qty'] = qty
    df.to_csv("data_barang.csv", index=False)

def show_update_item_page():
    st.title("Update Item Furniture")

    # Load data from data_barang.csv
    df = load_item_data()

    with st.form(key='update_form'):
        nama_barang = st.selectbox('Select Item to Update', df['nama_barang'].unique())
        
        # Get the current quantity of the selected item
        current_qty = df.loc[df['nama_barang'] == nama_barang, 'qty'].values[0] if not df.empty and nama_barang in df['nama_barang'].values else 1

        qty = st.number_input('New Quantity', min_value=1, step=1, value=int(current_qty))
        submit_button = st.form_submit_button(label='Update')

    if submit_button:
        update_item_data(nama_barang, qty)
        st.success('Data has been updated successfully!')
        st.write(f"Updated {nama_barang} to quantity {qty}")
