# GeoGenius-USA 🗺️

Learn all 50 U.S. states in a fun and interactive way!

---

## How to Play

1. Run the game:

   ```bash
   python main.py
   ```
2. A blank U.S. map will appear.
3. Type the name of a state when prompted.
4. Correct guesses are displayed on the map.
5. Keep guessing until all 50 states are named.
6. Type `"Exit"` anytime to end the game. A file called `states_to_learn.csv` will be generated with the states you missed.

---

## Features

* Interactive map with state names displayed at correct locations.
* Keeps track of your correct guesses.
* Generates a CSV file of missed states to help you learn.
* Simple and user-friendly gameplay.

---

## Installation

1. **Clone the repository:**

   ```bash
   git clone <repository_url>
   cd GeoGenius
   ```
2. **Install required packages:**

   ```bash
   pip install pandas
   ```
3. **Required files:**

   * `50_states.csv` – contains state names and coordinates
   * `blank_states_img.gif` – blank map of the U.S.

---

## How It Works

1. The script uses **pandas** to read state data including names and coordinates.
2. A **turtle** window displays a blank U.S. map.
3. Users input guesses in a loop until all states are guessed or they exit.
4. Correct guesses are written onto the map using turtle at the specified coordinates.
5. On exit, a CSV file `states_to_learn.csv` is created for states not guessed.

---

## Contributing

Contributions are welcome! You can help by:

* Adding new features (e.g., hints, timer).
* Improving the user interface.
* Fixing bugs or optimizing code.

---

## License

This project is **open-source** 

---

## Enjoy learning U.S. geography! 🎉
