from playwright.sync_api import expect, Page
import pytest

@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state: Page):
    courses_header = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
    expect(courses_header).to_have_text('Courses')

    folder_icon = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
    expect(folder_icon).to_be_visible()

    result_header = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
    expect(result_header).to_have_text('There is no results')

    description_line = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')
    expect(description_line).to_have_text('Results from the load test pipeline will be displayed here')

