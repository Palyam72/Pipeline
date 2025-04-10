import streamlit as st
from sklearn.impute import *

def missing_data():
    st.subheader("Pipeline For Imputing Missing Values",divider='green')
    
    imputers = [
        'IterativeImputer', 'KNNImputer', 'MissingIndicator', 'SimpleImputer',
        'ArbitraryNumberImputer', 'EndTailImputer', 'CategoricalImputer',
        'RandomSampleImputer', 'DropMissingData'
    ]
    
    functions_list = [
        iterative_imputer,
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
    fuction_list[imputers.index(selectedImputer)]

# Initialize all imputer functions with pass (to be implemented later)
def iterative_imputer():
    pass

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
