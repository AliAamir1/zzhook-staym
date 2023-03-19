Feature: Quran.com Home Page Assesment
    As a user of Quran.com
    I want to view all the contents properly.  able to easily access and navigate the website's home page
    So that I can quickly find the information I need and begin my study of the Quran

    Background: On home page of Quran.com
        Given I am on the Quran.com home page
    
    # Scenario: All Surah Tags are shown
    #     Then All the Surah tags are shown



    #Scenario: chal nai rra
     #   When I click Juz
      #  Then I get Juz


    # Scenario: View By Tab 
    #     Then View By Tab is present

    Scenario Outline: Viewing by Surah,Juz and Revelation   
       When I switch to "<tab>"     
       Then the "<view>" is switched

    Examples: Tabs
        | tab | view | 
        | Juz | JuzView_juzTitle__mVq8J |
        | Surah | SurahPreviewRow_container__3ZfRV | 
        | Revelation Order | ChapterAndJuzList_revelationOrderDisclaimer__ymzfy |
            