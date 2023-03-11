Feature: Google search
    As a user
    I want to be able to search for keywords
    So that I can find relevant results

  Scenario: Search for a keyword
    Given I am on the Google homepage
    When I enter "Behave" into the search bar
    And I click the search button
    Then I should see search results for "Behave"
