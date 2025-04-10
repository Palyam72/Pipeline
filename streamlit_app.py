import streamlit as st
import chardet
import pandas as pd

# Import all stage modules
from missing_data import *
from outlier_removal import *  
from encoding import *
from feature_selection import *  
from feature_creation import *
from feature_scaling import *
from train_test_split import *
from model_selection import *
from model_download import *

# Function to read file with encoding detection
def read_file(fileUploaded):
    # Detect the file encoding
    raw_data = fileUploaded.read()
    result = chardet.detect(raw_data)
    encoding = result['encoding']
    
    # Reset file pointer to beginning
    fileUploaded.seek(0)
    
    # Read file based on its type
    if fileUploaded.type == 'text/csv':
        return pd.read_csv(fileUploaded, encoding=encoding)
    elif fileUploaded.type in [
        'application/vnd.ms-excel', 
        'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    ]:
        return pd.read_excel(fileUploaded)
    else:
        st.error("Unsupported file type")
        return None

# Initialize pipeline in session state if not exists
if "pipeline" not in st.session_state:
    st.session_state['pipeline'] = []

# Display pipeline in sidebar
st.sidebar.subheader("View the stages that you add in pipeline here", divider='blue')
if not st.session_state['pipeline']:
    st.sidebar.warning("No Stages were added into pipeline")
else:
    st.sidebar.write(st.session_state['pipeline'])

# File uploader
st.sidebar.subheader("Upload file here", divider='blue')
fileUploaded = st.file_uploader("Upload files", type=['csv', 'xlsx'])

# Store uploaded dataset in session state
if fileUploaded:
    st.session_state['dataset'] = read_file(fileUploaded)

# Stage mapping
mapper = {
    1: missing_data,
    2: outlier_removal,
    3: encode,
    4: feature_selection,
    5: feature_creation,
    6: feature_scaling,
    7: train_test_split,
    8: model_selection,
    9: model_download
}

# Create individual column objects
col1, col2 = st.columns(2, border=True)
col3, col4 = st.columns(2, border=True)
col5_list = st.columns(1, border=True)
col6, col7 = st.columns(2, border=True)
col8, col9 = st.columns(2, border=True)

# Unpack col5_list (which is a list) correctly
col5 = col5_list[0]

# Store all column references in one flat list
columns = [col1, col2, col3, col4, col5, col6, col7, col8, col9]

# Render each stage module in its corresponding column
for i in range(1, 10):
    with columns[i - 1]:
        mapper[i]()  # Call the respective function
