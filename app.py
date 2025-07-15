
import streamlit as st
import zipfile
import tempfile
import os
from datetime import datetime
from hppdauto import run_hppd_comparison_for_date

st.set_page_config(page_title="HPPD Automator", layout="centered")
st.title("HPPD Automator")

# Step 1: Upload zipped folders
st.markdown("### 1. Upload Zipped Folders")
template_zip = st.file_uploader("Labor Templates (.zip)", type="zip")
report_zip = st.file_uploader("Actual Reports (.zip)", type="zip")

# Step 2: Choose analysis mode
st.markdown("### 2. Choose Date Range")
date_mode = st.radio("Run Mode", ["Specific Date", "All Dates"])

if date_mode == "Specific Date":
    target_date = st.date_input("Select the date you want to analyze")
else:
    target_date = None

# Step 3: Run analysis
if st.button("Generate Report"):
    if not template_zip or not report_zip:
        st.error("Please upload both zipped folders.")
    else:
        with tempfile.TemporaryDirectory() as tmpdir:
            templates_dir = os.path.join(tmpdir, "templates")
            reports_dir = os.path.join(tmpdir, "reports")
            output_file = os.path.join(tmpdir, "HPPD_Report.xlsx")

            # Extract zip files
            with zipfile.ZipFile(template_zip, 'r') as z:
                z.extractall(templates_dir)
            with zipfile.ZipFile(report_zip, 'r') as z:
                z.extractall(reports_dir)

            date_str = target_date.strftime("%Y-%m-%d") if target_date else None
            try:
                run_hppd_comparison_for_date(
                    templates_folder=templates_dir,
                    reports_folder=reports_dir,
                    target_date=date_str,
                    output_path=output_file
                )
                st.success("Report generated successfully!")

                with open(output_file, "rb") as f:
                    st.download_button(
                        label="Download Excel Report",
                        data=f,
                        file_name=f"HPPD_Comparison_{date_str or 'ALL'}.xlsx",
                        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                    )
            except Exception as e:
                st.error(f"Error occurred during processing:\n{e}")
