
# AI-Powered Product Recommender using Gemini

This project is a lightweight product recommendation system built for e-commerce platforms. It uses Google's Gemini API to generate personalized product suggestions based on user preferences like category, brand, and price range. The goal is to offer smart suggestions without relying on traditional recommendation engines.

## 🔍 What It Does

- Accepts user preferences for department, category, brand, and price
- Uses Gemini API to suggest similar products
- Visualizes key product trends like pricing and discounts
- Works with CSV datasets from sources like Flipkart or your own

## 🚀 How to Run

1. Clone the project:
```bash
git clone https://github.com/yagneshs2004/Product-Recommendation-System-Using-GEN-AI.git
cd gemini-recommender
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up your Gemini API Key:
- Create a `.env` file and add:
```
GEMINI_API_KEY=your-gemini-api-key
```

4. Start the app:
```bash
streamlit run app.py
```

## 📊 Dataset

You can use any CSV file with product details like category, price, brand, description, and image links. The system will preprocess and filter the data automatically.

## 🧠 Powered By

- **Streamlit** for UI
- **Google Gemini API** for smart recommendations
- **Pandas + Seaborn** for data handling and charts

## 📌 Notes

- All suggestions are generated on-the-fly using Gemini, no local model or vector database required.
- Ideal for small/medium datasets and testing generative AI for e-commerce use cases.

## 🛠️ Improvements to Add

- Upload product images for visual recommendation
- Save user history for personalized results
- Add feedback loop for better future suggestions

---

MIT License © 2025
