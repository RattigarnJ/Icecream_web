import streamlit as st
import requests
import datetime

# Function switch page
def switch_page(page_name):
    st.session_state["page"] = page_name

if "page" not in st.session_state:
    st.session_state["page"] = "pull"

if st.session_state["page"] == "pull":

    st.sidebar.title("Menu")

    if st.sidebar.button("Pull Images"):
        switch_page("pull")
    
    elif st.sidebar.button("Show images"):
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

    selected_fday = st.date_input("select first day")

    selected_lday = st.date_input("select last day")

    if st.button("PULL"):
        st.text(f"คุณเลือกวันที่ {selected_fday} ถึง {selected_lday}")

elif st.session_state["page"] == "show":

    st.sidebar.title("Menu")

    if st.sidebar.button("Pull images"):
        switch_page("pull")

    elif st.sidebar.button("Show images"):
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

    selected_fday = st.date_input("select first day")

    selected_lday = st.date_input("select last day")

    if st.button("SHOW"):
        st.text(f"คุณเลือกวันที่ {selected_fday} ถึง {selected_lday}")

# user_input = st.text_input("พิมพ์ข้อความ:")
# if st.button("ส่ง"):
#     response = requests.post("http://127.0.0.1:8000/predict", json={"text": user_input})
#     st.write(response.json()["response"])
