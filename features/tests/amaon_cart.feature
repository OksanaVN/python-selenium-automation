
Feature: Amazon cart tests


  Scenario: Verify Cart is empty
    Given Open Amazon page
    When Click on Cart
    Then I should see "Your Amazon Cart is empty"


   Scenario: Verify product in the cart
    Given Open Amazon page
    When Input text mug
    When Click on search button
    When Select "Ember Temperature Control Smart Mug"
    And Click on Add to Cart
    And Close Slide Window
    And Click on Cart
    Then I should see "Ember Temperature Control Smart Mug 2"




