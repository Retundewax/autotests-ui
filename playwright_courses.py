from playwright.sync_api import sync_playwright, expect

d1 = {
    'url1': 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration',
    'regEmailInput': 'user.name@gmail.com',
    'regUsernameInput': 'username',
    'regPasswordInput': 'password',
    'regEmailLocator': '//div[@data-testid="registration-form-email-input"]//input',
    'regButtonLocator': '//button[@data-testid="registration-page-registration-button"]',
    'regUsernameLocator': '//div[@data-testid="registration-form-username-input"]//input',
    'regPasswordLocator': '//div[@data-testid="registration-form-password-input"]//input'
}
d2 = {
    'url': 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses',
    'coursesTestId': 'courses-list-toolbar-title-text',
    'iconTestId': 'courses-list-empty-view-icon',
    'noResultsTestId': 'courses-list-empty-view-title-text',
    'descriptionLineTestId': 'courses-list-empty-view-description-text',
    'coursesText': 'Courses',
    'noResultsText': 'There is no results',
    'descriptionLineText': 'Results from the load test pipeline will be displayed here',
}

with sync_playwright() as pl:
    chrom = pl.chromium.launch(headless=False)
    context = chrom.new_context()
    page = context.new_page()
    page.goto(
        d1['url1']
        # , wait_until='networkidle'
    )
    regEmail = page.locator(d1['regEmailLocator'])
    expect(regEmail, 5000).to_be_visible()
    regEmail.fill(d1['regEmailInput'])
    regUsername = page.locator(d1['regUsernameLocator'])
    regUsername.fill(d1['regUsernameInput'])
    regPassword = page.locator(d1['regPasswordLocator'])
    regPassword.fill(d1['regPasswordInput'])
    regButton = page.locator(d1['regButtonLocator'])
    regButton.click()
    context.storage_state(path='browser-state.json')

    page.wait_for_timeout(3000)


with sync_playwright() as pl:
    chrom = pl.chromium.launch(headless=False)
    context = chrom.new_context(storage_state='browser-state.json')
    page = context.new_page()
    page.goto(d2['url'])
    courses = page.get_by_test_id(d2['coursesTestId'])
    icon = page.get_by_test_id(d2['iconTestId'])
    noResults = page.get_by_test_id(d2['noResultsTestId'])
    descriptionLine = page.get_by_test_id(d2['descriptionLineTestId'])
    expect(courses).to_have_text(d2['coursesText'])
    expect(noResults).to_have_text(d2['noResultsText'])
    expect(icon).to_be_visible()
    expect(descriptionLine).to_have_text(d2['descriptionLineText'])

    page.wait_for_timeout(3000)


