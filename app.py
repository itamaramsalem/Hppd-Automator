import streamlit as st
import os
import tempfile
from datetime import datetime
from hppdauto import run_hppd_comparison_for_date

st.set_page_config(page_title="HPPD Automator", layout="centered")
st.title("📊 HPPD Automator")

# Step 1: Manual folder paths
st.markdown("### 1. Enter Folder Paths")
template_folder = st.text_input("📂 Path to Labor Templates Folder (e.g. C:/Users/You/Desktop/Templates)")
report_folder = st.text_input("📂 Path to Actual Reports Folder (e.g. C:/Users/You/Desktop/Reports)")

# Step 2: Date selection OR All
st.markdown("### 2. Choose a Date")
date_mode = st.radio("Run Mode", ["Specific Date", "All Dates"])

if date_mode == "Specific Date":
    target_date = st.date_input("📅 Select the date you want to analyze")
else:
    target_date = None

# Step 3: Generate report
if st.button("Generate Report"):
    if not template_folder or not report_folder:
        st.error("❌ Please provide both folder paths.")
    elif not os.path.isdir(template_folder) or not os.path.isdir(report_folder):
        st.error("❌ One or both paths are invalid.")
    else:
        with tempfile.TemporaryDirectory() as tmpdir:
            date_suffix = target_date.strftime('%Y%m%d') if target_date else "ALL"
            output_path = os.path.join(tmpdir, f"HPPD_Report_{date_suffix}.xlsx")
            try:
                run_hppd_comparison_for_date(
                    templates_folder=template_folder,
                    reports_folder=report_folder,
                    target_date=target_date.strftime("%Y-%m-%d") if target_date else None,
                    output_path=output_path
                )
                st.success("✅ Report generated successfully!")

                with open(output_path, "rb") as f:
                    st.download_button(
                        label="📥 Download Excel Report",
                        data=f,
                        file_name=f"HPPD_Comparison_{date_suffix}.xlsx",
                        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                    )
            except Exception as e:
                st.error(f"❌ An error occurred during processing:\n\n{e}")
