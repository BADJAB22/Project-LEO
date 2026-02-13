# Contributing to Project LEO

We welcome and appreciate your contributions to Project LEO! This document outlines the guidelines for contributing to ensure a smooth and collaborative development process.

## How to Contribute

There are many ways to contribute to Project LEO, including:

*   **Reporting Bugs:** If you find a bug, please open an issue on our GitHub repository.
*   **Suggesting Features:** Have an idea for a new feature or improvement? Open an issue to discuss it.
*   **Writing Code:** Contribute directly by fixing bugs, implementing new features, or developing new skills.
*   **Improving Documentation:** Help us make our documentation clearer, more comprehensive, and easier to understand.
*   **Community Support:** Answer questions, help other users, and participate in discussions.

## Getting Started with Code Contributions

1.  **Fork the Repository:** Start by forking the `Project-LEO` repository on GitHub.
2.  **Clone Your Fork:** Clone your forked repository to your local machine:
    ```bash
    git clone https://github.com/YOUR_USERNAME/Project-LEO.git
    cd Project-LEO
    ```
3.  **Create a New Branch:** For each new feature or bug fix, create a new branch:
    ```bash
    git checkout -b feature/your-feature-name
    # or
    git checkout -b bugfix/issue-description
    ```
4.  **Set up Your Development Environment:** Follow the instructions in `install.sh` and `README.md` to set up your local development environment.
5.  **Make Your Changes:** Write your code, tests, and update documentation as necessary.
6.  **Test Your Changes:** Ensure your changes do not introduce new bugs and that all existing tests pass.
7.  **Commit Your Changes:** Write clear and concise commit messages. Follow the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) specification if possible.
    ```bash
    git commit -m "feat: add new skill for calendar integration"
    ```
8.  **Push to Your Fork:**
    ```bash
    git push origin feature/your-feature-name
    ```
9.  **Open a Pull Request (PR):** Go to the original `Project-LEO` repository on GitHub and open a new Pull Request from your branch. Provide a detailed description of your changes.

## Code Style and Guidelines

*   **Python:** Adhere to PEP 8 style guidelines. We recommend using a linter like `flake8` or `black`.
*   **Type Hinting:** Use type hints for all function arguments and return values.
*   **Docstrings:** Document your code using Google-style docstrings for functions, classes, and modules.
*   **Tests:** All new features and bug fixes should be accompanied by appropriate unit and integration tests.

## Developing New Skills

Project LEO's modular design makes it easy to add new skills. To create a new skill:

1.  Navigate to the `leo_core/skills/` directory.
2.  Create a new Python file (e.g., `my_new_skill.py`).
3.  Define your skill as a Python function or class that can be imported and used by the `leo_core/brain` module.
4.  Ensure your skill has clear documentation and handles potential errors gracefully.

## Issue Reporting

When reporting an issue, please include:

*   A clear and concise title.
*   A detailed description of the problem.
*   Steps to reproduce the behavior.
*   Expected behavior.
*   Screenshots or error messages (if applicable).
*   Your operating system and Python version.

## Code of Conduct

By participating in Project LEO, you are expected to uphold our [Code of Conduct](CODE_OF_CONDUCT.md). Please read it carefully.

Thank you for helping us build Project LEO!
