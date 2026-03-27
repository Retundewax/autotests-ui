from playwright.sync_api import sync_playwright, expect

with sync_playwright() as pl:
    chrom = pl.chromium.launch(headless=False)
    page = chrom.new_page()
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
    emailInput = page.get_by_test_id('registration-form-email-input').locator('input')
    emailInput.fill('user.name@gmail.com')
    usernameInput = page.get_by_test_id('registration-form-username-input').locator('input')
    usernameInput.fill('username')
    passwordInput = page.get_by_test_id('registration-form-password-input').locator('input')
    passwordInput.fill('password')
    registrationButton = page.get_by_test_id('registration-page-registration-button')
    registrationButton.click()
    headerDashboard = page.get_by_test_id('dashboard-toolbar-title-text')
    expect(headerDashboard).to_have_text('Dashboard')

