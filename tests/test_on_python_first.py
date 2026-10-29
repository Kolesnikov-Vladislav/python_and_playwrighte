import allure
from core.base import TestBase

@allure.epic("Веб-интерфейс")
@allure.feature("Авторизация")
class TestFirstTestOnPython(TestBase):

    @allure.story("Успешный вход")
    @allure.title("Проверка успешного входа в систему")
    def test_first_test(self):
        with allure.step("Открыть страницу"):
            self.page.goto('/sign-in')
        with allure.step("Проверить логин"):
            self.page.locator("input[name='email']").wait_for(state="visible")
        with allure.step("Указать логин"):
            self.page.fill("input[name='email']", "email")
        with allure.step("Проверить пароль"):
            self.page.locator("input[name='email']").wait_for(state="visible")
        with allure.step("Указать пароль"):
            self.page.fill("input[name='password']", "password")
        with allure.step("Проверить чек-бокс"):
            self.page.locator("input[name='confirm']").wait_for(state="visible")
        with allure.step("Установить чек-бокс в true"):
            self.page.locator("input[name='confirm']").click()

    def test_2_test(self):
        self.page.goto('/sign-in')
        self.page.locator("input[name='email']").wait_for(state="visible")
        self.page.fill("input[name='email']", "email")
        self.page.locator("input[name='email']").wait_for(state="visible")
        self.page.fill("input[name='password']", "password")
        self.page.locator("input[name='confirm']").wait_for(state="visible")
        self.page.locator("input[name='confirm']").click()

    def test_3_test(self):
        self.page.goto('/sign-in')
        self.page.locator("input[name='email']").wait_for(state="visible")
        self.page.fill("input[name='email']", "email")
        self.page.locator("input[name='email']").wait_for(state="visible")
        self.page.fill("input[name='password']", "password")
        self.page.locator("input[name='confirm']").wait_for(state="visible")
        self.page.locator("input[name='confirm']").click()

    def test_no_first_test(self):
        with allure.step("Открыть страницу"):
            self.page.goto('/sign-in')
        with allure.step("Проверить логин"):
            self.page.locator("input[name='email']").wait_for(state="visible")
        with allure.step("Указать логин"):
            self.page.fill("input[name='email']", "email")
        with allure.step("Проверить пароль"):
            self.page.locator("input[name='email']").wait_for(state="visible")
        with allure.step("Указать пароль"):
            self.page.fill("input[name='password']", "password")
        with allure.step("Проверить чек-бокс"):
            self.page.locator("input[name='confirm']").wait_for(state="visible")
        with allure.step("Установить чек-бокс в true"):
            self.page.locator("input[name='confirm']").click()

