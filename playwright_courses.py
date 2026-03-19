from playwright.sync_api import sync_playwright, expect

with sync_playwright() as pl:
    chrom = pl.chromium.launch(headless=False)
    context = chrom.new_context()
    page = context.new_page()
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
    regEmail = page.locator('//div[@data-testid="registration-form-email-input"]//input')
    regEmail.fill('user.name@gmail.com')
    regUsername = page.locator('//div[@data-testid="registration-form-username-input"]//input')
    regUsername.fill('username')
    regPassword = page.locator('//div[@data-testid="registration-form-password-input"]//input')
    regPassword.fill('password')
    regButton = page.locator('//button[@data-testid="registration-page-registration-button"]')
    regButton.click()
    context.storage_state(path='browser-state.json')


with sync_playwright() as pl:
    chrom = pl.chromium.launch(headless=False)
    context = chrom.new_context(storage_state='browser-state.json')
    page = context.new_page()
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')
    courses = page.get_by_test_id('courses-list-toolbar-title-text')
    icon = page.get_by_test_id('courses-list-empty-view-icon')
    noResults = page.get_by_test_id('courses-list-empty-view-title-text')
    descriptionLine = page.get_by_test_id('courses-list-empty-view-description-text')
    expect(courses).to_have_text('Courses')
    expect(noResults).to_have_text('There is no results')
    expect(icon).to_be_visible()
    expect(descriptionLine).to_have_text('Results from the load test pipeline will be displayed here')



