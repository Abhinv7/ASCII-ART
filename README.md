# ASCII Art Generator (Python)

A terminal-based ASCII Art Generator written in Python. This program converts characters, words, and numbers into large ASCII art using the * symbol and displays them in the terminal with optional color output. The project also includes predefined ASCII logos such as a heart and a smiley face.
The application is menu-driven and uses instant keypress input for smooth navigation.

## Table of Contents

- Introduction
- Features
- Requirements
- Installation
- Usage
- How the Program Works
- Code Structure
- Platform Compatibility
- Limitations
- Future Enhancements
- License

## Introduction

ASCII art is a graphic design technique that uses printable characters from the ASCII standard to create visual designs. This project demonstrates how ASCII art can be generated programmatically using Python by mapping characters to fixed-size patterns and printing them line by line in the terminal.
This project is suitable for beginners learning Python fundamentals such as dictionaries, loops, functions, and basic terminal interaction.

## Features

- Single Character mode to display one alphabet or digit as large ASCII art
- Words mode to display alphabetic text as ASCII art
- Numbers mode to display numeric strings of any length
- Predefined heart logo created using ASCII characters
- Predefined smile logo created using ASCII characters
- Colored output using the colorama library
- Menu-driven interface
- Instant keypress input using msvcrt.getch()
- Input validation for all modes

## Requirements

- Python 3.x
- Windows operating system
- colorama Python package

Install the dependency using:
`pip install colorama`

## Installation

- Download or clone the repository to your local system
- Ensure Python 3 is installed and available in PATH
- Install the required dependency (colorama)
- Open Command Prompt and navigate to the project directory
- Run the program using:

`python ascii_art.py`

## Usage

When the program starts, a menu is displayed. Use the number keys on your keyboard to select an option. Pressing Enter is not required, as the program reads keypresses instantly.

## Menu Options

- Single Character
Displays exactly one alphabet or digit as ASCII art.
- Words
Displays alphabetic words (spaces allowed) as ASCII art.
- Numbers
Displays numeric input of any length as ASCII art.
- Heart Logo
Displays a predefined heart-shaped ASCII logo.
- Smile Logo
Displays a predefined smiley face ASCII logo.
- Exit
Exits the program.

## Color Selection

- Red
- Green
- Yellow
- Blue
- Magenta
- Cyan
- White

The program uses colorama.init(autoreset=True) to automatically reset the terminal color after each print operation.

How the Program Works

- Each supported character (A–Z, 0–9, and space) is stored as a fixed-size ASCII pattern
- All ASCII patterns are created using the * character
- Characters are printed row by row so they appear side by side
- Input is validated before converting text into ASCII art

## Code Structure

- ASCII font dictionary containing character patterns
- Utility functions for clearing the screen, pausing execution, and selecting colors
- Separate functions for each menu mode
- Main menu loop for user navigation and control flow

## Platform Compatibility

- Designed specifically for Windows
- Uses the msvcrt module for instant keypress handling
- Not directly compatible with Linux or macOS without modification

## Limitations

- Only characters defined in the ASCII font dictionary are supported
- Input handling is Windows-specific
- Lowercase input is converted to uppercase automatically

## Future Enhancements

- Add more ASCII logos and symbols
- Implement animated ASCII art
- Add an option to save output to a file
- Make the program cross-platform
- Add gradient or multi-color text effects

### License

This project is released under the MIT License. It is free to use, modify, and distribute for educational and personal purposes
