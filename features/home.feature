Feature: Quran.com Home Page
  As a user of Quran.com
  I want to be able to easily access and navigate the website's home page
  So that I can quickly find the information I need and begin my study of the Quran

  Scenario: Accessing Quran.com Home Page
    Given I have a web browser open
    When I open my web browser and type www.quran.com in the address bar
    Then I should be directed to the Quran.com home page

  Scenario: check search button
    Given I am on the Quran.com home page
    Then search button should be there

  Scenario: check language button
    Given I am on the Quran.com home page
    Then language button should be there

  Scenario: check setting button
    Given I am on the Quran.com home page
    Then setting button should be there

  Scenario: check login button
    Given I am on the Quran.com home page
    Then login button should be there

  Scenario: surahs are listed
    Given I am on the Quran.com home page
    Then surah are listed in the container

  Scenario: Using the search bar
    Given I am on the Quran.com home page
    When I click on search bar
    Then The search pop up shows up

  Scenario: Accessing Quranic Surahs
    Given I am on the search pop up
    When I click on juz 1
    Then I should be directed to the juz 1 page
