import streamlit as st
from main import Dashboard

st.set_page_config(
    page_title="Advanced Data Dashboard",
    page_icon="💻",
    layout="wide"
)

dashboard = Dashboard()

st.title("📊 Advanced Data Dashboard")
st.markdown("---")

st.subheader("➕ Add New Entry")

with st.form("entry_form"):

    col1, col2 = st.columns(2)
    
    with col1:
        name = st.text_input(
            "Name", 
            placeholder="Enter your name",
            help="Enter the participant's name"
        )
        
    with col2:
        category = st.selectbox(
            "Category",
            ["General", "Maths", "Science", "Commerce", "Art"],
            help="Select the appropriate category"
        )
    
    score = st.number_input(
        "Score",
        min_value=0.0,
        max_value=100.0,
        step=0.1,
        format="%.1f",
        help="Enter score between 0 and 100"
    )
    

    col1, col2 = st.columns(2)
    with col1:
        submitted = st.form_submit_button(
            "✅ Add Entry", 
            use_container_width=True,
            type="primary"
        )
    with col2:
        clear_all = st.form_submit_button(
            "🗑️ Clear All", 
            use_container_width=True
        )
    

    if submitted:
        if name.strip():  
            if dashboard.add_entry(name, score, category):
                st.success(f"✅ Successfully added: {name} - {score}%")
            else:
                st.error("❌ Failed to add entry. Please check your input.")
        else:
            st.error("❌ Please enter a valid name.")
    
    if clear_all:
        dashboard.clear_data()
        st.success("🧹 All data cleared successfully!")
        st.rerun()

st.markdown("---")


df = dashboard.get_dataframe()

if not df.empty:

    st.subheader("📋 Current Data")
    st.dataframe(
        df, 
        use_container_width=True,
        hide_index=True
    )
    

    st.subheader("📈 Data Visualization")
    dashboard.plot_data()
    

    st.markdown("---")
    st.subheader("💾 Export Data")
    
    file = dashboard.save_to_excel()
    if file:
        with open(file, "rb") as f:
            st.download_button(
                "📥 Download Excel File",
                data=f,
                file_name=file,
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                use_container_width=True
            )
else:
    st.info("📝 No data available. Add your first entry using the form above!")