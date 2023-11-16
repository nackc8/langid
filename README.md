# Langid - Identifies language of text

### Requirements

- Python 3.10 or greater is required.

### Getting Started

#### VS Code Setup

To set up your environment with Visual Studio Code, follow these instructions:

1. Open the repository in VS Code which utilizes the `.vscode` directory at the root.
2. Install the recommended extensions that pop up upon opening.
3. Use "Python: Create Environment..." to set up a `.venv` at the root for local development, despite the backend directory being preferable for isolated Docker use.

#### Setting up the virtual environment

Before running the application, you need to set up a virtual environment and install the necessary dependencies. Follow these steps:

1. Navigate to the project's root directory.

```bash
cd path/to/langid
```

2. Create a virtual environment in the `backend` directory.

```bash
# On macOS and Linux:
python3 -m venv venv

# On Windows:
python -m venv venv
```

3. Activate the virtual environment.

```bash
# On macOS and Linux:
source venv/bin/activate

# On Windows:
.\venv\Scripts\activate
```

#### Installing Dependencies

Install all dependencies required for the project to run:

```bash
pip install -r requirements.txt
```

#### Running the Application

Use the command line interface to run the application after activating the venv.

```bash
# On macOS and Linux:
./langid.py --help

# On Windows:
langid.py --help
```

# Useful links

- [Pytest Docs](https://docs.pytest.org/en)
- [Pytest How-to](https://docs.pytest.org/en/7.4.x/how-to/index.html#how-to)
- [unittest.mock docs](https://docs.python.org/3/library/unittest.mock.html)
