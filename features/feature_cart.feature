Feature: Verify cart functionality on Target.com

  Scenario: User clicks on the cart icon and sees an empty cart message
    Given I open "https://www.target.com"
    When I click on the cart icon
    Then I should see the message "Your cart is empty"
    Then close the browser
