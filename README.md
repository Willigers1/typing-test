# Speed Typing Test

## Overview

The **Speed Typing Test** is a terminal-based application built using Python and the `curses` library. The goal is to measure how fast you can type a given text, displaying real-time results and calculating your **Words Per Minute (WPM)**. You can either test yourself with a default text or challenge yourself with randomly generated text.

## Features

- **Default Typing Text**: Practice with a preset text.
- **Random Text Generation**: Option to generate random text for a more dynamic typing test.
- **Real-Time WPM Calculation**: Tracks and updates your WPM as you type.
- **Visual Feedback**: Correct characters are highlighted in green, while incorrect characters are highlighted in red.
- **Backspace Support**: Fix your mistakes with backspace as you type.
- **Exit Option**: Press `Esc` to exit the test anytime.

## Technologies Used

- **Python 3**
- **Curses Library**: For handling the terminal user interface.

## How to Run the Project

### Prerequisites
1. **Python 3.x** must be installed. You can download it from [python.org](https://www.python.org/downloads/).
2. **Curses library** is required. It's available by default on Unix-based systems (Linux, macOS). On Windows, you may need to install the `windows-curses` package:
   ```bash
   pip install windows-curses
   ```

### Running the Program

1. Clone or download the repository:
   ```bash
   git clone https://github.com/your-username/speed-typing-test.git
   cd speed-typing-test
   ```

2. Run the Python script:
   ```bash
   python typing_test.py
   ```

3. Choose whether you want to type the **default text** or **generate random text**:
   - Press `r` for random text.
   - Press any other key to use the default text.

4. Start typing! You will see your WPM updated in real time.

5. After finishing the test, your final WPM will be displayed.

## Project Structure

```
├── typing_test.py   # Main Python file containing the typing test logic
└── README.md        # Documentation for the project
```

## How the Project Works

1. **Start Screen**: The user is greeted with a welcome screen where they choose between random text or default text.
2. **Typing Screen**: The text appears, and the user types while the program calculates WPM based on their progress.
3. **Visual Feedback**: Characters typed correctly appear green, incorrect characters appear red, and the remaining characters are shown as underscores.
4. **Exit**: The test ends when the user finishes typing the text or presses `Esc` to exit early.

## Example Usage

Here's a quick demo of how the application works in the terminal:

```
Welcome to the speed typing test!
Press 'r' for random text or any other key for default text.
```

Then the typing screen appears, with real-time feedback on how fast you type. When you're done:

```
Test finished!
Your WPM: 42
Press any key to exit.
```

## Future Improvements

- **Custom Text Input**: Allow users to input their own text for the typing test.
- **Difficulty Levels**: Add multiple difficulty levels with varying text complexity.
- **Leaderboard**: Implement a leaderboard to track best scores.

## Contributing

If you’d like to contribute to this project:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## License

This project is open-source and available under the **MIT License**. Feel free to use, modify, and distribute it as per the terms of the license.

---

Feel free to modify any of this content to suit your project more specifically!
