from pytest_bdd import given, when, then, scenarios

scenarios('test_shopping_cart.feature')


@given('I am on the product page')
def product_page():
    pass


@when('I click the "Add to Cart" button')
def add_to_cart():
    pass


@then('the item is added to my shopping cart')
def verify_cart():
    pass
