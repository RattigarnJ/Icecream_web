import streamlit as st
import requests
from datetime import date
import subprocess
import os

# Function switch page
def switch_page(page_name):
    st.session_state["page"] = page_name

# Func - DATE for GET tr & td
def get_column_day(selected_date):
    weekday = selected_date.weekday()
    weekday = (weekday + 1) % 7
    column = (weekday % 7) + 1
    day = selected_date.day
    return day, column

def get_row_day(day, column, selected_date):
    first_day_of_month = selected_date.replace(day=1)
    first_day_column = ((first_day_of_month.weekday() + 1) % 7) + 1
    day_position = day + (first_day_column - 1)
    row = (day_position - 1) // 7 + 1
    return row

documents_path = os.path.join(os.path.expanduser("~"), "Documents", "IcecreamWeb")

# Setting Default Page
if "page" not in st.session_state:
    st.session_state["page"] = "pull"

# Pull Page
if st.session_state["page"] == "pull":

    st.sidebar.title("Mode")

    if st.sidebar.button("Pull Images"):
        switch_page("pull")
    
    elif st.sidebar.button("Show Images"):
        switch_page("show")

    # Logo 7-11
    st.markdown(
    """
    <div style="text-align:center;">
        <img src= "https://upload.wikimedia.org/wikipedia/commons/4/40/7-eleven_logo.svg" width="100">
    </div>
    """, unsafe_allow_html=True
    )
    
    st.markdown(
    """
    <h1 style="text-algin:center;">
        PULL IMAGES ICE CREAM CABINET
    </h1>
    """, unsafe_allow_html=True
    )

    # Keep value in mode session_state
    if "mode" not in st.session_state:
        st.session_state.mode = None

    if st.button("Daily"):
        st.session_state.mode = "daily"

    elif st.button("Period Day"):
        st.session_state.mode = "period"

    # Daily Mode
    if st.session_state.mode == "daily":
        selected_day = st.date_input("Select a day")
        
        if st.button("PULL Daily"):
            st.write("Mode: Daily")
            st.write(f"Selected Day: {selected_day}")
            period = 0

            fday , td = get_column_day(selected_day)
            tr = get_row_day(fday, td, selected_day)

            selected_folder_name = selected_day.strftime("%Y-%m-%d")
            # Var image & csv FOLDER
            # folder branch code ??
            image_folder = os.path.join(documents_path, "IMAGE_file")
            csv_folder = os.path.join(documents_path, "CSV_file" , f"{selected_folder_name}_csv")

            if not (os.path.exists(image_folder) or os.path.exists(csv_folder)):
                try:
                    st.sidebar.write("Running RPA script to fetch images...")
                    result = subprocess.run(["python", "rpa_pulldaily.py",str(tr),str(td),str(selected_day.month),str(selected_day.year),str(period)]
                    , capture_output=True, text=True, encoding="utf-8")
                    if result.returncode == 0:
                        st.sidebar.success("RPA script completed successfully!")
                    else:
                        st.error(f"RPA script failed. Error: {result.stderr}")
                        st.stop()
                except Exception as e:
                    st.error(f"An unexpected error occurred: {e}")
                    st.stop()

    # Period Day Mode
    elif st.session_state.mode == "period":
        selected_fday = st.date_input("Select first day")
        selected_lday = st.date_input("Select last day")

        period = (selected_fday.day - selected_lday.day) + 1
        
        if st.button("PULL Period"):
            st.write("Mode: Period")
            st.write(f"Start Date: {selected_fday}")
            st.write(f"End Date: {selected_lday}")
            
            fday , td = get_column_day(selected_fday)
            tr = get_row_day(fday, td, selected_fday)

            selected_folder_name = selected_fday.strftime("%Y-%m-%d")
            # Var image & csv FOLDER
            # folder branch code ??
            image_folder = os.path.join(documents_path, "IMAGE_file")
            csv_folder = os.path.join(documents_path, "CSV_file" , f"{selected_folder_name}_csv")

            if not (os.path.exists(image_folder) or os.path.exists(csv_folder)):
                try:
                    st.sidebar.write("Running RPA script to fetch images...")
                    result = subprocess.run(["python", "rpa_pullperiod.py",str(tr),str(td),str(selected_fday.month),str(selected_fday.year),str(period)
                    ], capture_output=True, text=True, encoding="utf-8")
                    if result.returncode == 0:
                        st.sidebar.success("RPA script completed successfully!")
                    else:
                        st.error(f"RPA script failed. Error: {result.stderr}")
                        st.stop()
                except Exception as e:
                    st.error(f"An unexpected error occurred: {e}")
                    st.stop()

# Show Page
elif st.session_state["page"] == "show":

    st.sidebar.title("Mode")

    if st.sidebar.button("Pull Images"):
        switch_page("pull")

    elif st.sidebar.button("Show Images"):
        switch_page("show")

    # Logo 7-11
    st.markdown(
    """
    <div style="text-align:center;">
        <img src= "https://upload.wikimedia.org/wikipedia/commons/4/40/7-eleven_logo.svg" width="100">
    </div>
    """, unsafe_allow_html=True
    )

    st.markdown(
        """
        <h1 style="text-algin:center;">
            SHOW IMAGES ICE CREAM CABINET
        </h1>
        """, unsafe_allow_html=True
    )

    # Keep value in mode session_state
    if "mode" not in st.session_state:
        st.session_state.mode = None
    
    if st.button("Daily"):
        st.session_state.mode = "daily"

    elif st.button("Period Day"):
        st.session_state.mode = "period"

    # Daily Mode
    if st.session_state.mode == "daily":
        selected_day = st.date_input("Select a day", key="daily_date")
        
        if st.button("SHOW Daily"):
            st.write("Mode: Daily")
            st.write(f"Selected Day: {selected_day}")

    # Period Day Mode
    elif st.session_state.mode == "period":
        selected_fday = st.date_input("Select first day", key="fday")
        selected_lday = st.date_input("Select last day", key="lday")
        
        if st.button("SHOW Period"):
            st.write("Mode: Period")
            st.write(f"Start Date: {selected_fday}")
            st.write(f"End Date: {selected_lday}")

# user_input = st.text_input("พิมพ์ข้อความ:")
# if st.button("ส่ง"):
#     response = requests.post("http://127.0.0.1:8000/predict", json={"text": user_input})
#     st.write(response.json()["response"])
