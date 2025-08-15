import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

class Dashboard:
    
    def __init__(self):
        if "data" not in st.session_state:
            st.session_state.data = []
    
    def add_entry(self,name,score,catagory):
        if name and score is not None:
            st.session_state.data.append({"Name":name, "Score": score})
            return True
        return False
   
    def get_dataframe(self):
        return pd.DataFrame(st.session_state.data)
    
    