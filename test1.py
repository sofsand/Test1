#Import streamlit and the necessary libraries
import streamlit as st
import requests
import json

#Set up the page configuration of our app
st.set_page_config(
    page_title="MySmartFridge",
    page_icon= "smart-fridge.png", 
    layout="centered",    
    initial_sidebar_state="expanded",
)

#Set the title of our app 
st.title("MySmartFridge: No more FoodWaste, No more MoneyWaste")

#API endpoint URL
#migros_url = "https://nutristorage.ch/api/products/migros/{gtin}/"
#coop_url = "https://nutristorage.ch/api/products/coop/{gtin}/"

#Send a GET request
#response = requests.get(migros_url)
#response = requests.get(coop_url)

#Check whether the request is successful
#if response.status_code == 200:
#    data = response.json() #Convert JSON response to a Python dictionary
#    st.write("Data received:", data)  # Display the data in the Streamlit app
#else:
#    st.error(f"Request error: {response.status_code}")



#Add a field to input the barcode (user interface)
#barcode = st.text_input("Enter the product barcode:")

#Button to submit the barcode and get product information
#if st.button("Search Product"):
#    if barcode:
        # Build the URL to search for the product using the barcode
 #       barcode_url = f"https://api.example.com/products/{barcode}"  # Modify based on the API

        # Send a GET request for the specific barcode
 #       response = requests.get(barcode_url)

        # Check if the request was successful
#      if response.status_code == 200:
#            product_data = response.json()  # Convert the JSON response to a Python dictionary
 #           st.write("Product information:", product_data)  # Display product information
 #       else:
  #          st.error(f"Product not found. Error: {response.status_code}")
   # else:
    #    st.warning("Please enter a valid barcode.")