from selene import by, be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s
import allure

def test_github_issue():
    with allure.step('Open browser'):
        browser.open('https://github.com')

    with allure.step('Search repo'):
        s('.header-search-button').click()
        s('#query-builder-test').send_keys('eroshenkoam/allure-example')
        s('#query-builder-test').submit()

    with allure.step('Go to link of repo'):
        s(by.link_text('eroshenkoam/allure-example')).click()

    with allure.step('Open issue'):
        s('#issues-tab').click()

    with allure.step('Check number 76 of issue'):
        s(by.partial_text('#76')).should(be.visible)
