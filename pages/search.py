"""
This module contains DuckDuckGoSearchPage,
the page object for the DuckDuckGo search page.
"""

from playwright.sync_api import Page


class DuckDuckGoSearchPage:

    URL = 'https://www.duckduckgo.com'

    def __init__(self, page: Page) -> None:
        self.page = page
        self.search_button = page.get_by_label("search")
        self.search_button = page.locator('button[type=submit]')
        #searchbox_homepage > div > div > button
        self.search_input = page.locator('#searchbox_input')
    
    def load(self) -> None:
        self.page.goto(self.URL)
    
    def search(self, phrase: str) -> None:
        self.search_input.fill(phrase)
        self.search_button.click()
