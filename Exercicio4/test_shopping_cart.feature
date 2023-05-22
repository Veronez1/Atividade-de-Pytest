Feature: Shopping Cart
    As a customer
    I want to add items to my shopping cart
    So that I can purchase them later

Scenario: Add item to shopping cart
    Given I am on the product page
    When I click the "Add to Cart" button
    Then the item is added to my shopping cart
