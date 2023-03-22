
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


  Scenario: User can select and search in a department
    Given Open Amazon page
    When Select department by alias audible
    When Input text Faust
    When Click on search button
    Then Verify audible department is selected


  Scenario: User can select and search for computers in a department
    Given Open Amazon page
    When Select department by alias computers
    When Input text gaming computer
    When Click on search button
    Then Verify pc department is selected


