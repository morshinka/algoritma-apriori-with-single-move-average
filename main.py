import streamlit as st
from prediction import show_prediction_page
from apriori import show_apriori_page
from add_transaction import show_add_transaction_page, show_data
from adding_item_furniture import show_adding_item_furniture_page
from update_item_furniture import show_update_item_page

# Fungsi untuk memeriksa status login
def check_login():
    if 'logged_in' not in st.session_state or not st.session_state['logged_in']:
        st.error("You must log in first!")
        st.experimental_set_query_params(page="login")
        st.experimental_rerun()

# Fungsi utama
def main():
    # Periksa status login
    check_login()

    # Judul aplikasi
    st.title("Implementation Algorithm Apriori With Method Single Moving Average")

    # Menu sidebar
    pilihan = st.sidebar.radio(
        "Menu",
        ("Home", "Prediction", "Apriori", "Adding Furniture", "Adding Item Furniture", "Update Item Furniture")
    )

    # Tombol logout di sidebar
    if st.sidebar.button("Logout"):
        st.session_state['logged_in'] = False
        st.session_state['page'] = "login"
        st.experimental_rerun()

    # Konten berdasarkan pilihan sidebar atau session state
    if pilihan == "Home" or st.session_state.get("section") == "home":
        st.title("Halaman Utama")
        st.write("Selamat datang di halaman utama.")
    elif pilihan == "Prediction" or st.session_state.get("section") == "prediction":
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

    # Update session state berdasarkan pilihan
    st.session_state["section"] = pilihan.lower()

if __name__ == '__main__':
    main()
