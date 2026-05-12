# ResearchMind
### Distributed Multi-Agent Research Architecture

ResearchMind is an advanced multi-agent AI research system built using LangChain, LangGraph, Streamlit, and Tavily.

The platform orchestrates multiple specialized AI agents that collaboratively perform:

- Real-time web research
- Deep content extraction
- Research synthesis
- AI-powered report generation
- Report critique & refinement

The system simulates a distributed AI research workflow where each autonomous agent handles a specific responsibility inside the pipeline.

---

# Features

- Multi-agent AI architecture
- Real-time web search using Tavily API
- Deep webpage scraping with BeautifulSoup
- AI-generated research reports
- Critic agent for report refinement
- Interactive Streamlit interface
- Modular & scalable architecture
- Production-ready deployment workflow

---
## 🚀 Live Demo

[[Live Demo](https://multi-ai-agent-fpckoqokwamnby2hmgoaon.streamlit.app/)


# Architecture Overview

ResearchMind follows a distributed agent workflow:

<img width="1536" height="1024" alt="ChatGPT Image May 6, 2026, 02_44_12 PM" src="https://github.com/user-attachments/assets/43983241-4c01-42b4-894c-44d0071ce513" />


---

# Agent Pipeline

## 1. Search Agent

Responsible for:
- Searching live web data
- Finding relevant sources
- Gathering research references

### Tools Used
- Tavily Search API

---

## 2. Reader Agent

Responsible for:
- Scraping webpages
- Extracting structured content
- Cleaning article text

### Tools Used
- BeautifulSoup
- Requests

---

## 3. Writer Chain

Responsible for:
- Synthesizing research information
- Structuring detailed reports
- Generating high-quality summaries

### Technologies
- LangChain
- LLM Reasoning Chains

---

## 4. Critic Chain

Responsible for:
- Reviewing generated reports
- Improving coherence
- Enhancing factual quality
- Evaluating research completeness

---

# Tech Stack

| Category | Technologies |
|---|---|
| Frontend | Streamlit |
| AI Framework | LangChain |
| Workflow Orchestration | LangGraph |
| Search Engine | Tavily API |
| LLM Provider | Groq / Gemini |
| Scraping | BeautifulSoup |
| Backend Language | Python |
| Deployment | Streamlit Cloud |
| Version Control | Git & GitHub |

---

# Screenshots

## Landing Page

<img width="1920" height="862" alt="Screenshot (406)" src="https://github.com/user-attachments/assets/e97a6aa7-f5b7-4d11-9de8-ea66a21c361f" />


---

## Multi-Agent Pipeline

<img width="1920" height="831" alt="Screenshot (407)" src="https://github.com/user-attachments/assets/e2501114-9c44-4a9b-9f39-6f3e2dc3c288" />


---

# Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/researchmind.git
cd researchmind
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Mac/Linux

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file:

```env
TAVILY_API_KEY=your_tavily_key
GROQ_API_KEY=your_groq_key
```

---

# Run Application

```bash
streamlit run app.py
```

---

# Deployment

This project can be deployed easily using:

- Streamlit Cloud
- Render
- Railway
- HuggingFace Spaces

### Streamlit Deployment Steps

1. Push project to GitHub
2. Connect repository to Streamlit Cloud
3. Add API keys inside Streamlit Secrets
4. Deploy instantly

---

# Project Structure

```text
researchmind/
│
├── app.py
├── agents.py
├── tools.py
├── requirements.txt
├── README.md
├── .env
└── utils/
```

---

# Future Improvements

- Memory-enabled AI agents
- Vector database integration
- PDF report export
- Multi-modal research support
- Autonomous planning agents
- Citation generation
- Async agent execution
- Voice-powered research assistant

---

# Example Research Topics

- LLM Agents in 2026
- Quantum Computing Breakthroughs
- CRISPR Gene Editing
- Fusion Energy Progress
- AI Infrastructure Trends

---



### ResearchMind
Distributed Multi-Agent Research Architecture
