# BBC News RSS Parser

## About
This project is designed for **automatic parsing of BBC news** through their official RSS feed.
The program downloads news, extracts titles and links, descriptions and publication date, and then saves them in JSON format.

The goal of the project is **easy to get relevant news in a structured form** so that they can be used for analytics, Telegram bot or other applications.

This is my first parser and I used AI to create it. It's not bad, but I want to do such projects without it on 100%. And just by writing this project, I learned what I need to learn (namely the libraries).

---

## Project Structure

```text
bbc/
├── pyproject.toml        # Project metadata and CLI entry point
├── README.md
│
├── bbc/
│   ├── __init__.py
│   ├── __main__.py       # Package entry point (python -m bbc / bbc)
│   │
│   ├── cli/              # Command-line interface layer
│   │   ├── args.py       # Argument parsing (argparse)
│   │   └── handlers.py   # CLI mode handlers
│   │
│   ├── core/             # Business logic
│   │   ├── fetcher.py    # RSS / HTTP fetching
│   │   └── parser.py     # RSS / HTML parsing
│   │
│   ├── storage/          # Output layer
│   │   └── json.py       # Save parsed data to JSON
│   │
│   └── config/
│       ├── header.py     
│       └── topics.py     # Available BBC RSS topics
```

### Architecture overview

- cli — defines how the user interacts with the tool
- core — contains pure logic (fetching and parsing)
- storage — responsible for data persistence
- config — static configuration and constants

This separation allows the project to scale without turning into a monolithic script.

---

## Installation

It is recommended to use a **virtual environment (`venv`)** to isolate dependencies.

### Create and activate virtual environment

```bash
python -m venv .venv

# Linux / macOS
source .venv/bin/activate

# Windows
.venv\Scripts\activate
```

Read [Install packages in a virtual environment using pip and venv](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/)

### Install the project

The project uses pyproject.toml and exposes a CLI command.

```bash
pip install -e .
```

This will:
- install dependencies
- register the bbc command
- link the command to the project source code

---

## Usage

After installation, the CLI tool is available as bbc.

```bash
bbc -h
```

```text
usage: bbc [-h] (-l | -p PARSE | --parse-all) [--limit LIMIT] [-o OUTPUT]

BBC News RSS Parser

options:
  -h, --help            show this help message and exit
  -l, --list-topics     Show available BBC topics
  -p, --parse PARSE     Parse BBC topic (default: Top_Stories)
  --parse-all           Parse all BBC topics
  --limit LIMIT         Limit number of parsed news
  -o, --output OUTPUT   Output directory
```

### Examples

```bash
# Show available topics
bbcy -l

# Parse a single topic
bbc -p world --limit 10

# Parse all topics
bbc --parse-all
```

---

## How it works

1. The user runs the bbc command.
2. The CLI entry point is defined in pyproject.toml.
3. bbc/__main__.py launches the CLI.
4. Arguments are parsed in cli/args.py.
5. The corresponding handler is executed from cli/handlers.py.
6. RSS data is fetched and parsed via the core layer.
7. The result is saved to JSON via the storage layer.

---

## Output format

Parsed news is saved as a JSON file in the specified output directory.

Each file contains:
- topic name
- publication date
- title
- description
- link