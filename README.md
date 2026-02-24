# Alien Invasion (Pygame)

A small arcade shooter built with `pygame`.

## Features

- Player ship movement and shooting
- Alien fleet generation and movement
- Bullet-alien collision scoring
- Level progression with increasing speed
- High score persistence (`high_score.json`)
- Blink skill: press `D` with one direction key to dash horizontally

## Controls

- `Left` / `Right`: move ship
- `Space`: fire bullet
- `D` + (`Left` or `Right`): blink/dash
- `Esc` or `Q`: quit game
- Mouse click `Play`: start game

## Requirements

- Python 3.10+ (recommended)
- `pygame`

Install dependency:

```bash
pip install pygame
```

## Run

From project root:

```bash
python alien_invasion.py
```

## Project Structure

- `alien_invasion.py`: main game loop and event handling
- `settings.py`: gameplay configuration
- `ship.py`: player ship logic
- `alien.py`: alien sprite behavior
- `bullet.py`: bullet behavior
- `game_stats.py`: game state and high score loading
- `scoreboard.py`: HUD and high score name input
- `button.py`: play button rendering
- `images/`: sprite assets
- `high_score.json`: saved high score data

## Notes

- If `D` input behaves unexpectedly on some systems, switch to English keyboard input mode.
- `high_score.json` is game runtime data; you can keep it in repo or ignore it based on team preference.

## License

No license file is included yet. Add a `LICENSE` before publishing if you want others to reuse your code.
