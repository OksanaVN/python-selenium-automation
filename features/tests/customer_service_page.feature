
Feature: Verify Customer Service Page UI elements

#I see the second version of the UI
  Scenario: Verify Customer Service UI elements
    Given Open Amazon page
    When Click on Customer Service
    Then Verify Customer Service Header contains 3 links
    Then Verify Customer Service Header contain Customer Service Link
    Then Verify Customer Service Header contains Home Link
    Then Verify Customer Service Header contains Digital Services and Device Support link
    Then Verify Welcome to Amazon Customer Service Header
