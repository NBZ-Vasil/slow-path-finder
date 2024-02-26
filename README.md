# Shortest Route Tracer

## Overview

This Python program uses the Raylib library to visualize and find the shortest route between points using a brute-force approach. My plan is to reimplement this in another repo with a better search algorithm. This program implements [Heap's algorithm](https://en.wikipedia.org/wiki/Heap's_algorithm) for generating permutations.

## Installation

1. Clone or download the project repository to your local machine.
2. Navigate to the project directory in your terminal.
3. Ensure you have Python installed on your system (version 3.11 recommended).
4. Install the required dependencies listed in `requirements.txt` (using a virtual environment is best). You can install them using pip:
   ```
   pip install -r requirements.txt
   ```

## How to Run

1. Run the `main.py` script:
   ```
   python main.py
   ```
2. The GUI window will open, allowing you to interact with the program.

## Usage

- Add points by clicking anywhere in the window.
- Click the "Start" button to find the shortest route using a brute-force algorithm.
- The program will display the current best distance and update it if a shorter route is found.
- Once the simulation is complete, the final best distance will be displayed in red.

## Dependencies

- cffi==1.16.0
- inflection==0.5.1
- ordered-set==4.1.0
- pycparser==2.21
- raylib==5.0.0.1
- zstandard==0.22.0

## License

This project is licensed under the [MIT License](LICENSE).
