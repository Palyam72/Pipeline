import streamlit as st
from sklearn.impute import *

def missing_data():
    st.subheader("Pipeline For Imputing Missing Values",divider='green')
    
    imputers = [
        'MeanMedianImputer', 'KNNImputer', 'MissingIndicator', 'SimpleImputer',
        'ArbitraryNumberImputer', 'EndTailImputer', 'CategoricalImputer',
        'RandomSampleImputer', 'DropMissingData'
    ]
    
    functions_list = [
        mean_median_imputer,
        knn_imputer,
        missing_indicator,
        simple_imputer,
        arbitrary_number_imputer,
        end_tail_imputer,
        categorical_imputer,
        random_sample_imputer,
        drop_missing_data
    ]
    
    selectedImputer=st.selectbox("Select the imputer",imputers)
    if selectedImputer:
       functions_list[imputers.index(selectedImputer)]()

# Initialize all imputer functions with pass (to be implemented later)
def mean_median_imputer():
    st.markdown("##### Set the params")
    imputation_method=st.seslectbox("How you want to fill the missing values in numerical columns",['median','mean'])
    variables=st.multiselect("List of numerical columns to impute",[st.session_state['dataset'].select_dtypes(include=['int8','int32','int64','float8','float32','float64']).columns])
    if st.button("Add To Pipeline",use_container_width=True,type='primary'):
        if imputation_method and variables:
            st.session_state['pipeline'].append(MeanMedianImputer(imputation_method,variables))
            st.success("Added Successfully")
        else:
            st.warning("All inputs are required")
def knn_imputer():
    pass

def missing_indicator():
    pass

def simple_imputer():
    pass

def arbitrary_number_imputer():
    pass

def end_tail_imputer():
    pass

def categorical_imputer():
    pass

def random_sample_imputer():
    pass

def drop_missing_data():
    pass
