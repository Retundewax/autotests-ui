from playwright.sync_api import sync_playwright, expect

with sync_playwright() as pl:
    chrom = pl.chromium.launch(headless=False)
    page = chrom.new_page()
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
    regEmail = page.get_by_test_id('registration-form-email-input').locator('input')
    regEmail.fill('user.name@gmail.com')
    regUsername = page.get_by_test_id('registration-form-username-input').locator('input')
    regUsername.fill('username')
    regPassword = page.get_by_test_id('registration-form-password-input').locator('input')
    regPassword.fill('password')
    regButton = page.get_by_test_id('registration-page-registration-button')
    regButton.click()
    headerDashboard = page.get_by_test_id('dashboard-toolbar-title-text')
    expect(headerDashboard, 5000).to_be_visible()
    expect(headerDashboard).to_have_text('Dashboard')

