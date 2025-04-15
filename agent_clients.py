import requests
import os

# Load from .env or fallback to default localhost ports
RETRIEVER_URL = os.getenv("RETRIEVER_URL", "http://localhost:8000/run")
ANALYZER_URL = os.getenv("ANALYZER_URL", "http://localhost:8001/run")
PLANNER_URL = os.getenv("PLANNER_URL", "http://localhost:8002/run")
REPORTER_URL = os.getenv("REPORTER_URL", "http://localhost:8003/run")


def call_agent(url, payload):
    try:
        response = requests.post(url, json=payload)
        return response.json()
    except Exception as e:
        return {"status": "error", "message": str(e)}


def call_retriever_agent(query, mode="hybrid"):
    return call_agent(RETRIEVER_URL, {"input": query, "mode": mode})


def call_analyzer_agent(input_data):
    return call_agent(ANALYZER_URL, {"input": input_data})


def call_planner_agent(input_data):
    return call_agent(PLANNER_URL, {"input": input_data})


def call_reporter_agent(input_data):
    return call_agent(REPORTER_URL, {"input": input_data})
