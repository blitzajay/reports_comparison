# 📊 Report Comparison Tool (Streamlit)

This is a simple web app built using [Streamlit](https://streamlit.io/) that allows users to **upload two report files** (CSV, XLS, or XLSX) and **compare them** row-by-row and column-by-column. The app highlights mismatches and allows users to download a mismatch report as CSV.

---

## 🔧 Features

- Upload two reports from the browser
- Supports `.csv`, `.xls`, and `.xlsx` formats
- Compares:
  - Column names
  - Row counts
  - Cell-by-cell values
- Highlights mismatches
- Allows mismatches to be downloaded

---

## 🚀 How to Use

1. Visit the app:  
   📍 _**[your-streamlit-app-url-here]**_  
   *(You’ll update this after deployment)*

2. Upload the two reports you want to compare

3. Wait for the comparison results:
   - If no mismatches → ✅ message
   - If mismatches found → Preview table + Download button

---

## 🛠️ Local Setup (for developers)

1. Clone the repo:
   ```bash
   git clone https://github.com/YOUR_USERNAME/report-comparator.git
   cd report-comparator

2. Install dependencies
    pip install -r requirements.txt

3. Run the app:
    streamlit run streamlit_data_compare.py