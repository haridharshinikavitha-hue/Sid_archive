import streamlit as st
import base64

st.set_page_config(
    page_title="SID Archive",
    page_icon="♡",
    layout="wide"
)

# ---------- PAGE BACKGROUND ----------
def set_background(image_file):
    with open(image_file, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image:
                linear-gradient(rgba(10, 8, 7, 0.45), rgba(10, 8, 7, 0.65)),
                url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}

        .block-container {{
            padding-top: 0;
        }}

        .title {{
            text-align: center;
            margin-top: 25vh;
            font-family: Georgia, serif;
            font-size: 64px;
            letter-spacing: 10px;
            color: #f1e8dc;
            text-shadow: 0 2px 15px rgba(0,0,0,0.6);
        }}

        .divider {{
            text-align: center;
            color: #d8c8b5;
            font-size: 25px;
            margin-top: 15px;
        }}

        .subtitle {{
            text-align: center;
            font-family: Georgia, serif;
            font-size: 20px;
            font-style: italic;
            color: #ded2c3;
            margin-top: 20px;
        }}

        div.stButton {{
            text-align: center;
            margin-top: 55px;
        }}

        div.stButton > button {{
            background: transparent;
            border: none;
            color: #e5d6c4;
            font-family: Georgia, serif;
            font-size: 21px;
            font-style: italic;
            letter-spacing: 2px;
            text-decoration: underline;
            text-underline-offset: 8px;
        }}

        div.stButton > button:hover {{
            color: #ffffff;
            border: none;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )


# ---------- SCREEN ----------
if "page" not in st.session_state:
    st.session_state.page = "home"


if st.session_state.page == "home":

    set_background("background.png")

    st.markdown(
        '<div class="title">SID ARCHIVE</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="divider">──── ♡ ────</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">Some things were never meant to disappear.</div>',
        unsafe_allow_html=True
    )

    if st.button("open the archive"):
        st.session_state.page = "archive"
        st.rerun()


# ---------- ARCHIVE ----------
elif st.session_state.page == "archive":

    st.markdown(
        """
        <div style="
            text-align:center;
            margin-top:18vh;
            font-family:Georgia,serif;
        ">
            <div style="
                font-size:45px;
                letter-spacing:7px;
                color:#eee8df;
            ">
                THE ARCHIVE
            </div>

            <div style="
                margin-top:20px;
                font-size:17px;
                font-style:italic;
                color:#aaa29a;
            ">
                What would you like to open?
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("♡  LETTERS", use_container_width=True):
            st.session_state.page = "letters"
            st.rerun()

    with col2:
        if st.button("♡  UNSENT", use_container_width=True):
            st.session_state.page = "unsent"
            st.rerun()
