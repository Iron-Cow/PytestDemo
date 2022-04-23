Feature: Fixtures and BDD background on Python Set DataType

  # background can have only given statements. We can setup tests before scenariou
  Background: Setting up data for test
    Given A data type set
    And The set is not empty

  Scenario: Adding to Set
    Given A sent with 3 elements
    When Add 2 elents to the set
    Then The set should have 5 elements