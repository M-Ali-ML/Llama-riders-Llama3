import streamlit as st
import os
import nest_asyncio

from llm import * 

nest_asyncio.apply()

if st.secrets:
    print("secrets found")
    os.environ['TOGETHER_API_KEY'] = st.secrets["TOGETHER_API_KEY"]
    os.environ['LLAMA_CLOUD_API_KEY'] = st.secrets["LLAMA_CLOUD_API_KEY"]


# Streamlit app
st.markdown("<h1 style='text-align: center;'>ResuMate 🤵 Your AI Wingman for Job Hunting</h1>", unsafe_allow_html=True)

# Input form
with st.form("input_form"):
    cv_file = st.file_uploader("Upload your CV (PDF)", type=["pdf"])
    linkedin_file = st.file_uploader("Upload your Linkedin profile as a pdf [optional]",  type=["pdf"], help="You can create one from your linkedin profile")
    job_post_url = st.text_input("Enter job post URL")
    option = st.selectbox("Choose an option", ["Question", "Cover Letter"])
    user_input = st.text_area("Enter your question, if applicable", )
    submit_button = st.form_submit_button("Submit")

# Validation and response placeholder
if submit_button:
    if cv_file is None or not job_post_url:
        st.error("Please fill the required fields before submitting.")
    else:
        st.subheader("Generated Response")

        # LLM
        job_post_parsed = webscrape_url(job_post_url)
        if linkedin_file:
            linkedin_parse = process_uploaded_file(linkedin_file)
        else:
            linkedin_parse = None
        
        cv_parsed = process_uploaded_file(cv_file)
        user_context = llm_agent_KIE(CV=cv_parsed, linkedin=linkedin_parse, job_details=job_post_parsed, max_tokens=4096, temperature=0.1, stream=False)
        if option == "Question":
            result = llm_agent_question(context=user_context, question=user_input, max_tokens=4096, temperature=0.3, stream=True)
        else:
            result = llm_agent_cover(context=user_context, question=None, max_tokens=4096, temperature=0.3, stream=True)
        st.write_stream(result)
