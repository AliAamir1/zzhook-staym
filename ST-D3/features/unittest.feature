Feature: Surah Model Test Cases

  Background: 
    Given I have connected to the MongoDB database

  Scenario: Get surah by number
    When I retrieve surah with number 1
    Then I should receive surah details with number 1 and name "Al-Fatihah"
    When I retrieve surah with number 999
    Then I should receive null

  Scenario: Get surah by name
    When I retrieve surah with name "Al-Fatihah"
    Then I should receive surah details with number 1 and name "Al-Fatihah"
    When I retrieve surah with name "Invalid Name"
    Then I should receive null

  Scenario: Get all surahs
    When I retrieve all surahs
    Then I should receive a list of surahs with length 2 and numbers 1 and 2

  Scenario: Create surah
    Given I have a new surah with number 3, name "Al-Imran" and English name "The Family of Imran"
    When I create the new surah
    Then I should receive the created surah with number 3 and name "Al-Imran"

  Scenario: Update surah
    Given I have an updated surah with number 1, name "New Name" and English name "The New Name"
    When I update the surah with number 1
    Then the update operation should be successful and the surah details should be updated
    When I update the surah with number 999
    Then the update operation should not be successful

  Scenario: Delete surah
    When I delete the surah with number 1
    Then the delete operation should be successful and the surah details should be deleted
    When I delete the surah with number 999
    Then the delete operation should not be successful
