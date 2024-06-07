import streamlit as st
from ydata_profiling import ProfileReport
import pandas as pd
import seaborn as sns
import os
import streamlit.components.v1 as components
# welcome to main code.
# Set up the page layout
st.set_page_config(layout="wide")
st.title("Upload CSV or Excel File and Display Pandas Profiling Report")

# Function to read CSV or Excel file
def load_file(uploaded_file):
    if uploaded_file is not None:
        try:
            if uploaded_file.name.endswith('.csv'):
                df = pd.read_csv(uploaded_file)
            elif uploaded_file.name.endswith(('.xls', '.xlsx')):
                df = pd.read_excel(uploaded_file)
            else:
                st.error("Unsupported file type. Please upload a CSV or Excel file.")
                return None
            return df
        except Exception as e:
            st.error(f"Error loading file: {e}")
            return None
    else:
        st.info("Please upload a file.")
        return None

# File uploader
uploaded_file = st.file_uploader("Choose a CSV or Excel file", type=['csv', 'xls', 'xlsx'])

# Load and display the pandas profile file
if uploaded_file is not None:
    df = load_file(uploaded_file)
    if df is not None:
        # Generate the profiling report
        profile = ProfileReport(df, title="Pandas Profiling Report of the Given Data Set", explorative=True)

        # Save the report to a temporary HTML file
        tmp_html_path = "report.html"
        profile.to_file(tmp_html_path)

        # Read the HTML file and display it in Streamlit
        with open(tmp_html_path, "r", encoding='utf-8') as f:
            html_content = f.read()
        # Use streamlit's st.components.v1.html to display the report
        components.html(html_content, height=800, scrolling=True)

        # Optionally, clean up the temporary file
        os.remove(tmp_html_path)

   

