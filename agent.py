from scraper import get_random_quote, get_author_wiki

def run_agent(query):
    query = query.lower()

    # 🧠 decision making
    if "quote" in query:
        text, author = get_random_quote()

        info = get_author_wiki(author)

        return f"""
📜 Quote:
{text}

✍️ Author:
{author}

🌍 About Author (Wikipedia):
{info}
"""

    elif "author" in query:
        name = query.replace("author", "").strip()
        info = get_author_wiki(name)

        return f"""
🌍 About {name}:
{info}
"""

    else:
        return "I can give quotes or author info 😄"