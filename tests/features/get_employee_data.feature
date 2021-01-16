@automated
Feature: Employee - Fetch employee data
    As a user
    I will send GET request to Dummy Rest API
    I want to be able to see the expected response

    Background:
        Given I set Dummy Rest API URL to "/api/v1"

    @smoke
    Scenario: Get all employee data
        Given I set Dummy Rest API GET route to "/employees" for all employees
        When I set User-Agent as "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36" in headers
        And I send a GET HTTP request
        Then I expect HTTP response code to be "200" for "GET"
        Then I expect response body of "GET" to be non-empty
        And I expect response body to contain status: "success"
        And I expect response body to contain all employee data

    @smoke
    Scenario: Get a single employee data
        Given I set Dummy Rest API GET route to "/employee/{id}" for single employee
        When I set User-Agent as "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36" in headers
        And I send a GET HTTP request
        Then I expect HTTP response code to be "200" for "GET"
        Then I expect response body of "GET" to be non-empty
        And I expect response body to contain status: "success"
        And I expect response body to contain message: "Successfully! Record has been fetched."
        And I expect response body to contain a single employee data
