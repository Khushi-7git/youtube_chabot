from ddgs import DDGS
from config import MAX_SEARCH_RESULTS

def web_search(query):
    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(query, 
                          max_results=MAX_SEARCH_RESULTS))
            output = ""
            for r in results:
                output += f"Title: {r['title']}\n"
                output += f"Summary: {r['body']}\n\n"
            return output
    except Exception as e:
        return f"❌ Search error: {str(e)}"
