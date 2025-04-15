# CognOps/streamlit_app.py

import streamlit as st
from agent_clients import call_retriever_agent, call_analyzer_agent, call_planner_agent, call_reporter_agent
import os
from dotenv import load_dotenv
import requests

load_dotenv()

st.set_page_config(page_title="CognOps – AI Ops Panel", layout="wide")
st.title("CognOps – Multi-Agent GenAI Ops Panel")

# Input Section
st.subheader("Live Incident Feed")


def get_all_issues():
    owner = "kubernetes"
    repo = "kubernetes"
    url = f"https://api.github.com/repos/{owner}/{repo}/issues?state=open&per_page=100"

    headers = {
        "Accept": "application/vnd.github.v3+json"
    }

    response = requests.get(url, headers=headers)
    issue_list = []
    if response.status_code == 200:
        issues = response.json()
        for issue in issues:
            if not issue.get("pull_request"):
                title = issue['title']
                body = issue.get('body', '')
                full_text = f"{title}\n{body}"
                issue_list.append((title, full_text))
    return issue_list


all_issues = get_all_issues()
titles = [title for title, _ in all_issues]
selected_title = st.selectbox("Select an Incident", titles)
query = next(
    (full for title, full in all_issues if title == selected_title), "")

st.code(query, language="text")

with st.expander("🛠️ Advanced Options"):
    mode = st.selectbox("Retriever Mode", ["hybrid", "rag", "live"])

# Agent Panels
st.markdown("---")
st.subheader("Retriever Agent")
if st.button("Run Retriever Agent"):
    with st.spinner("Calling Retriever Agent..."):
        retriever_response = call_retriever_agent(query, mode)
        st.success("Response from Retriever Agent")
        st.json(retriever_response)

st.markdown("---")
st.subheader("Analyzer Agent")
if st.button("Run Analyzer Agent"):
    with st.spinner("Calling Analyzer Agent..."):
        analyzer_response = call_analyzer_agent(query)
        st.success("Response from Analyzer Agent")
        st.json(analyzer_response)

st.markdown("---")
st.subheader("Planner Agent")
if st.button("Run Planner Agent"):
    with st.spinner("Calling Planner Agent..."):
        planner_response = call_planner_agent(query)
        st.success("Response from Planner Agent")
        st.json(planner_response)

st.markdown("---")
st.subheader("Reporter Agent")
if st.button("Run Reporter Agent"):
    with st.spinner("Calling Reporter Agent..."):
        reporter_response = call_reporter_agent(query)
        st.success("Response from Reporter Agent")
        st.json(reporter_response)
