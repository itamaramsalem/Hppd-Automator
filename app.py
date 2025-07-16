import streamlit as st
import os
from datetime import datetime
from hppdauto import run_hppd_comparison_for_date, run_hppd_analysis

st.set_page_config(page_title="HPPD Automator", layout="centered")
st.title("📊 HPPD Automator")

# Step 1: Input folders
st.markdown("### 1. Enter Folder Paths")
template_path = st.text_input("Labor Templates Folder Path")
report_path = st.text_input("Actual Reports Folder Path")

# Step 2: Choose run mode
st.markdown("### 2. Choose Analysis Mode")
run_mode = st.radio("Run Mode", ["Specific Date", "All Dates"])

if run_mode == "Specific Date":
    selected_date = st.date_input("Select date to analyze")
    date_str = selected_date.strftime("%Y-%m-%d")
else:
    date_str = None

# Step 3: Trigger analysis
if st.button("Run HPPD Comparison"):
    if not os.path.isdir(template_path):
        st.error("❌ Invalid templates folder path.")
    elif not os.path.isdir(report_path):
        st.error("❌ Invalid reports folder path.")
    else:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = f"HPPD_Comparison_{date_str or 'ALL'}_{timestamp}.xlsx"

        try:
            if date_str:
                run_hppd_comparison_for_date(
                    templates_folder=template_path,
                    reports_folder=report_path,
                    target_date=date_str,
                    output_path=output_file
                )
            else:
                run_hppd_analysis(
                    template_dir=template_path,
                    report_dir=report_path,
                    output_path=output_file
                )
            st.success("✅ Report generated successfully!")

            with open(output_file, "rb") as f:
                st.download_button(
                    label="⬇️ Download Excel Report",
                    data=f,
                    file_name=os.path.basename(output_file),
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )

        except ValueError as e:
            log_path = os.path.join(os.path.dirname(output_file), "hppd_skip_log.txt")
            if os.path.exists(log_path):
                with open(log_path, "r") as logf:
                    log_contents = logf.read()
                st.error(str(e))
                st.text_area("Details from Skip Log", log_contents, height=300)
            else:
                st.error(str(e))

        except Exception as e:
            st.error(f"❌ Unexpected error: {e}")
