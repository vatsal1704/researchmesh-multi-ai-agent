from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from tools import web_search, scrape_url
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.3
)

def build_search_agent():
    return create_react_agent(llm, [web_search])

def build_reader_agent():
    return create_react_agent(llm, [scrape_url])

writer_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert research writer. Write clear, structured and insightful reports."),
    ("human", """Write a detailed research report on the topic below.
Topic: {topic}
Research Gathered:
{research}
Structure: Introduction, Key Findings, Conclusion, Sources."""),
])
writer_chain = writer_prompt | llm | StrOutputParser()

critic_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a sharp and constructive research critic."),
    ("human", """Review this report and respond in this exact format:
Score: X/10
Strengths:
- ...
Areas to Improve:
- ...
One line verdict: ...

Report:
{report}"""),
])
critic_chain = critic_prompt | llm | StrOutputParser()
