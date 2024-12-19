# [FinTrack]

## Overview

[Hi, I’m Kai Nguyen, and my project is called ‘FinTrack.’ Many people find it hard to track their spending and manage their budgets, which can cause financial stress. FinTrack is a tool that analyzes income, expenses, and savings, helping users see where their money goes, like food, entertainment, and bills. What makes FinTrack special is its ability to find saving opportunities and send alerts when users are close to their budget limits. I’m excited to develop FinTrack to help people make better financial decisions and take control of their money.]

### Primary Features

- [Store transactions (Date, category, amount, name, type, description, type)]
- [Add new transactions, then view all]
- [Analyze expenses and alert for budget limits]

---

## Project Structure

```
[FinTrack]/
│   # Phase 1: Business logic:
├── core.py          # Core business logic
├── test.py          # Tests for business logic
├── transaction.py   # business logic
├── utils.py         # greetings and check
│
│   # Phase 2: Choose one or more of these UI options:
├── main.py          # CLI interface (optional)
│
├── readme.md       # This file
├── changelog.md    # Weekly development updates
├── /data          # Data files
└── /resources     # Course resources and help
```

## Getting Started

1. Install dependencies

No dependency

```bash
pip install <dependency>
...
```

2. Run business logic tests

```bash
python test.py
```

3. Run the program
   [Choose the appropriate command based on your UI choice:]

```bash
# If using CLI interface:
python main.py


# Any other interface you choose

```

[Update these instructions to match your chosen interface]

## Weekly Progress

See [changelog.md](changelog.md) for detailed development updates.

## Future Ideas

- [Building a beautiful user interface using web framework]
- [Enabling multi user support: sign up, login, logout, authentication]
- [Enabling AI's advice on financial planning]

## AI Usage

function: def __build_transactions_list(self, transactions, choice, argument) in core.py
I have to consult Chatgpt for the complicated logic of sorting and filtering

## Resources Used

- (https://docs.python.org/3/library/json.html): I needed to consult this python website to better understand how to handle json data (serialize and deserialize)
- Course materials: I needed to write and read data into file.

---

Created by Kai Nguyen for CSC-121
