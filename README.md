```markdown
# CognOps – Multi-Agent GenAI Ops Panel

CognOps is a GenAI-powered multi-agent system built using [CrewAI](https://github.com/joaomdmoura/crewAI) and Streamlit.  
It simulates a real-world AI incident response team with intelligent agents that retrieve, analyze, plan, and summarize resolution steps.

---

## 🚀 Tech Stack

- [✅] Streamlit (UI)
- [✅] CrewAI (Agent Framework)
- [✅] LangChain (Prompt orchestration)
- [✅] ChromaDB (vector store for Retriever)
- [✅]Groq API (LLM Inference)

---


## Agents

| Agent     | Role                             | Output |
|-----------|----------------------------------|--------|
| Retriever | Finds similar incidents or docs  | context_snippets |
| Analyzer  | Diagnoses root cause/severity    | root_cause, symptoms |
| Planner   | Suggests remediation strategy    | steps, risk, ETA |
| Reporter  | Summarizes postmortem            | markdown summary |

---

## 🛠️ Setup Instructions

1. **Clone the Repo**
```bash
git clone https://github.com/chandrika-3367/cognops.git
cd cognops
```

2. **Set up virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Add your `.env` file**
```env
OPENAI_API_KEY=your-key
```

5. **Run the Streamlit app**
```bash
streamlit run streamlit_app.py
```

---

## ⚙️ Customization

- Modify each agent inside `retriever/`, `analyzer/`, etc.
- All CrewAI logic is managed via `crew.py`
- Streamlit UI dynamically feeds GitHub issues into the Crew pipeline

---

## Credits
- Framework: [CrewAI](https://github.com/joaomdmoura/crewAI)
- UI & UX: Streamlit

---

## 💡 Future Enhancements

- Add Slack/Email reporting
- Integrate with real PagerDuty or Prometheus
- Plug in fine-tuned models for Planner/Analyzer

---

> “CognOps isn't just automation — it's intelligent coordination.” 
```
