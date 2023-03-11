Feature: Quran.com Home Page
  As a user of Quran.com
  I want to be able to easily access and navigate the website's home page
  So that I can quickly find the information I need and begin my study of the Quran

  Scenario: Accessing Quran.com Home Page
    Given that I am a user of Quran.com
    When I open my web browser and type "www.quran.com" in the address bar
    Then I should be directed to the Quran.com home page

  Scenario: Change theme to dark
    Given that I am on the Quran.com home page
    When Change theme is clicked to dark
    Then Theme is changed to dark

  Scenario: Change language
    Given that I am on the Quran.com home page
    When Change language to urdu
    Then language is changed to urdu

  Scenario: surahs are listed
    Given that I am on quran.com home Page
    When check for the surah div
    Then surah are listed in the container

  Scenario: Using the search bar
    Given I am on Quran.com home page
    When I click on search bar
    Then The search pop up appearsw

  Scenario: Accessing Quranic Surahs
    Given I am on the search pop up
    When I click on juz 1
    Then I should be directed to the juz 1 page

  Scenario: Accessing Settings
    Given I am on Quran.com home Page
    When I click on settings icon
    Then setting menu is oppened

  Scenario: Increase font size:
    Given setting menu is oppened
    When I click on font size + button
    Then Font size will increase
