# Restful Booker API Testing Project

This project is a simple API testing framework built using Python and `pytest`, designed to test the https://restful-booker.herokuapp.com. It tests real world scenarios plus edge cases to make sure API works smoothly.

It's designed to show how to write clear, reusable tests and organize all test well and keep track of test execution using logs.

---

## Setup Tools

- **Python 3** language used 
- **Pytest** for writing and executing test cases
- **Requests** Python library to interact with APIs
- **Logging** for saving logs test logs
- **Pycharm** IDE for writing and managing code 

---

##  Test Cases Covered

- Health check test
- Retrieve all bookings (GET `/booking`)
- Retrieve single booking (GET `/booking/{id}`)
- CRUD operations (Create, Read, Update, Partially update, Delete) for bookings
- Logging of test flow and outcomes
- Modular test setup using fixtures in `conftest.py`

##  Negative and Edge Case Testing
The following negative scenarios are covered:

-  Retrieving booking with an invalid ID  
-  Sending incorrect or badly formated json data 
-  Attempting to update booking with an invalid/expired token  
-  Deleting a booking twice to confirm graceful error handling  


---


##  Setup & Installation

1. **Clone this repository**
   ```bash
   git clone https://github.com/sobiasarfraz/restful-booker-project.git    
   cd restful-booker-project
   
2. (Optional) Create and activate a virtual environment

- **On macOS/Linux:**

        python -m venv .venv
        source .venv/bin/activate


- **On Windows:**
   
      python -m venv .venv
      .venv\Scripts\activate

3. Install dependencies

       pip install -r requirements.txt

Running Tests

Simply run the tests from the project root:

    pytest -v


To run only one test file:

    pytest tests/test_api_flow.py
To generate an HTML test report:
    
    pytest --html=reports/project_report.html


You can also generate a log file in the /logs folder after running the tests.

**Logging**

- All test execution logs are stored in the logs/ directory.

- Logs include:
  - API responses and status codes.
  - warnings, and errors for failed or edge case tests.
  - Informational logs about test actions (e.g. "update the booking", "booking is deleted")
---
**Author**

Sobia Sarfraz
email:

 GitHub Profile:  sobiasarfraz
---
## Continuous Integration (CI) with github actions
- All tests are run in virtual environment on every push or pull request to the `main` branch.
- A detailed **html report** `project_report.html` is generated after every test run
- The report is saved as a downloadable file under the **Actions** tab on GitHub.
- The workflow file  is located at:
 `.github/workflows/restful-booker.herokuapp.yml`

📄 License

This project is licensed for learning and demonstration purposes.

### Reference page for API endpoints ###
   https://restful-booker.herokuapp.com/apidoc/index.html
   
  
