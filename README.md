# rr-qa-automation-assignment
This is a QA Assignment for the demo project. The goal of this project is to implement a highly maintainable, self-reporting, and shippable end-to-end automation framework that comprehensively evaluates both successful user journeys and edge cases.

# RR QA Automation Assignment

## 1. Testing Strategy

The testing approach focused on validating the most critical user workflows of the TMDB Discover application. The strategy included:

* Functional testing of filters and navigation.
* Positive and negative test scenarios.
* UI validation using Selenium WebDriver.
* Independent test execution using Pytest fixtures.
* Page Object Model for maintainability and reusability.
* Documentation of known defects.

The priority was given to user-facing functionality such as categories, search, filters, and pagination.

---

## 2. Test Cases Generated and Why

### Category Navigation

* Verify Popular category.
* Verify Trend category.
* Verify Newest category.
* Verify Top Rated category.

These tests ensure users can navigate between different movie sections.

### Search Functionality

* Search with a valid movie name.
* Search with an invalid movie name.

These tests verify search behavior and result filtering.

### Type Filter

* Select Movie.
* Select TV Shows.

These tests validate content filtering based on media type.

### Genre Filter

* Verify filtering by genres such as Comedy and Drama.

These tests ensure genre-based filtering works correctly.

### Year Filter

* Verify filtering using year ranges.

These tests validate release year constraints.

### Rating Filter

* Verify filtering based on ratings.

These tests ensure highly rated content can be identified.

### Pagination

* Verify next page navigation.
* Verify previous page navigation.

These tests ensure users can browse multiple pages of results.

### Negative Scenarios

* Invalid search input.
* Refreshing slug URLs.
* Pagination edge cases.

These tests help identify defects and improve robustness.

---

## 3. Test Automation Framework

Framework:

* Python 3
* Selenium WebDriver
* Pytest
* WebDriver Manager
* Pytest HTML Report

Libraries Used:

* selenium
* pytest
* webdriver-manager
* pytest-html

Framework Pattern:

* Page Object Model (POM)

Folder Structure:

```
tests/
docs/
reports/
screenshots/
conftest.py
home_page.py
requirements.txt
README.md
```

---

## 4. How to Run Tests

Install dependencies:

```bash
pip install -r requirements.txt
```

Run all tests:

```bash
pytest
```

Run specific tests:

```bash
pytest tests/test_filters.py
pytest tests/test_pagination.py
```

Generate HTML report:

```bash
pytest --html=reports/report.html
```

---

## 5. Test Design Techniques Used

### Positive Testing

Valid inputs and expected user behavior were verified.

### Negative Testing

Invalid inputs and known edge cases were tested.

### Boundary Value Testing

Year ranges and pagination behavior were validated near boundaries.

### Equivalence Partitioning

Representative values were selected instead of testing every possible combination.

### Exploratory Testing

Manual exploration was performed to identify unexpected behaviors and defects.

---

## 6. Coding Patterns Used

### Page Object Model (POM)

Locators and actions are separated from test cases to improve readability and maintainability.

### Fixture Pattern

Pytest fixtures are used to manage browser setup and teardown.

### Reusability

Common methods are placed inside page classes and reused across multiple tests.

### Separation of Concerns

Tests, page objects, reports, and documentation are maintained separately.

---

## 7. Defects Identified

### BUG-001: Refreshing Slug URLs

Example:

```
https://tmdb-discover.surge.sh/popular
```

Refreshing the page may lead to incorrect behavior because the route is not handled properly.

Severity: Medium

---

### BUG-002: Pagination Issues

Pagination behavior near the last pages may be inconsistent.

Severity: Medium

---

### BUG-003: Search Edge Cases

Invalid search values may produce unexpected results or empty states.

Severity: Low

---

## 8. Design Pattern Used

Simple Page Object Model (POM) was used to separate page actions from test logic, making the framework easier to maintain and extend.
