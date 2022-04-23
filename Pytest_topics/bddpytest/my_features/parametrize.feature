Feature: Parametrizing tests in Pytest BDD

  Scenario: Check variety of fruit
    Given There are 3 kinds of fruits
    When Add same kind of fruit
    Then There is same count of fruit kinds
    But If we add a different kind of fruit
    Then The count of kinds increases to 4
