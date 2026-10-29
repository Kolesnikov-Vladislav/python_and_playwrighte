import allure
import pytest
from pathlib import Path
from playwright.sync_api import sync_playwright, Page, BrowserContext, Browser


@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as pw:
        yield pw


@pytest.fixture(scope="session")
def browser(playwright_instance):
    browser = playwright_instance.chromium.launch(headless=True)
    yield browser
    browser.close()


@pytest.fixture(scope="function")
def context(browser: Browser):
    context = browser.new_context()
    yield context
    context.close()


@pytest.fixture(scope="function")
def page(context: BrowserContext) -> Page:
    page = context.new_page()
    yield page
    page.close()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Выполняем хук, чтобы получить результат теста
    outcome = yield
    rep = outcome.get_result()

    # Действуем только если тест упал (на этапе вызова)
    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page")  # Получаем объект страницы из фикстур

        if page:
            # 1. Прикрепляем скриншот
            allure.attach(
                page.screenshot(),
                name="Скриншот при падении",
                attachment_type=allure.attachment_type.PNG,
            )

            # 2. Прикрепляем видео, если оно есть
            video_path = page.video.path() if page.video else None
            if video_path and Path(video_path).exists():
                allure.attach.file(
                    video_path,
                    name="Видео при падении",
                    attachment_type=allure.attachment_type.WEBM,
                )