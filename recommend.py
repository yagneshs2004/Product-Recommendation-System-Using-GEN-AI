
import os
from dotenv import load_dotenv
import streamlit as st
import pandas as pd
import google.generativeai as genai

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def generate_recommendation(department, category, brand, price):
    model = genai.GenerativeModel("gemini-1.5-flash")
    prompt = f"""
    You are a helpful AI assistant trained to recommend e-commerce products.

    Product Department: {department}
    Product Category: {category}
    Product Brand: {brand}
    Maximum Price Range: ₹{price}

    Recommend 3 similar products including:
    - Product Name
    - Product Category
    - Price
    - Brand
    - Stock Quantity (assume if unknown)
    - One-line description

    Sort them by the lowest price first.
    """
    response = model.generate_content(prompt)
    return response.text

def display_product_recommendation(refined_df):
    st.header("Gemini-based Product Recommendation")

    department = st.text_input("Product Department")
    category = st.text_input("Product Category")
    brand = st.text_input("Product Brand")
    price = st.text_input("Maximum Price Range")

    if st.button("Get Recommendations"):
        result = generate_recommendation(department, category, brand, price)
        st.write(result)
