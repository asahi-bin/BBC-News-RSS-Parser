# BBC News RSS Parser

## About
This project is designed for **automatic parsing of BBC news** through their official RSS feed.
The program downloads news, extracts titles and links, descriptions and publication date, and then saves them in JSON format.

The goal of the project is **easy to get relevant news in a structured form** so that they can be used for analytics, Telegram bot or other applications.

This is my first parser and I used AI to create it. It's not bad, but I want to do such projects without it on 100%. And just by writing this project, I learned what I need to learn (namely the libraries).

---

I recommend using **virtual environment (`venv`)** to isolate project dependencies.

### Installation of dependencies
```bash
# Create a virtual environment
python -m venv .venv

# Activate virtual environment
# Linux/macOS
source .venv/bin/activate

#Windows
.venv\Scripts\activate

# Install the necessary libraries
pip install requests beautifulsoup4 lxml
```

Read [Install packages in a virtual environment using pip and venv](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/)

---

### The script works at the expense of keys

```bash
python3 main.py -h
```

```text
usage: main.py [-h] (-l | -p PARSE | --parse-all) [--limit LIMIT] [-o OUTPUT]

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
python main.py -l

# Parse a single topic
python main.py -p world --limit 10

# Parse all topics
python main.py --parse-all
```

---

### Output format

Parsed news is saved as a JSON file in the specified output directory.
