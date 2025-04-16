# crew/run_cognops_crew.py

from retriever.retriever_agent import run_retriever
from analyzer.analyzer_agent import run_analyzer
from planner.planner_agent import run_planner
from reporter.reporter_agent import run_reporter


def run_cognops_crew(query: str):
    """
    Runs the full CognOps agent pipeline in sequence:
    Retriever -> Analyzer -> Planner -> Reporter
    """
    retrieval_output = run_retriever(query)
    analyzer_output = run_analyzer(query, retrieval_output)
    planner_output = run_planner(analyzer_output)
    reporter_output = run_reporter(analyzer_output, planner_output)

    return {
        "retriever": retrieval_output,
        "analyzer": analyzer_output,
        "planner": planner_output,
        "reporter": reporter_output
    }
