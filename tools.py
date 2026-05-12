from langchain.tools import tool
import requests
from bs4 import BeautifulSoup
from tavily import TavilyClient
import os
from dotenv import load_dotenv

load_dotenv()

tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

@tool
def web_search(query: str) -> str:
    """Search the web for recent and reliable information. Returns titles, URLs and snippets."""
    results = tavily.search(query=query, max_results=5)
    out = []
    for r in results['results']:
        out.append(f"Title: {r['title']}\nURL: {r['url']}\nSnippet: {r['content'][:300]}\n")
    return "\n----\n".join(out)

@tool
def scrape_url(url: str) -> str:
    """Scrape and return clean text content from a given URL."""
    try:
        resp = requests.get(
            url,
            timeout=5,  # hard 5 second timeout
            headers={"User-Agent": "Mozilla/5.0"},
            allow_redirects=True
        )
        if resp.status_code != 200:
            return f"Could not fetch URL (status {resp.status_code}). Skipping."

        soup = BeautifulSoup(resp.text, "html.parser")
        for tag in soup(["script", "style", "nav", "footer", "header", "aside"]):
            tag.decompose()

        text = soup.get_text(separator=" ", strip=True)
        return text[:2000] if text else "No readable content found."

    except requests.exceptions.Timeout:
        return "URL timed out after 5 seconds. Skipping this source."
    except requests.exceptions.ConnectionError:
        return "Could not connect to URL. Skipping this source."
    except Exception as e:
        return f"Could not scrape URL: {str(e)}"

