from selenium.webdriver.common.keys import Keys


def set_text_and_submit(text_box, text):
    set_text(text_box, text)
    text_box.send_keys(Keys.RETURN)


def set_text(text_box, text):
    text_box.clear()
    text_box.send_keys(text)
