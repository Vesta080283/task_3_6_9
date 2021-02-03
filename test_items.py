link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"


def test_basket_button_exists(browser):
    browser.get(link)
    assert len(browser.find_elements_by_css_selector(
        '.btn-add-to-basket')) > 0, "Not found a button 'Add to basket'!"
