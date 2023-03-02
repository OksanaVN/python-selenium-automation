
Feature: Verify Customer Service Page UI elements

#I see the second version of the UI
  Scenario: Verify Customer Service UI elements
    Given Open Amazon page
    When Click on Customer Service
    Then Verify Customer Service Header contains 3 links
    And Verify Customer Service Header contain Customer Service Link
    And Verify Customer Service Header contains Home Link
    And Verify Customer Service Header contains Digital Services and Device Support link
    And Verify Welcome to Amazon Customer Service Header
    And Verify What would you like help with today message displayed
    #Sometimes there are 9 cards, sometimes 10
    And Verify Welcome to Amazon section contain 10 cards
    And Verify Search our help library header
    And Verify Library search input field