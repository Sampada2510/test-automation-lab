Feature: Admin User Search

  Scenario: Search the user on Admin page
    Given I am logged in as an admin user
    Then I navigate to the Admin page
    When I search for the username "testuser11"
    Then the user "testuser11" should be visible in the result


  Scenario: Add a new user
    Given I am logged in as an admin user
    Then I navigate to the Admin page
    When I click on the Add button
    And I fill in the userrole "Admin", status "Enabled", and employeename "testuser11"
    And I fill in the user details with username "Samp13", password "Password@123" and confirm password "Password@123"
    And I click on the Save button on add user
    Then I navigate to the Admin page
    When I search for the username "testuser11"
    Then the user "Samp13" should be visible in the result