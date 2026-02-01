# Asteroids (Minimal Python / Pygame)

A small, educational implementation of the classic Asteroids game using
Python and Pygame. The project is intentionally compact and easy to read. A good starting point for learning game structure, simple physics,
and sprite-based updates/drawing.

---

## Features

- Player-controlled triangular ship with rotation and forward/back motion
- Shoot projectiles to break asteroids into smaller pieces
- Procedural asteroid spawning from off-screen edges
- Simple circle-vs-circle collision detection
- Lightweight logging of game events and state

---

## Requirements

- Python 3.8+
- pygame

Install dependencies (example):

```bash
pip install pygame
```

---

## Run the game

From the project root directory:

```bash
python main.py
```

(If you use a task runner or a script that wraps `python`, follow your
normal workflow — e.g., `uv run main.py` if you use that alias.)

---

## Controls

- W: Thrust forward
- S: Thrust backward
- A: Rotate left
- D: Rotate right
- SPACE: Shoot
- Close the window to quit

---

## Project structure

- `main.py` — game bootstrap, group setup, main loop
- `player.py` — player ship logic and input handling
- `shot.py` — simple projectile implementation
- `asteroid.py` — single asteroid behavior (draw, update, split)
- `asteroidfield.py` — timed spawning of asteroids from screen edges
- `circleshape.py` — lightweight base class (position, velocity, radius)
- `constants.py` — configuration constants (speeds, sizes, screen dims)
- `logger.py` — minimal logging helpers used for state/events
- `game_state.jsonl`, `game_events.jsonl` — persisted logs (JSON Lines)

---

## Notes & Ideas

- The code is intentionally simple — try adding features such as a
  scoring system, lives, sound effects, or asteroid sprites.
- The current collision logic is circle-based; switching to polygon
  collision would allow more detailed ship/asteroid shapes.

---
