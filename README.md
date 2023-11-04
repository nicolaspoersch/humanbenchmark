# Reaction Time Benchmark ✏️

This is a Python program designed to measure reaction time by allowing the computer to react to a change in the color green on the screen. The goal is to simulate a fast reaction, similar to that of a person with keen reflexes or a high refresh rate monitor.

## Features

- Automatically reacts to a change in the green color on the screen.
- Allows you to configure the delay between color detection and reaction.
- Activates/deactivates the program with a keyboard shortcut (`Ctrl+Alt+P`).

## Requirements

- Python 3.x
- Python libraries: `pyautogui`, `time`, `random`, `keyboard`, `winsound`

## Usage

1. Run the Python script.
2. The program is enabled by default and is waiting for a change in the green target color.
3. Use the `Ctrl+Alt+P` shortcut to enable/disable the program.
4. When the program is enabled, it will automatically detect the green target color on the screen.
5. When the green target color is detected, there will be a configurable delay, followed by a click at the position where the color was found.

## Configuration

You can customize the green target color and the delay between detection and reaction by adjusting the variables at the beginning of the script:

- `target_color`: The green color that the program should detect (RGB format).
- `delay`: The delay between detection and reaction. It can be configured with the desired values.

## Keyboard Shortcut

- `Ctrl+Alt+P`: Enables/disables the program.
