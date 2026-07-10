# GitHub API Automation Framework

## Overview

This project is a GitHub REST API automation framework built using **Python and Pytest**.

The framework automates GitHub repository operations such as creating, retrieving, updating, and deleting repositories. It validates API responses, status codes, and repository behavior using automated test cases.

The project is designed with a modular structure to make API automation easy to maintain and extend.

---

## What This Project Does

This framework performs automated testing of GitHub repository APIs.

Supported operations:

- Create a GitHub repository/branch
- Get repository/branch details
- Update repository/branch information
- Delete a repository/branch
- Validate API responses

---

## Tech Stack

- **Python** - Programming language
- **Pytest** - Test automation framework
- **Requests** - API communication library
- **GitHub REST API** - Application under test
- **pytest-html** - Test reporting
- **Logging** - Execution tracking

---

## Project Structure

pytest-api-demo
│
├── api/
│ ├── api_client.py # Handles API requests
│ ├── endpoints.py # Manages API endpoints
│ └── github_repo.py # Repository API operations
│
├── tests/
│ └── test_repo.py # Test cases
│
├── logs/
│ └── api_automation.log # Execution logs
│
├── Archives/
│ └── logs_.zip # Archived logs
│
├── requirements.txt
├── pytest.ini
└── conftest.py # Pytest fixtures

---

## Key Features

- Reusable API request handling
- Centralized endpoint management
- Separation of test logic and API implementation
- Pytest fixtures for dependency management
- Logging support
- Test reporting support
- Easy addition of new API tests

---

## How to Run

Install dependencies:

```bash
pip install -r requirements.txt
Run all tests:
pytest

Example Test Scenarios
Verify repository creation
Verify repository details
Update repository description
Change repository settings
Delete repository
Verify deleted repository
Validate invalid API requests
Purpose
The purpose of this project is to demonstrate API automation framework development using Python, Pytest, and GitHub REST APIs with a scalable and maintainable design approach.
