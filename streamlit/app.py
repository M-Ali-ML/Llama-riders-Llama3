import streamlit as st

# Streamlit app
st.markdown("<h1 style='text-align: center;'>Job Application Assistant</h1>", unsafe_allow_html=True)

# Input form
with st.form("input_form"):
    cv_file = st.file_uploader("Upload your CV (PDF)", type=["pdf"])
    linkedin_url = st.text_input("Enter your LinkedIn URL")
    option = st.selectbox("Choose an option", ["Question", "Cover Letter"])
    user_input = st.text_area("Enter your question or cover letter details")
    submit_button = st.form_submit_button("Submit")

# Validation and response placeholder
if submit_button:
    if cv_file is None or not linkedin_url or not user_input:
        st.error("Please fill out all fields before submitting.")
    else:
        st.subheader("Generated Response")
        st.write("Response will be displayed here.")
