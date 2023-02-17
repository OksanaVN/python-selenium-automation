
Feature: Amazon Search


  Scenario: User can search for a product on Amazon
    Given Open Amazon page
    When Input text coffee
    When Click on search button
    Then Verify that text "coffee" is shown


  Scenario: User can search for a product on Amazon
    Given Open Amazon page
    When Input text shampoo
    When Click on search button
    Then Verify that text "shampoo" is shown
