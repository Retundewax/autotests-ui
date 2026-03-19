from playwright.sync_api import sync_playwright, expect

with sync_playwright() as pl:
    chrom = pl.chromium.launch(headless=False)
    page = chrom.new_page()
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
    regEmail = page.locator('//div[@data-testid="registration-form-email-input"]//input')
    regButton = page.locator('//button[@data-testid="registration-page-registration-button"]')
    regButton.is_disabled()
    regEmail.fill('user.name@gmail.com')
    regUsername = page.locator('//div[@data-testid="registration-form-username-input"]//input')
    regUsername.fill('username')
    regPassword = page.locator('//div[@data-testid="registration-form-password-input"]//input')
    regPassword.fill('password')
    regButton.is_enabled()



