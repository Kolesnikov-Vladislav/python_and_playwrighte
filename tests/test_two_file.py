import allure
from core.base import TestBase


@allure.epic("Веб-интерфейс")
@allure.feature("Авторизация")
class TestSecondTestOnPython(TestBase):
    def test_01_test(self):

        self.page.goto('https://dev1lkp.aqsi.ru')
        self.page.locator("input[name='email']").wait_for(state="visible")
        self.page.fill("input[name='email']", "email")
        self.page.locator("input[name='email']").wait_for(state="visible")
        self.page.fill("input[name='password']", "password")
        self.page.locator("input[name='confirm']").wait_for(state="visible")
        self.page.locator("input[name='confirm']").click()

    def test_02_test(self):
        self.page.goto('https://dev1lkp.aqsi.ru')
        self.page.locator("input[name='email']").wait_for(state="visible")
        self.page.fill("input[name='email']", "email")
        self.page.locator("input[name='email']").wait_for(state="visible")
        self.page.fill("input[name='password']", "password")
        self.page.locator("input[name='confirm']").wait_for(state="visible")
        self.page.locator("input[name='confirm']").click()

    def test_03_test(self):
        self.page.goto('https://dev1lkp.aqsi.ru')
        self.page.locator("input[name='email']").wait_for(state="visible")
        self.page.fill("input[name='email']", "email")
        self.page.locator("input[name='email']").wait_for(state="visible")
        self.page.fill("input[name='password']", "password")
        self.page.locator("input[name='confirm']").wait_for(state="visible")
        self.page.locator("input[name='confirm']").click()

    def test_04_test(self):
        self.page.goto('https://tech-test.aqsi.ru')
        self.page.locator("input[name='email']").wait_for(state="visible")
        self.page.fill("input[name='email']", "email")
        self.page.locator("input[name='email']").wait_for(state="visible")
        self.page.fill("input[name='password']", "password")
        self.page.locator("input[name='confirm']").wait_for(state="visible")
        self.page.locator("input[name='confirm']").click()