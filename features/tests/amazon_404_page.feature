Feature: Test for 404 page

  Scenario: User is able to navigate to amazon blog page from 404 page
    Given Open Amazon product B08JHKQPBV1111111111 page
    And Store original window
    When Click on a dog image
    And Switch to new window
    Then Verify blog is opened
    And Close blog
    And Return to original window
