import streamlit as st
from prediction import show_prediction_page
from apriori import show_apriori_page
from add_transaction import show_add_transaction_page, show_data
from adding_item_furniture import show_adding_item_furniture_page
from update_item_furniture import show_update_item_page

# Judul aplikasi
st.title("Implementation Algorithm Apriori With Method Single Moving Average")

# Menu sidebar
pilihan = st.sidebar.radio(
    "Menu",
    ("Home", "Prediction", "Apriori", "Adding Furniture", "Adding Item Furniture", "Update Item Furniture")
)

# Konten berdasarkan pilihan sidebar
if pilihan == "Home":
    st.title("Halaman Utama")
    st.write("Selamat datang di halaman utama.")
elif pilihan == "Prediction":
    show_prediction_page()
elif pilihan == 'Apriori':
    show_apriori_page()
elif pilihan == 'Adding Furniture':
    show_add_transaction_page()
    show_data()
elif pilihan == 'Adding Item Furniture':
    show_adding_item_furniture_page()
elif pilihan == 'Update Item Furniture':
    show_update_item_page()
