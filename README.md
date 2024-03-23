# My Flask App

This is a simple Flask application demonstrating a "Hello, World!" message.

## Startup Instructions

### Prerequisites

- Python 3.x installed on your system
- Virtual environment tool such as `virtualenv` or `venv`

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your_username/my_flask_app.git
   ```

2. Navigate to the project directory:

   ```bash
   cd my_flask_app
   ```

3. Set up a virtual environment (optional but recommended):

   - On Windows:

     ```bash
     py -m venv .venv
     ```

   - On macOS and Linux:

     ```bash
     python3 -m venv .venv
     ```

4. Activate the virtual environment:

   - On Windows:

     ```bash
     .venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source .venv/bin/activate
     ```

5. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

Once you have completed the installation steps, you can run the Flask application using the `run.py` script:

```bash
python run.py
```

The application will start on `http://127.0.0.1:5000/`. Open this URL in your web browser to see the "Hello, World!" message.

## Testing

To run the tests, use the following command:

```bash
pytest
```

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository on GitHub.
2. Create a new branch with a descriptive name (`git checkout -b feature/add-new-feature`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push your changes to your forked repository (`git push origin feature/add-new-feature`).
5. Submit a pull request describing your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
