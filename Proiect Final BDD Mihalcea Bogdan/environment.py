from browser import Browser
from pages.home_page import Home_Page

def before_all(context):
    context.browser = Browser()
    context.home_page_object = Home_Page()

def after_all(context):
    context.browser.close()