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


#Lana's example of HM 5, number 3
  Scenario: Verify that user can see product names and images
    Given Open Amazon page
    When Input text coffee
    And Click on search button
    Then Verify that every product has a name and an image

