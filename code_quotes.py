import json
import requests
from rich import print
from rich.panel import Panel
from rich.style import Style
from rich.text import Text
from rich.align import Align
from rich.console import Group, Console
from rich.status import Status
from random import randint
from typing import TypedDict


QUOTE_API_ENDPOINT = "https://programming-quotes-api.herokuapp.com/quotes/random"


class Quote(TypedDict):
    """
    Type definition for the quote dictionary that comes back from the API
    """

    id: str
    author: str
    en: str


def get_random_quote(url: str) -> Quote:
    """
    Fetches a quote from the programming quote API
    """
    response = requests.get(url)
    try:
        quote: Quote = json.loads(response.content)
    except:
        quote: Quote = {
            "id": "",
            "en": "Quotes could not be loaded",
            "author": "Nobody",
        }

    return quote


def renderQuote(quote: Quote):
    """
    renders a quote and author using rich Group and Text
    """
    quote_text = quote["en"]
    author_text = quote["author"]
    textStyle = Style(color="#FFFFFF")
    return Group(
        Text(
            text=quote_text,
            justify="left",
            style=textStyle,
        ),
        Text(
            text=f"-- {author_text}",
            justify="right",
            style=textStyle,
        ),
    )


def main():
    """
    Main entry point
    """
    console = Console()
    console.clear()

    status = Status("Fetching Quote...")
    status.start()
    random_quote = get_random_quote(QUOTE_API_ENDPOINT)
    status.stop()

    print(
        Align(
            align="center",
            renderable=Panel(
                renderable=renderQuote(random_quote),
                style=Style(color="cyan"),
                width=79,
                expand=False,
            ),
        )
    )


if __name__ == "__main__":
    main()
