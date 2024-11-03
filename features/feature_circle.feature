Feature: Verify Target Circle benefits

  Scenario: User opens Target Circle page and verifies there are 10 benefit cells
    Given I open "https://www.target.com/circle"
    When I check the benefit cells
    Then I should see 10 benefit cells
