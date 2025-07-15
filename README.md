# HPPD Automator

A streamlined tool for skilled nursing facilities to compare projected labor templates against actual staffing reports. The HPPD Automator ensures labor budget adherence, highlights staffing discrepancies, and tracks agency and overtime usage — all from a simple web interface.

---

## Features

- 📊 **Daily HPPD Comparison**  
  Compares projected and actual Hours Per Patient Day (HPPD) per facility.

- 📉 **Department-Level Budget Checks**  
  Validates CNA and RN/LPN splits separately to flag over- or under-spending.

- 🔍 **Agency & Overtime Tracking**  
  Calculates agency staffing percentages and total overtime hours.

- 📅 **Per-Day or Full-Batch Analysis**  
  Run reports for a specific day or all available dates.

- 📥 **Excel Output**  
  Generates a formatted, categorized Excel report with color-coded sections.

---

## 🧠 How It Works

1. **Upload Folders**  
   Provide the file paths to:
   - Labor Template Folder (projections)
   - Actual Report Folder (post-shift hours)

2. **Select a Date**  
   Choose a specific date or run for all available data.

3. **Generate Report**  
   The system matches facilities by name and date, runs analysis, and outputs an Excel file.

---

## 🛠 Built With

- [Streamlit](https://streamlit.io) – UI framework
- `pandas`, `openpyxl`, `xlrd` – Excel and data processing
- Python 3.8+

---

## 🧪 Local Development

```bash
git clone https://github.com/yourusername/hppd-automator.git
cd hppd-automator
pip install -r requirements.txt
streamlit run app.py
