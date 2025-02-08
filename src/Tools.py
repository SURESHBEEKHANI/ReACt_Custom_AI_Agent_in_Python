import httpx
# Action function: Wikipedia search
def wikipedia(query):
    response = httpx.get("https://en.wikipedia.org/w/api.php", params={
        "action": "query",
        "list": "search",
        "srsearch": query,
        "format": "json"
    })
    data = response.json()
    try:
        return data["query"]["search"][0]["snippet"]
    except (KeyError, IndexError):
        return "No Wikipedia results found."

# Action function: Simon Willison's blog search
def simon_blog_search(query):
    response = httpx.get("https://datasette.simonwillison.net/simonwillisonblog.json", params={
        "sql": """
        select
          blog_entry.title || ': ' || substr(html_strip_tags(blog_entry.body), 0, 1000) as text,
          blog_entry.created
        from
          blog_entry join blog_entry_fts on blog_entry.rowid = blog_entry_fts.rowid
        where
          blog_entry_fts match escape_fts(:q)
        order by
          blog_entry_fts.rank
        limit
          1
        """.strip(),
        "_shape": "array",
        "q": query,
    })
    data = response.json()
    try:
        return data[0]["text"]
    except (KeyError, IndexError):
        return "No blog post found."

# Action function: Calculate arithmetic expressions
def calculate(expression):
    try:
        # Using eval here is convenient but be cautious about security implications
        return eval(expression)
    except Exception as e:
        return f"Error evaluating expression: {e}"