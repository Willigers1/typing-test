import curses
from curses import wrapper
import time
import random
import string

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to the speed typing test! ")
    stdscr.addstr("\nPress 'r' for random text or any other key for default text. ")
    stdscr.refresh()
    key = stdscr.getkey()
    return key

def generate_random_text(length=50):
    words = ["".join(random.choices(string.ascii_lowercase, k=random.randint(3, 8))) for _ in range(length // 5)]
    return " ".join(words)

def display_text(stdscr, target, current, wpm=0):
    stdscr.clear()
    stdscr.addstr(f"WPM: {wpm}\n")
    stdscr.addstr(target + "\n")

    for i, char in enumerate(current):
        correct_char = target[i] if i < len(target) else ""
        if char == correct_char:
            stdscr.addstr(char, curses.color_pair(1))  # Green for correct letters
        else:
            stdscr.addstr(char, curses.color_pair(2))  # Red for incorrect letters

    # Add spaces for the remaining target text that hasn't been typed
    for i in range(len(current), len(target)):
        stdscr.addstr("_", curses.color_pair(3))  # Display remaining target as underscores

    stdscr.refresh()

def wpm_test(stdscr, target_text):
    current_text = []
    wpm = 0
    start_time = time.time()

    stdscr.nodelay(True)  # Makes getkey non-blocking
    while True:
        time_elapsed = max(time.time() - start_time, 1)  # Avoid division by zero
        wpm = round((len(current_text) / 5) / (time_elapsed / 60))

        display_text(stdscr, target_text, current_text, wpm)

        try:
            key = stdscr.getkey()
        except:
            key = None

        if key is None:
            continue

        if ord(key) == 27:  # Escape key to exit
            break

        if key in ("KEY_BACKSPACE", '\b', "\x7f"):
            if len(current_text) > 0:
                current_text.pop()
        elif len(current_text) < len(target_text):
            current_text.append(key)

        # End the test if the user finishes typing the target text
        if "".join(current_text) == target_text:
            stdscr.nodelay(False)
            break

    # Once finished, display final result
    stdscr.nodelay(False)
    time_elapsed = time.time() - start_time
    wpm = round((len(current_text) / 5) / (time_elapsed / 60))
    stdscr.clear()
    stdscr.addstr(f"Test finished!\nYour WPM: {wpm}\n")
    stdscr.addstr("Press any key to exit.")
    stdscr.refresh()
    stdscr.getkey()

def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)  # Correct chars in green
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)    # Incorrect chars in red
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)  # Remaining text in white

    key = start_screen(stdscr)

    # Generate random text or use default based on user's choice
    if key == 'r':
        target_text = generate_random_text()
    else:
        target_text = "Hello world this is some test text for this app"
    
    wpm_test(stdscr, target_text)

wrapper(main)
