# Development

## Start development

Create and activate an environment by running the following command:

```bash
python -m venv .venv
```

**On Windows:**

```bash
.venv/Scripts/activate
```

**On Linux/macOS:**

```bash
source .venv/bin/activate
```

Install the required dependencies:

```bash
pip install -r src/requirements.txt
```

To build and install the project using `pyproject.toml`:

```bash
pip install .
```

To run the application:

```bash
python src/workdir.py
```

## Notes

If you run Workdir the first time, the window can be really small. The size is auto-adjusted based on your directories.
