import streamlit as st

st.set_page_config(
    page_title="SID Archive",
    page_icon="♡",
    layout="centered"
)

st.markdown(
    """
    <style>
    .stApp {
        background-color: #11100f;
        color: #eee8df;
    }

    .title {
        text-align: center;
        margin-top: 180px;
        font-family: Georgia, serif;
        font-size: 48px;
        letter-spacing: 8px;
        color: #eee8df;
    }

    .subtitle {
        text-align: center;
        font-family: Georgia, serif;
        font-size: 16px;
        font-style: italic;
        color: #a9a29a;
        margin-top: 20px;
    }

    .enter {
        text-align: center;
        margin-top: 50px;
        font-family: Georgia, serif;
        color: #c8b9a6;
        letter-spacing: 3px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    '<div class="title">SID ARCHIVE</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">A place for everything that remained.</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="enter">ENTER ♡</div>',
    unsafe_allow_html=True
)
