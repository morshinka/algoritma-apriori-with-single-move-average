import streamlit as st
import pandas as pd
import os
from st_aggrid import AgGrid, GridOptionsBuilder

def load_furniture_data():
    if not os.path.isfile("modified_file_jan_to_jun.csv"):
        df = pd.DataFrame(columns=["date_time", "Transaction", "Item", "Quantity"])
        df.to_csv("modified_file_jan_to_jun.csv", index=False)
    else:
        df = pd.read_csv("modified_file_jan_to_jun.csv")
    return df

def append_transaction_data(data):
    df = pd.read_csv("modified_file_jan_to_jun.csv")
    df = pd.concat([df, data], ignore_index=True)
    df.to_csv("modified_file_jan_to_jun.csv", index=False)

def get_next_transaction_id():
    df = load_furniture_data()
    if df.empty:
        return 1
    else:
        return df['Transaction'].max() + 1

def show_add_transaction_page():
    st.title("Adding Furniture")

    with st.form(key='furniture_form'):
        date = st.date_input('date_time')
        item = st.text_input('Item')
        transaction_id = get_next_transaction_id()
        submit_button = st.form_submit_button(label='Submit')

    if submit_button:
        new_data = {
            "date_time": [date],
            "Transaction": [transaction_id],
            "Item": [item],
        }
        new_data_df = pd.DataFrame(new_data)
        append_transaction_data(new_data_df)
        st.success('Data has been added successfully!')
        st.write(new_data_df)

def show_data():
    st.title("Report Data Transaction")
    df = load_furniture_data()
    
    # Konversi kolom date_time ke datetime dan urutkan berdasarkan date_time menurun
    df['date_time'] = pd.to_datetime(df['date_time'], errors='coerce')
    df = df.sort_values(by='date_time', ascending=False)
    
    # Gunakan AgGrid untuk menampilkan tabel dengan pagination
    gb = GridOptionsBuilder.from_dataframe(df)
    gb.configure_pagination(paginationAutoPageSize=False, paginationPageSize=5)
    gridOptions = gb.build()

    st.write("Report Data Transaction:")
    AgGrid(df, gridOptions=gridOptions, height=300, fit_columns_on_grid_load=True)
