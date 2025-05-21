Feature: Update profile name on My Info page

  Scenario: B: Change the admin user's name
    Then I navigate to the "My Info" page
    When I update the name to "testuser11" "testuser22" "testuser33"
    And I click on the save button