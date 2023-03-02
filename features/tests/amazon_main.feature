
Feature: Amazon main page tests


  Scenario: User can see hamburger menu
    Given Open Amazon page
    Then Verify hamburger menu item



  Scenario: Footer has correct amount of links
    Given Open Amazon page
    Then Verify that footer has 42 links
    Then Verify that header has 29 links


  Scenario: Sign in page can be opened from Sign In popup
    Given Open Amazon page
    When Click Sign In from popup
    Then Verify sign page opens




