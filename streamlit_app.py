# CognOps/streamlit_app.py

import streamlit as st
from dotenv import load_dotenv
import os
import requests
from retriever.retriever_agent import run_retriever
from analyzer.analyzer_agent import run_analyzer
from planner.planner_agent import run_planner
from reporter.reporter_agent import run_reporter
from crew.run_cognops_crew import run_cognops_crew
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

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

if st.button("Preview Selected Incident"):
    st.code(query, language="text")

# Run the CognOps crew end-to-end
if st.button("Run CognOps Crew (All Agents)"):
    with st.spinner("Running full agent pipeline..."):
        result = run_cognops_crew(query)
        st.success("CognOps Agent Output")
        st.json(result)

# Individual agent buttons
st.markdown("---")
st.caption("Agents powered by CrewAI: Retriever → Analyzer → Planner → Reporter")

if st.button("Run Retriever Agent"):
    with st.spinner("Running Retriever..."):
        result = run_retriever(query)
        st.success("Retriever Output")
        st.json(result)

if st.button("Run Analyzer Agent"):
    with st.spinner("Running Analyzer..."):
        result = run_analyzer(query)
        st.success("Analyzer Output")
        st.json(result)

if st.button("Run Planner Agent"):
    with st.spinner("Running Planner..."):
        result = run_planner(query)
        st.success("Planner Output")
        st.json(result)

if st.button("Run Reporter Agent"):
    with st.spinner("Running Reporter..."):
        result = run_reporter(query)
        st.success("Reporter Output")
        st.json(result)
