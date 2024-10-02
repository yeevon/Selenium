# SeleniumHQ Documentation Review and Template Project

## Purpose
The purpose of this project is to review and document the SeleniumHQ documentation while building a template project for Selenium with Python. This project aims to be versatile, allowing users to run tests locally, within Docker containers, and on cloud services like Sauce Labs and BrowserStack.

## Table of Contents
- [Purpose](#purpose)
- [Getting Started](#getting-started)
- [Running Locally](#running-locally)
- [Running with Docker](#running-with-docker)
- [Running on Sauce Labs](#running-on-sauce-labs)
- [Running on BrowserStack](#running-on-browserstack)

## Getting Started
To get started with this project, ensure you have the following prerequisites:
- Python 3.11.9 installed
- Pytest 8.3.3 installed
- Pip (Python package installer) installed
- Docker installed (if using Docker)

## Running Locally
### Instructions
1. Clone the repository:
   ```bash
   git clone <https://github.com/yeevon/Selenium.git>
   cd <Selenium\SeleniumPythonPracticeProject>
2. Use pytest to run test: https://docs.pytest.org/en/stable/how-to/usage.html
   ```bash
   pytest pytest '.\SeleniumPythonPracticeProject\Seleniumhq Documentation\test_webdriver.py'
   
## Running Docker
### Instructions
1. Clone the repository:
   ```bash
   git clone <https://github.com/yeevon/Selenium.git>
   cd <Selenium\SeleniumPythonPracticeProject>
2. Have Docker Desktop installed: https://app.docker.com/


3. Pull and run selenium standalone chrome image:
   ```bash
   docker run -d -p 4445:4444 -p 7900:7900 --shm-size="2g" selenium/standalone-chrome:latest
3. Use pytest to run test: https://docs.pytest.org/en/stable/how-to/usage.html
   ```bash
   pytest .\SeleniumPythonPracticeProject\Docker\test_webdriver_docker_standalone_chrome.py