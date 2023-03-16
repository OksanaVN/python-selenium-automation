
Feature: Best Sellers Page

#Home Work 4
  Scenario: Verify Best Sellers Page contains 5 links
    Given Open Amazon page
    When Click on Best Sellers
    Then Verify Best Seller has 5 links


  Scenario: Bestsellers link can be opened
    Given Open Amazon page
    When Click on Best Sellers
    Then User can click on every link and verify correct page opens

