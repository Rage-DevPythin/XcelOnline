import streamlit as st
import pandas as pd

# Set up the page config
st.set_page_config(page_title="XcelOnline")

# Title of the web page
st.title("Welcome to XcelOnline (Or Excel Online) :wave:")

# Simple slider widget
slider_number = st.slider("Select a rating between 1-100", 1, 100, 50)

# Display the selected rating
st.write(f"You selected {slider_number}. Thank you!")

# File uploader widget for Excel file
uploaded_file = st.file_uploader("Upload your Excel file", type="xlsx")

# Check if the user uploaded a file
if uploaded_file is not None:
    # Read the Excel file into a DataFrame
    df = pd.read_excel(uploaded_file)

    # Display the content of the Excel file as a dataframe
    st.subheader("Excel File Content")
    st.dataframe(df)  # Display the Excel data as a table
else:
    st.write("Please upload an Excel file to display its content.")
