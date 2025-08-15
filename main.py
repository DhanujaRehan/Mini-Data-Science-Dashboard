import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

class Dashboard:
    
    def __init__(self):
        if "data" not in st.session_state:
            st.session_state.data = []
    
    def add_entry(self,name,score,category):
        if name and score is not None:
            st.session_state.data.append({"Name": name, "Score": score, "Category": category})
            return True
        return False
   
    def get_dataframe(self):
        return pd.DataFrame(st.session_state.data)

    def save_to_excel(self,filename = "MiniDashBoard.xlsx"):
        df = self.get_dataframe()
        if not df.empty:
            df.to_excel(filename, index=False)
            return filename
        return None
    
    def plot_data(self):
        df = self.get_dataframe()
        if not df.empty:
            fig,ax = plt.subplots()
            ax.bar(df["Name"],df["Score"],df["category"],color="blue")
            plt.xticks(rotation = 45)
            ax.set_title("Score Chart")
            ax.set_xlabel("Name")
            ax.set_ylabel("Score")
            st.pyplot(fig)
    def clear_data(self):
        st.session_state.data = []
    
     
     
    
    