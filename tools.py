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
    """Search the web for information on a topic. Returns titles, URLs and snippets."""
    results = tavily.search(query=query, max_results=3)  # only 3 results
    out = []
    for r in results['results']:
        out.append(
            f"Title: {r['title']}\nURL: {r['url']}\nSnippet: {r['content'][:150]}\n"  # 150 chars only
        )
    return "\n----\n".join(out)

@tool
def scrape_url(url: str) -> str:
    """Scrape clean text from a URL."""
    try:
        resp = requests.get(
            url,
            timeout=5,
            headers={"User-Agent": "Mozilla/5.0"},
            allow_redirects=True
        )
        if resp.status_code != 200:
            return f"Could not fetch URL (status {resp.status_code})."

        soup = BeautifulSoup(resp.text, "html.parser")
        for tag in soup(["script", "style", "nav", "footer", "header", "aside"]):
            tag.decompose()

        text = soup.get_text(separator=" ", strip=True)
        return text[:1500] if text else "No readable content found."  # 1500 chars max

    except requests.exceptions.Timeout:
        return "URL timed out. Skipping."
    except requests.exceptions.ConnectionError:
        return "Could not connect. Skipping."
    except Exception as e:
        return f"Error: {str(e)}"
