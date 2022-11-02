Feature: Testing scenarios on cel.ro
  Scenario: Searching a product on cel.ro homepage
    Given I am on cel.ro
    When I search for "laptop i7" and I choose DELL as manufacturer and order after descending price
    Then I get at least 3 results