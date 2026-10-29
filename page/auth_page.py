from playwright.sync_api import Page


class AuthPage(Page):

    def input_login_visible(self):
        return self.page.locator("input[name='email']").wait_for(state="visible")

    def input_login_value(self, value):
        return self.page.locator("input[name='email']").wait_for(state="visible")

    def input_password_visible(self):
        return self.page.locator("input[name='password']").wait_for(state="visible")

    def input_password_value(self, value):
        return self.page.locator("input[name='password']").wait_for(state="visible")

    def check_box_confirm_visible(self):
        return self.page.locator("input[name='confirm']").wait_for(state="visible")

    def check_box_confirm_click(self):
        return self.page.locator("input[name='confirm']").wait_for(state="visible")
