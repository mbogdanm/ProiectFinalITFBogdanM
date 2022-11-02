from behave import *

@Given('I am on cel.ro')
def step_impl(context):
    context.home_page_object.test_navigate_to_home_page()

@When('I search for "laptop i7" and I choose DELL as manufacturer and order after descending price')
def step_impl(context):
    context.home_page_object.test_enter_search_criteria()
    context.home_page_object.click_search_button()
    context.home_page_object.filter_after_manufacturer()
    context.home_page_object.open_sorting_options()
    context.home_page_object.filter_after_descending_price()

@Then ('I get at least 3 results')
def step_impl(context):
    context.home_page_object.check_results()