# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Running the project

```bash
# Run the interactive bot (play Wordle with assistance)
python main.py

# Run simulations to evaluate scoring systems
python simulate.py

# Run graphing/visualization of simulation results
python chart.py

# Populate the database (one-time setup)
python upload.py
```

## Architecture

The bot uses a scored word dictionary to recommend the best next guess. Words are ranked by a weighted combination of two probability-based scoring systems, computed at startup from the SQLite database.

**Data flow:**
1. `upload.py` scrapes Wordle words and stores them in `WordleDictionary.db` (SQLite)
2. `create.py` handles the scraping logic (using `requests` + `BeautifulSoup`)
3. `counter.py` loads the word list and computes three scored word dicts at module level:
   - `word_score` / `stand_word_score` — letter frequency across all positions
   - `loc_word_score` / `stand_loc_score` — letter frequency per position
   - `final_word_dict` — weighted combination (22% letter, 78% location), standardized
4. `database.py` (`WordleDatabase`) wraps SQLite for storing/retrieving lists and dicts as JSON
5. `edit.py` (`EditDictionary`) wraps a scored dict and filters it based on Wordle feedback (green/yellow/black). `best_word()` returns the top-ranked remaining word.
6. `main.py` runs the interactive loop: suggest word → get user feedback → filter dictionary → repeat
7. `simulate.py` (`WordleSimulation`) auto-solves every word in the list and records turn count
8. `chart.py` (`WordleGraph`) visualizes simulation results via matplotlib

**Key design detail:** `counter.py` runs all scoring computation at import time, so importing it is expensive. `EditDictionary` takes a plain `dict` (not the class) and mutates a copy — callers must `copy.deepcopy` before passing if they need to reuse the original.
