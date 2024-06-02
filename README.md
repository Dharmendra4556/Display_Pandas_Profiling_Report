# Upload CSV or Excel File and Display Pandas Profiling Report

This Streamlit application allows users to upload a CSV or Excel file and then generates a Pandas Profiling Report for the uploaded dataset. The report is displayed directly in the Streamlit app, providing an easy and interactive way to explore and analyze data.

## Features

- Upload CSV or Excel files (.csv, .xls, .xlsx)
- Display a detailed profiling report of the dataset
- Interactive and scrollable report within the Streamlit app
- Error handling for unsupported file types and file loading issues

## Installation


1. Install the required packages:

   ```sh
   pip install pandas seaborn ydata_profiling
   ```

## Usage

2. Run the Streamlit app:

   ```sh
   streamlit run pandas_profiling_report.py
   ```

3. Open your web browser and go to `http://localhost:8501`

4. Upload a CSV or Excel file using the file uploader.

5. The Pandas Profiling Report will be generated and displayed within the app.

## Code Overview

The main functionality is implemented in the `pandas_profiling_report.py` file. Here's a brief overview of the key sections:

### Page Layout

The page layout is set to wide for better visualization of the profiling report.

```python
st.set_page_config(layout="wide")
st.title("Upload CSV or Excel File and Display Pandas Profiling Report")
```

### File Loading Function

The `load_file` function reads the uploaded file and returns a DataFrame. It handles both CSV and Excel files and provides error messages for unsupported file types or loading issues.

```python
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
```

### File Uploader and Profiling Report

The uploaded file is processed, and a Pandas Profiling Report is generated and displayed using Streamlit's HTML component.

```python
uploaded_file = st.file_uploader("Choose a CSV or Excel file", type=['csv', 'xls', 'xlsx'])

if uploaded_file is not None:
    df = load_file(uploaded_file)
    if df is not None:
        profile = ProfileReport(df, title="Pandas Profiling Report of the Given Data Set", explorative=True)
        
        tmp_html_path = "report.html"
        profile.to_file(tmp_html_path)
        
        with open(tmp_html_path, "r", encoding='utf-8') as f:
            html_content = f.read()
        components.html(html_content, height=800, scrolling=True)
        
        os.remove(tmp_html_path)
```

## Requirements

- streamlit
- pandas
- seaborn
- ydata-profiling

These can be installed using the following command:

```sh
pip install streamlit pandas seaborn ydata-profiling
```


## Author

- [Dharmendra](https://github.com/Dharmendra4556)

## Acknowledgments

- [Streamlit](https://streamlit.io/)
- [Pandas Profiling](https://github.com/ydataai/pandas-profiling)

## Contact

For more information, visit my [LinkedIn profile](https://www.linkedin.com/in/dharmendra-behara-230388239/).
