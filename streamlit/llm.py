import os
from together import Together
from dotenv import load_dotenv
from llama_parse import LlamaParse
from llama_index.core import SimpleDirectoryReader
import nest_asyncio
import glob
import requests
import re
from llama_index.llms.together import TogetherLLM
from llama_index.core.llms import ChatMessage
import streamlit as st
import tempfile





@st.cache_data
def webscrape_url(url):
    url = url.replace("https://", "")
    response = requests.get("https://r.jina.ai/" + url)
    return response.text

@st.cache_resource
def process_uploaded_file(uploaded_file):
    parser = LlamaParse(result_type="markdown")
    file_extractor = {".pdf": parser}

    with tempfile.TemporaryDirectory() as temp_dir:
        temp_file_path = os.path.join(temp_dir, uploaded_file.name)
        with open(temp_file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        pdf = SimpleDirectoryReader(input_files=[temp_file_path], file_extractor=file_extractor).load_data()
        parsed_pdf = '\n\n'.join([page.text for page in pdf])
    return parsed_pdf



def llm_agent_KIE(CV=None, linkedin=None, job_details=None, max_tokens=4096, temperature=0.1, stream=False, ):

    llm = TogetherLLM(model=f"meta-llama/Meta-Llama-3-8B-Instruct-Turbo",
            api_key=os.environ.get('TOGETHER_API_KEY'),
            max_tokens=max_tokens,
            temperature=temperature,
            repetition_penalty=1,
            stop=["<|eot_id|>"],
            stream=stream
            )

    messages = [
        ChatMessage(
            role="system", content="""You are an AI assitance that extract key information from user CV, lindedin profile and job post 
            and only output the results in multiple unique bullet points.
            Make sure to also extract name of the user."""
        ),
        ChatMessage(
            role="user", content=f"""
    CV : {CV}
    Linkedin: {linkedin}
    Job details: {job_details}
    """),
    ]

    resp = llm.chat(messages)
    return resp.message.content

def llm_agent_question(context=None, question=None, max_tokens=4096, temperature=0.2, stream=True):

    llm = TogetherLLM(model=f"meta-llama/Meta-Llama-3-70B-Instruct-Turbo",
            api_key=os.environ.get('TOGETHER_API_KEY'),
            max_tokens=max_tokens,
            temperature=temperature,
            repetition_penalty=1,
            stop=["<|eot_id|>"],
            stream=stream
            )

    messages = [
    ChatMessage(
        role="system", content=f"""You are an AI assitance that answer job related questions based on 
        context provided which include key informtation of user CV, linkedin profile and job. Answer in a formal way and
        don't mention the source of your information.
        context = {context}
        """
    ),
    ChatMessage(role="user", content=f"""qestion: {question}
                Answer: """),
]


    resp = llm.stream_chat(messages)
    for r in resp:
        yield r.delta


def llm_agent_cover(context=None, question=None, max_tokens=4096, temperature=0.2, stream=True):

    llm = TogetherLLM(model=f"meta-llama/Meta-Llama-3-70B-Instruct-Turbo",
            api_key=os.environ.get('TOGETHER_API_KEY'),
            max_tokens=max_tokens,
            temperature=temperature,
            repetition_penalty=1,
            stop=["<|eot_id|>"],
            stream=stream
            )

    messages = f"""You are an AI assitance that writes a cover letter based on 
            context provided which include key informtation of user CV, linkedin profile and
            job details.
            Answer in a formal and clear way and don't mention source of information.
            Use the name provided in context for the cover letter signing off.
            context = {context}
            cover letter:

            """


    resp = llm.stream_complete(messages)
    for r in resp:
        yield r.delta





# https://github.com/run-llama/llama_index/discussions/11946