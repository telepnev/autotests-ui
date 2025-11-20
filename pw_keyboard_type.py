from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    registration_email = page.get_by_test_id('registration-form-email-input').locator('input')
    registration_email.focus()

    for char in "registration":
        page.keyboard.type(char, delay=100)

    page.keyboard.press("ControlOrMeta+A")
    page.keyboard.press("ControlOrMeta+C")

    registration_username = page.get_by_test_id('registration-form-username-input').locator('input')
    registration_username.focus()
    page.keyboard.press("ControlOrMeta+V")

    page.wait_for_timeout(2000)