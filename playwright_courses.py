from playwright.sync_api import sync_playwright, expect

with sync_playwright() as pl:
    chrom = pl.chromium.launch(headless=False)
    context = chrom.new_context()
    page = context.new_page()
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    emailInput = page.get_by_test_id('registration-form-email-input').locator('input')
    emailInput.fill('user.name@gmail.com')

    usernameInput = page.get_by_test_id('registration-form-username-input').locator('input')
    usernameInput.fill('username')

    passwordInput = page.get_by_test_id('registration-form-password-input').locator('input')
    passwordInput.fill('password')

    registrationButton = page.get_by_test_id('registration-page-registration-button')
    registrationButton.click()
    context.storage_state(path='browser-state.json')


with sync_playwright() as pl:
    chrom = pl.chromium.launch(headless=False)
    context = chrom.new_context(storage_state='browser-state.json')
    page = context.new_page()
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

    coursesHeader = page.get_by_test_id('courses-list-toolbar-title-text')
    expect(coursesHeader).to_have_text('Courses')

    folderIcon = page.get_by_test_id('courses-list-empty-view-icon')
    expect(folderIcon).to_be_visible()

    resultHeader = page.get_by_test_id('courses-list-empty-view-title-text')
    expect(resultHeader).to_have_text('There is no results')

    descriptionLine = page.get_by_test_id('courses-list-empty-view-description-text')
    expect(descriptionLine).to_have_text('Results from the load test pipeline will be displayed here')
