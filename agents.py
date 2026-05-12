from langgraph.prebuilt import create_react_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from tools import web_search, scrape_url
from dotenv import load_dotenv

load_dotenv()

# Main LLM - used for writer and critic (needs more tokens)
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.3,
    max_output_tokens=800  # cap output to save tokens
)

# Lightweight LLM - used for agents (tool calling only, needs less)
llm_agent = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0,
    max_output_tokens=300  # agents just need to call tools, not write essays
)

def build_search_agent():
    return create_react_agent(llm_agent, [web_search])

def build_reader_agent():
    return create_react_agent(llm_agent, [scrape_url])

writer_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a concise research writer. Write structured, factual reports."),
    ("human", """Write a research report on: {topic}

Research:
{research}

Format:
## Introduction
## Key Findings (3 points)
## Conclusion
## Sources"""),
])
writer_chain = writer_prompt | llm | StrOutputParser()

critic_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a research critic. Be brief and specific."),
    ("human", """Review this report briefly.

Score: X/10
Strengths: (2 points)
Areas to Improve: (2 points)
Verdict: (1 line)

Report:
{report}"""),
])
critic_chain = critic_prompt | llm | StrOutputParser()
