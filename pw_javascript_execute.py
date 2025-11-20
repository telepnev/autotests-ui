from playwright.sync_api import *

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto(
        "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login",
        wait_until='networkidle'
    )

    # 1
    # text = "Some New Text !!!!!"
    # page.evaluate(
    #     f"""
    #     const title = document.getElementById('authentication-ui-course-title-text')
    #     title.textContent = '{text}'
    #     """)

    # 2
    new_text = "New_Text"
    page.evaluate(
        """
        (text) => {
        const title = document.getElementById('authentication-ui-course-title-text')
        title.textContent = text
        }
        """, new_text
    )

    page.wait_for_timeout(2000)
