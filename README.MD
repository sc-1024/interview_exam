## CathayBK Exam

## Logic Test
```
logic/
├── hollow_triangle.py
└── sort_num.py
```
### How to run the logic test
1. Run the hollow triangle logic test
    ```bash
    python logic/hollow_triangle.py
    ```
2. Run the sort number logic test
    ```bash
    python logic/sort_num.py
    ```

## API Automation

### Description
This project is an API automation framework built using pytest and pydantic with python 3.11.3, designed for API testing with structured validation models.

### Project Structure
```
api_automation/
├── api_utils/
│   └── rest_api.py              # Wrapper for requests
├── common_utils/                # Common utilities (e.g. logger, report)
│   └── logger.py
├── configs/
│   └── config_template.py       # Template for configuration file
├── star_wars/
│   ├── data/
│   │   └── films/
│   │       └── test_data.py     # Sample data for films
│   ├── models/
│   │   └── films.py             # Pydantic model for films
│   ├── service/
│   │   └── films.py             # API Actions for films
│   └── tests/
│       ├── films/
│       │   └── test_films.py    # Test cases for films
│       ├── conftest.py
│       └── rest_base.py         # Base class for API tests
├── pytest.ini
└── README.md
```

### Prerequisites
* Python 3.11+
* poetry
    ```
  Install poetry using the following command:
    curl -sSL https://install.python-poetry.org | python3 -
  ```

### Project Setup
1. Clone the repository
2. Install the dependencies
    ```bash
    poetry install --no-root
    ```
   
### Running the tests
1. Run all tests
    ```bash
    poetry run pytest -s -vv tests
    ```
2. Run tests with specific marker
    ```bash
    poetry run pytest -s -vv -m <marker> tests
    ```

### Test Report
1. Run all tests with allure command
    ```bash
    poetry run pytest -vv tests --alluredir=./reports --clean-alluredir
    ```
2. Generate allure report
    ```bash
    poetry run allure generate ./reports -o ./allure-results/html --clean
    ```

### How to define an API and add first test cases
#### 1. Create a model in `models` directory

   Define the data structures for your API requests and responses using Pydantic models. Make sure the data validation and consistency across tests.

   For example /api/user JSON response data as below:
   ```json
      {
          "username": 0,
          "email": "steven@gmail.com"
      }
   ```  
   Use `BaseModel` of `Pydantic` to create a model to fill each field we need, it can define the type and default value in the class, here is an example for define the response model like below
   ```python
   from pydantic import BaseModel

   class UserResponseData(BaseModel):
        username: str
        email: str
   ```

#### 2. Create a service in `service` directory

   Create the action file in project folder (e.g. `star_wars`), and define the API model and define `path`, `method` and `response_type` in the class, the host will be defined in the `rest_base.py`. 
   ```python
    class GetUserAPI(RestApi):
        path: str = "/api/user"
        method: HttpMethods = HttpMethods.GET
        response_type = UserResponse
   ```

   Define the class for the endpoint and define functions in the class
   ```python
     class UserAction(RestAction):
        def request_get_user(self) -> UserResponse:
            """
            :return: User info
            """
            api = GetUserAPI(host=self.host)
            resp = api.request(json=payload)
            return UserResponse(**resp.json())
   ```

#### 3. Create test cases in `tests` directory

   Create the test file in the test folder, and define the test case in the class, use the `service` to call the API and assert the response data.
   ```python
    class TestUser:
        def test_get_user(self):
            user = UserAction().request_get()
            assert user.username == "steven"
            assert user.email == "XXX@XXX.com"
