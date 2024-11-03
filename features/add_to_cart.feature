Feature: Add Product to Cart

  Scenario: User adds a product to the cart from the Target homepage
    Given I open "https://www.target.com"
    When I scroll down to the "Festive favorites now trending" section
    When I click on a product's initial "Add to Cart" button
    When I click on the side window add to cart button
    When I close the side window
    Then I should see a cart total or quantity in the cart

