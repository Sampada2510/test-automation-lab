@awesome
Feature: Basic shopping flow on AwesomeQA

  Scenario: Search for an existing product
    Given the user is on the homepage
    When the user searches for "MacBook"
    Then the search results should show the product "MacBook"

  Scenario: Add a product to the cart
    Given the user searched for "MacBook"
    When the user adds the product to the cart
    Then the success message should confirm the product is added

  Scenario: Navigate to contact us page
    Given the user is on the homepage
    When the user clicks on "Contact Us"
    Then the contact page should be displayed
