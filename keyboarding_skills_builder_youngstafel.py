# keyboarding_skills_builder_youngstafel_christopher
# Created on: 2024-09-22
# Author: Chris Youngstafel
# IDE: VS Code

# Pseudo code:
# Create a main window with a button to start the test
# Display a series of 10 random, non-repeating letters in new windows
# Prompt the user to press the key corresponding to the displayed letter
# Check if the user presses the correct key
# After 10 letters, show the user the number of correct answers

import tkinter as tk
import random
import string

# Global variables to track progress and results
letters_to_test = []
correct_answers = 0
attempted_tests = 0  # Track only the number of questions attempted
total_tests = 10
current_test = 0

# Function to generate 10 random unique letters
def generate_letters():
    global letters_to_test
    letters_to_test = random.sample(string.ascii_uppercase, total_tests)

# Function to center the window
def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x_position = int((screen_width / 2) - (width / 2))
    y_position = int((screen_height / 2) - (height / 2))
    window.geometry(f"{width}x{height}+{x_position}+{y_position}")

# Function to check user input and go to the next test
def check_input(event, displayed_letter, test_window):
    global correct_answers, attempted_tests, current_test
    user_input = event.char.upper()

    if user_input == displayed_letter:
        correct_answers += 1
    attempted_tests += 1

    current_test += 1
    test_window.destroy()

    if current_test < total_tests:
        show_test_window()
    else:
        show_results()

# Function to show a test window with a letter and entry prompt
def show_test_window():
    test_window = tk.Toplevel(window)
    test_window.title("Keyboard Test")
    center_window(test_window, 300, 150)
    test_window.configure(bg="#D3D3D3")
    test_window.focus_set()

    letter = letters_to_test[current_test]

    # Display the letter to the user
    label = tk.Label(test_window, text=f"Press the key for: {letter}", font=("Helvetica", 24), bg="#D3D3D3")
    label.pack(pady=20)

    # Bind the key press event to check the user's input
    test_window.bind("<Key>", lambda event: check_input(event, letter, test_window))

    # End the test early
    end_button = tk.Button(test_window, text="End Test Early", command=lambda: end_early(test_window))
    end_button.pack(pady=10)

# Function to end the test early and show results
def end_early(test_window):
    test_window.destroy()  # Close the current test window
    show_results()

# Function to show the results
def show_results():
    result_window = tk.Toplevel(window)
    result_window.title("Test Results")
    center_window(result_window, 300, 150)
    result_window.configure(bg="#90EE90")

    result_label = tk.Label(result_window, text=f"You got {correct_answers} out of {attempted_tests} correct!", font=("Helvetica", 18), bg="#90EE90")
    result_label.pack(pady=30)

# Function to start the test
def start_test():
    global correct_answers, current_test, attempted_tests
    correct_answers = 0
    current_test = 0
    attempted_tests = 0
    generate_letters()
    show_test_window()

# Function to set up the main window
def main():
    global window

    window = tk.Tk()
    window.title("Keyboard Test App")
    center_window(window, 400, 300)
    window.configure(bg="#ADD8E6")

    # Branding label
    label = tk.Label(window, text="Welcome to the Keyboard Test!", bg="#ADD8E6", font=("Helvetica", 16))
    label.pack(pady=40)

    # Start test button
    start_button = tk.Button(window, text="Start Test", command=start_test, font=("Helvetica", 14))
    start_button.pack(pady=20)

    window.mainloop()

# Start the program
if __name__ == "__main__":
    main()