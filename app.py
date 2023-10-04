import streamlit as st
import requests
import pandas as pd
import base64  # Required for file download

# API base URL
base_url = "https://universe-timetable.vercel.app/"

# Define the Streamlit app
st.title("FAST Timetable Viewer")

# Fetch a list of all subjects
all_subjects_url = base_url + "all-subjects"
response = requests.get(all_subjects_url)
if response.status_code == 200:
    all_subjects = response.json()
else:
    st.error(f"Failed to fetch subjects. Status code: {response.status_code}")
    st.stop()

# Create a multi-select widget for selecting subjects
selected_subjects = st.multiselect("Select Subjects:", all_subjects)

# Fetch and display the time table for selected subjects
if st.button("Fetch Time Table"):
    if not selected_subjects:
        st.warning("Please select at least one subject.")
    else:
        time_table_url = base_url + "time-table"
        payload = {"subjects": selected_subjects}
        response = requests.post(time_table_url, json=payload)
        if response.status_code == 200:
            time_table = response.json()

            # Create a DataFrame for the time table
            df = pd.DataFrame(time_table)

            # Display the DataFrame with styled headers
            st.markdown("### **Time Table**")
            st.dataframe(df.style.set_properties(**{'font-weight': 'bold'}, subset=pd.IndexSlice[:, ['Subject', 'Room', 'Day', 'Start-Time', 'End-Time']]))

            # Create a button for downloading the timetable data as a CSV file
            csv_data = df.to_csv(index=False, encoding='utf-8')
            b64 = base64.b64encode(csv_data.encode()).decode()
            button_label = "Download Timetable as CSV"
            st.download_button(label=button_label, data=b64, key="download_timetable_csv")

# Add the credits (always displayed)
st.markdown('<div style="text-align: center; font-size: small; margin-top: 20px;">**Credits:** Hassan Rasool, Umar Waseem, and Talal Muzaffar 🚀</div>', unsafe_allow_html=True)