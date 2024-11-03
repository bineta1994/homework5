Feature: Verify Sign In functionality on Target.com

  Scenario: Logged out user navigates to Sign In page
    Given I open "https://www.target.com"
    When I click on "Sign In"
    And I click on the "Sign In" option from the right-side navigation menu
    Then the Sign In form should be displayed
    Then close the browser
