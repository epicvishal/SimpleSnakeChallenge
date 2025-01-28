# Advanced Snake Game 🐍

A modern, engaging Snake Game built using Python and the `pygame` library. Navigate the snake to collect food, grow your length, and achieve the highest score while avoiding collisions with walls and yourself. A fun and nostalgic gaming experience reimagined for today!

---

## Features
- **Classic Gameplay:** Enjoy the timeless mechanics of Snake with a polished look.
- **Keyboard Controls:** Use arrow keys to control the snake seamlessly.
- **High Scores:** Compete with yourself by tracking and displaying the highest scores.
- **Custom Graphics:** Includes a custom icon for a professional touch.
- **Executable Application:** Play the game as a standalone Windows application without needing Python installed.

---
### Game Interface
![Game Screenshot ]([Image](https://github.com/user-attachments/assets/8953785b-3018-4641-aac6-6d85e816a901))
## How to Play
1. Launch the game from the executable or by running the Python script.
2. Use the **arrow keys** to move the snake:
   - **Arrow Up:** Move Up
   - **Arrow Down:** Move Down
   - **Arrow Left:** Move Left
   - **Arrow Right:** Move Right
3. Collect food to grow the snake and increase your score.
4. Avoid colliding with walls or the snake's body.
5. Aim to beat your high score!

---

## Installation and Execution
### Prerequisites
- **Python 3.x** installed on your system.
- **Pygame** library installed.

### Installation Steps
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/snake-game.git
   cd snake-game
   ```
2. Install dependencies:
   ```bash
   pip install pygame
   ```
3. Run the game:
   ```bash
   python advanced_snake.py
   ```

---

## Creating a Standalone Windows Application

Follow these steps to convert the Python game into an executable application for Windows:

### Step 1: Install Pygame
Open Command Prompt and install the Pygame library:
```bash
pip install pygame
```

### Step 2: Create the Executable
Use PyInstaller to convert the Python script into a `.exe` file:
```bash
pyinstaller --onefile --windowed --hidden-import=pygame --icon=snake_icon.ico advanced_snake.py
```
- `--onefile`: Creates a single executable file.
- `--windowed`: Runs the application without displaying a command prompt.
- `--hidden-import=pygame`: Ensures Pygame is bundled correctly.
- `--icon=snake_icon.ico`: Adds a custom icon for the application.

### Step 3: Verify Installation
Check if Pygame is installed by running:
```bash
pip list | findstr "pygame"
```

---

## Common Fixes
### Issue: Pygame Not Found
- Ensure the Pygame library is installed.
- If using a virtual environment, activate it first.

### Issue: Multiple Python Versions
- Use `pip3` instead of `pip` if multiple Python versions are installed.

### Issue: Permission Denied
- Run Command Prompt as Administrator.

### Alternative Approach
To bundle Pygame directly into your EXE file for a standalone application:
```bash
pyinstaller --onefile --windowed --hidden-import=pygame --add-data "venv/Lib/site-packages/pygame;pygame" --icon=snake_icon.ico advanced_snake.py
```
This ensures all Pygame dependencies are included in the executable.

### Locate the Executable
After running PyInstaller, you will find the compiled `.exe` file in the `dist` folder:
- Navigate to `dist`.
- Locate `advanced_snake.exe`.
- Run the file to play the game.

---

## Contributing
Contributions are welcome! Feel free to fork the repository and submit pull requests with improvements or bug fixes.


---

## Credits
- **Developer:** Vishal Kumar
- **Code Assistance:** DeepSeek AI
- **Libraries Used:** Python, Pygame
