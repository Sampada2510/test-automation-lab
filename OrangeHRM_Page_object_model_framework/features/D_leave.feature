Feature: Assign Leave

  Scenario: Assign a half-day personal leave to an employee
    Given I am logged in as an admin user
    Then I navigate to the Assign Leave page
    When I enter the leave details for employee "testuser11" with type "CAN - Matternity", for today as half day "AM", and comment "Half day off"
    And I click on the Assign button
    Then the leave should be assigned successfully