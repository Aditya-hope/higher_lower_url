# Higher or Lower

A simple number-guessing game built with Flask. The server picks a random number between 0 and 9, and you guess by visiting different URLs to see if you're too high, too low, or spot on.

## How to Play

1. Visit the homepage to start the game.
2. Guess a number by navigating to `/<number>` (e.g. `/5`).
3. The page will show a GIF and message telling you if your guess was too low, too high, or correct.

## Setup

4. ### Requirements
- Python 3.x
- Flask

### Installation

```bash
pip install flask
```

### Running the app

```bash
python server.py
```

Then open your browser to `http://127.0.0.1:5000/`



## Notes

- The secret number is generated once when the server starts and stays the same until the server restarts.
- Built as a learning project to practice Flask routing and dynamic URLs.
