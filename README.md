# boilerplate-poetry-project

Efficiently jumpstart your Python projects with boilerplate-poetry-project. Try it out as a template

**Purpose of this repository:**

1. **Streamline Project Setup:** This repository serves as a boilerplate to efficiently set up your Python project using Poetry for dependency management.
2. **Private Package Publishing:** Documents the process of publishing code as a Python package within a private repository (instructions not included but can be found in the Poetry documentation).

## Getting Started

This project leverages `pyenv` and `poetry` for streamlined environment management. Make sure you have them installed before proceeding.

Refer to their documentation for installation instructions.

* [PyEnv Installation](https://github.com/pyenv/pyenv?tab=readme-ov-file#getting-pyenv)
* [Poetry Installation](https://python-poetry.org/docs/#installing-with-the-official-installer)

**Setting Up the Development Environment**

1. **Install and Verify Python Versions:**

   * Use `pyenv` to install the required Python versions for your project. For example, to install Python 3.11.4:

     ```bash
     pyenv install 3.11.4
     ```
   * Verify the installation by listing available versions:

     ```
     pyenv versions
     ```
2. **Set the Default Python Version (Optional):**

   * If you have multiple Python versions and want to set one as the default for your project, do

     ```bash
     pyenv local 3.11.4
     ```

     This sets Python 3.11.4 as the active version in your current shell.
3. **Initialize the Poetry Environment:**

   * Navigate to your project directory and initialize a `poetry` environment:

     ```bash
     poetry init
     ```

     This creates a `pyproject.toml` file, which serves as the configuration center for your project's dependencies.
4. **Verify Poetry Environment Information:**

   * To view details about the active virtual environment, including the Python version, platform, and paths

     ```bash
     poetry env info
     poetry env info -p  # to view the path only
     ```
   * Optional: To ensure virtual environments are created inside your project folder, change the configuration setting and `poetry install` to see the creation of `.venv` folder

   ```bash
   poetry config virtualenvs.in-project true
   ```
5. **Activate the Poetry Environment (if necessary):**

   * If `pyenv` isn't managing your system-wide Python version or you want to explicitly activate the project's environment

     ```bash
     poetry env use python3.11
     ```

     Replace `python3.11` with the appropriate version for your project.
6. **Enter the Poetry Shell (Optional):**

   * To isolate your development environment and manage dependencies effectively, start the Poetry shell:

     ```
     poetry shell
     ```

   This launches a new shell pre-configured with the project's environment. The virtual environment name will be reflected in the prompt (e.g., `(my-project-3.11) $`).

## Note Regarding Folder Naming Conventions

Folder naming conventions in Poetry projects based on your approach to project creation:

**1. Using `poetry new`:**

When you create a new project using `poetry new project-name`, Poetry will automatically generate a folder named after your chosen project name (e.g., `project-name`) with the following structure:

```
poetry-project
├── pyproject.toml
├── README.md
├── poetry_project
│   └── __init__.py
└── tests
│    └── __init__.py 
└── .pre-commit-config.yaml

```

Reference: https://python-poetry.org/docs/basic-usage/#project-setup

**2. Using `poetry init` in an Existing Folder:**

If you initialize a Poetry project within an existing folder using `poetry init` (how this repo was set up), ensure the folder name adheres to the following guidelines:

* Use lowercase letters and underscores (`_`) only (no hyphens or other special characters).
* The naming convention should match your project name. For example, if your Poetry project name is `my-project`, the enclosing folder should be named `my_project`.
* Using underscores in folder names aligns with how Python expects modules to be structured for import.


## Project Dependencies

This project uses several dependencies managed by Poetry to streamline development, testing, and project management. Below is a list of key dependencies and a brief description of their purpose:

- **pyenv**: A tool that allows for easy installation and management of multiple Python versions. It's used to set a specific Python version for our project to ensure consistency across development environments.

- **Poetry**: A dependency management and packaging tool in Python. It's used to declare project libraries, manage their versions, and set up the project's virtual environment.

- **pytest**: A framework that makes it easy to write simple tests, yet scales to support complex functional testing. It's used for writing and running our project's tests.

- **pytest-cov**: A plugin for pytest that provides test coverage reporting for our tests. It's useful for identifying parts of the codebase that may not be adequately tested.

- **Hypothesis**: A library for property-based testing. With Hypothesis, you can write tests that are parameterized according to a source of examples. It's used to generate test cases that might not have been manually considered.

- **mypy**: An optional static type checker for Python. Mypy checks that the type hints in the codebase are being followed correctly, helping to catch type-related errors before runtime.

- **pre-commit**: A framework for managing and maintaining multi-language pre-commit hooks. It's used to run checks on the code before committing, ensuring code quality and style consistency.

- **isort**: A Python utility/library to sort imports alphabetically and automatically separate them into sections. It ensures that import statements are clean and consistently formatted.

- **ruff**: An extremely fast Python linter. It's used to catch syntax errors and stylistic issues before they make it into the codebase.


## Running Tests and Checking Test Coverage

Ensuring that your code is well-tested is crucial for maintaining high-quality software. This project uses `pytest` for testing and `pytest-cov` to check test coverage. Here's how you can run tests and generate coverage reports.

### Running Tests

To run all tests in the project, navigate to the project's root directory and use the following command:

```bash
poetry run pytest
```

This command runs all tests in the project, ensuring that all tests pass.

### Checking Test Coverage

To generate a coverage report, use the following command:

```bash
poetry run pytest --cov
```

This command runs all tests in the project and generates a coverage report, showing which parts of the codebase are covered by tests.
