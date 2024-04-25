import urllib
from urllib.parse import urljoin
from behave import given, when, then

@given( "we want to add a product")
def user_on_product_newpage(context):
    base_url = 'http://localhost:8000/'
    open_url = urljoin(base_url,'/product_new/')
    context.browser.get(open_url)

@when( "we fill in the form")
def user_fills_in_the_form(context):
    name_textfield = context.browser.find_element('name', 'name')
    name_textfield.send_keys('stanwell pipe')
    price_textfield = context.browser.find_element('name','price')
    price_textfield.send_keys(3)
    context.browser.find_element('name','submit').click()

@then( "it succeeds")
def product_added(context):
    assert 'stanwell pipe' in context.browser.page_source

@given(u'we have specific products to add')
def specific_products(context):
    base_url = 'http://localhost:8000/'
    open_url = urljoin(base_url,'/product_new/')
    for row in context.table:
        context.browser.get(open_url)
        name_textfield = context.browser.find_element('name', 'name')
        name_textfield.send_keys(row['name'])
        price_textfield = context.browser.find_element('name','price')
        price_textfield.send_keys(row['price'])
        context.browser.find_element('name','submit').click()
        assert row['name'] in context.browser.page_source
       
@when(u'we visit the listing page')
def step_impl(context):
    base_url = 'http://localhost:8000/'
    open_url = urljoin(base_url,'/product_list')
    context.browser.get(open_url)
    assert 'Product List' in context.browser.page_source

@then(u'we will find \'stanwell pipe\'')
def step_impl(context):
    base_url = 'http://localhost:8000/'
    open_url = urljoin(base_url,'/product_list/?page=999')
    context.browser.get(open_url)
    assert 'stanwell pipe' in context.browser.page_source