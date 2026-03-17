from playwright.sync_api import sync_playwright, expect

d = {
    'url': 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration',
    'regEmailInput': 'user.name@gmail.com',
    'regUsernameInput': 'username',
    'regPasswordInput': 'password',
    'regEmailLocator': '//div[@data-testid="registration-form-email-input"]//input',
    'regButtonLocator': '//button[@data-testid="registration-page-registration-button"]',
    'regUsernameLocator': '//div[@data-testid="registration-form-username-input"]//input',
    'regPasswordLocator': '//div[@data-testid="registration-form-password-input"]//input'
}

with sync_playwright() as pl:
    chrom = pl.chromium.launch(headless=False)
    page = chrom.new_page()
    page.goto(
        d['url']
        # , wait_until='networkidle'
    )
    regEmail = page.locator(d['regEmailLocator'])
    expect(regEmail, 5000).to_be_visible()
    regButton = page.locator(d['regButtonLocator'])
    regButton.is_disabled()
    regEmail.fill(d['regEmailInput'])
    regUsername = page.locator(d['regUsernameLocator'])
    regUsername.fill(d['regUsernameInput'])
    regPassword = page.locator(d['regPasswordLocator'])
    regPassword.fill(d['regPasswordInput'])
    regButton.is_enabled()

    page.wait_for_timeout(3000)


