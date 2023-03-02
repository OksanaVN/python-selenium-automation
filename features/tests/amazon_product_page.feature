Feature: Tests for product page


  Scenario: User can select colors
    Given Open Amazon product B08JHKQPBV page
    Then Verify user can click through colors

#Homework 5, number 2
  Scenario: User can select jeans colors
    Given Open Amazon product B07BJKRR25 page
    Then Verify user can click through jeans colors

#Just trying number 3 from homework 5, not sure if that's correct
  Scenario: Verify every product on amazon search page has an image
    Given Open Amazon page
    When Input text mug
    And Click on search button
    Then Verify every product has an image
    And Verify every product has a name