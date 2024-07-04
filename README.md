# CarZone Dealership

Welcome to CarZone Dealership! This is a Django-based web application that allows users to search for cars and view car listings.

## Features

- User authentication using Django Allauth
- Search functionality to find cars based on various criteria
- Car listing pages to display detailed information about each car

## Installation

1. Clone the repository:

    ```bash
    https://github.com/snipher-marube/CarZone-dealership.git
    ```

2. Navigate to the project directory:

    ```bash
    cd CarZone-dealership
    ```

3. Create a virtual environment:

    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:

    - For Windows:

      ```bash
      venv\Scripts\activate
      ```

    - For macOS/Linux:

      ```bash
      source venv/bin/activate
      ```

5. Install the project dependencies:

    ```bash
    pip install -r requirements.txt
    ```

6. Apply database migrations:

    ```bash
    python manage.py migrate
    ```

7. Start the development server:

    ```bash
    python manage.py runserver
    ```

8. Open your web browser and visit `http://localhost:8000` to access the CarZone Dealership application.

## Usage

- Register a new user account or log in with an existing account.
- Use the search functionality to find cars based on make, model, year, etc.
- View detailed information about each car on the car listing pages.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
