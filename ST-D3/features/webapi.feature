Feature: Quran API Tests

  Scenario: Get all surahs
    Given I send a GET request to "/api/v3/chapters"
    Then the response status code should be 200
    And the response should contain a list of surahs

  Scenario: Retrieve contents of a single surah
    Given I send a GET request to "/api/v3/chapters/1"
    Then the response status code should be 200
    And the response should contain the details of surah 1

  Scenario: Search for a surah by name
    Given I send a GET request to "/api/v3/search" with query parameter "q=al-fatiha&size=1"
    Then the response status code should be 200
    And the response should contain the surah with the matching name "Al-Fātiḥah"
