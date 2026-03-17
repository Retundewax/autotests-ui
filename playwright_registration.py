from playwright.sync_api import sync_playwright, expect

d = {
    'url': 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration',
    'regEmailInput': 'user.name@gmail.com',
    'regUsernameInput': 'username',
    'regPasswordInput': 'password',
}

with sync_playwright() as pl:
    chrom = pl.chromium.launch(headless=False)
    page = chrom.new_page()
    page.goto(
        d["url"]
        # ,wait_until='networkidle' #Код не выполняется, вынужден использовать 18-ю строку с явным ожиданием элемента
    )
    regEmail = page.get_by_test_id('registration-form-email-input').locator('//input') #полный локатор //div[@data-testid="registration-form-email-input"]//input
    expect(regEmail, 5000).to_be_visible()
    regEmail.fill(d["regEmailInput"])
    regUsername = page.get_by_test_id('registration-form-username-input').locator('//input')
    regUsername.fill(d['regUsernameInput'])
    regPassword = page.get_by_test_id('registration-form-password-input').locator('//input')
    regPassword.fill(d['regPasswordInput'])
    regButton = page.get_by_test_id('registration-page-registration-button')
    regButton.click()
    headerDashboard = page.get_by_test_id('dashboard-toolbar-title-text')
    expect(headerDashboard, 5000).to_be_visible()
    # assert headerDashboard.text_content() == 'Dashboard'
    expect(headerDashboard).to_have_text('Dashboard')
    page.wait_for_timeout(3000)


