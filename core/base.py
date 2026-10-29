import pytest
from playwright.sync_api import Page

class TestBase:

    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        self.page = page
        self.page.set_default_timeout(10000)
        yield