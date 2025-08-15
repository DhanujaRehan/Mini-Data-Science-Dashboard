import streamlit as st
from main import Dashboard

st.set_page_config(
    page_title = "Advance Data Dashboard",
    page_icon = "💻",
    layout = "wide"
)

dashboard = Dashboard()

st.markdown("Add New Entry")
with st.form("entry_form"):
    name = st.text_input("Name",placeholder= "Enter your name")
    score = st.number_input("Score",min_value = 0.0, max_value = 100.0,step=0.1,format = "%.1f")
    category = st.selectbox("Category",["General","Maths","Science", "Commerce", "Art"])
    
    col1 , col2 = st.columns(2)
    with col1:
        submitted = st.form_submit_button("Add Entry",use_container_width=True)
    with col2 :
        clear_all = st.form_submit_button("Clear All", use_container_width =True)
        
    if submitted:
        if dashboard.add_entry(name,score,category):
            st.success(f"Added : {name} - {score}")
        else:
            st.error("Please enter correct value")
            
    if clear_all:
        dashboard.clear_data()
        st.success(f"All data clear successfulyy")
        st.rerun()
            
df = dashboard.get_dataframe()

if not df.empty:
    st.subheading("Entered Data")
    st.dataframe(df)
    
    st.subheading("Visualization")
    dashboard.plot_data()
    
    file = dashboard.save_to_excel()
    if file:
        with open(file, "rb") as f:
            st.download_button("Download the excel file", f , file_name = file)