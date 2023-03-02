
Feature: Amazon Search


  Scenario Outline: User can search for a coffee on Amazon
    Given Open Amazon page
    When Input text <search_word>
    When Click on search button
    Then Verify that text <search_result> is shown
    Examples:
    |search_word |search_result |
    |coffee      |"coffee"      |
    |table       |"table"       |
    |mug         |"mug"         |


  Scenario: User can search for a shampoo on Amazon
    Given Open Amazon page
    When Input text shampoo
    When Click on search button
    Then Verify that text "shampoo" is shown


    # Created by Svetlana at 4/4/19
  Scenario: User can search for a product
    Given Open Google page
    When Input Dress into search field
    And Click on search icon
    Then Product results for Dress are shown
