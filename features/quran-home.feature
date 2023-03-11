Feature: Exploring quran.com home page

    Scenario: Decrease  font size:
    Given setting menu is oppened
    When I click on font size - button
    Then Font size will decrease

  Scenario: word tooltip Enable transliteration
    Given on settings menu and transliteration is disabled
    When I click on the check box of transliteration
    Then transliteration will get enabled

  Scenario: word tooltip Disable translation
    Given on settings menu and translation is enabled
    When I click on the check box of translation tt
    Then translation will get deactivated tt

  Scenario: Word by word Enable transliteration
    Given on settings menu and transliteration is disabled
    When I click on the check box of transliteration
    Then transliteration will get enabled

  Scenario: word by word Disable translation
    Given on settings menu and translation is enabled
    When I click on the check box of translation wbw
    Then translation will get deactivated wbw

  Scenario: deactivate autoscroll
    Given on settings menu and autoscroll is enabled
    When I click on the auto scroll button
    Then Auto scroll will get disabled

  Scenario: click on the surah fatiha
    Given I am on quran.com home page
    When I click on surah fatiha
    Then I will enter on surah faitha page