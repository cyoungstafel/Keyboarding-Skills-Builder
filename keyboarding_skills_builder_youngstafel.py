# keyboarding_skills_builder_youngstafel.py
# Created on: 2024-10-11
# Author: Chris Youngstafel
# IDE: VS Code

# Import necessary libraries: tkinter, PIL (for images), random, string, and os
# Import messagebox from tkinter for displaying dialog boxes

# Define global variables:
#   letters_to_test: stores the randomly generated letters
#   correct_answers: number of correct answers
#   attempted_tests: number of attempted tests
#   total_tests: total tests (10)
#   current_test: current test number
#   student_name: store student's name
#   missed_letters: letters missed during the test

# File to save and load the test results - test_results.txt
# File to load the user manual - user_manual.txt

# Define function to generate 10 random lowercase letters
# Define function to center the window on the screen
# Define function to check the user's input and move to the next test
# Define function to show the test window
# Define function to end the test early
# Define function to display the test results
# Define function to start the test
# Define function to load previous test results from the file
# Define function to read the user manual from the file
# Define function to calculate and display total results
# Define main function to set up the main window
# Call the main function to start the program

import tkinter as tk
import tkinter.messagebox as messagebox
import random
import string
from PIL import Image, ImageTk
import os

# Global variables
letters_to_test = []
correct_answers = 0
attempted_tests = 0
total_tests = 10
current_test = 0
student_name = ""
missed_letters = []

# Text files to be used
results_file = "test_results.txt"
manual_file = "user_manual.txt"

# Function to generate 10 random lowercase unique letters
def generate_letters():
    global letters_to_test
    letters_to_test = random.sample(string.ascii_lowercase, total_tests)

# Function to center the window
def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x_position = int((screen_width / 2) - (width / 2))
    y_position = int((screen_height / 2) - (height / 2))
    window.geometry(f"{width}x{height}+{x_position}+{y_position}")

# Function to check input and go to the next test
def check_input(event, displayed_letter, test_window):
    global correct_answers, attempted_tests, current_test, missed_letters
    user_input = event.char.lower()

    # Check if the user's input matches the displayed letter
    if user_input == displayed_letter:
        correct_answers += 1
    else:
        missed_letters.append(displayed_letter)

    attempted_tests += 1
    current_test += 1
    test_window.destroy()

    if current_test < total_tests:
        show_test_window()
    else:
        show_results()

# Function to show a test window
def show_test_window():
    test_window = tk.Toplevel(window)
    test_window.title("Keyboard Test")
    center_window(test_window, 300, 150)
    test_window.configure(bg="#D3D3D3")
    test_window.focus_set()

    letter = letters_to_test[current_test]

    # Display the letter
    label = tk.Label(test_window, text=f"Press the key for: {letter}", font=("Helvetica", 24), bg="#D3D3D3")
    label.pack(pady=20)

    # Bind the key press event
    test_window.bind("<Key>", lambda event: check_input(event, letter, test_window))

    # End the test early
    end_button = tk.Button(test_window, text="End Test Early", command=lambda: end_early(test_window))
    end_button.pack(pady=10)

# Function to end the test early
def end_early(test_window):
    test_window.destroy()
    show_results()

# Function to show the results
def show_results():
    global student_name

    # Create and append to the results file
    with open(results_file, "a") as file:
        file.write(f"Student: {student_name}, Correct: {correct_answers}, Attempted: {attempted_tests}, Missed: {', '.join(missed_letters)}\n")

    result_window = tk.Toplevel(window)
    result_window.title("Test Results")
    center_window(result_window, 400, 400)
    result_window.configure(bg="#2f2f2f")

    result_label = tk.Label(result_window, text=f"You got {correct_answers} out of {attempted_tests} correct!", font=("Helvetica", 18), bg="#2f2f2f", fg="white")
    result_label.pack(pady=10)

    # Display missed letters
    if missed_letters:
        missed_label = tk.Label(result_window, text=f"Missed Letters: {', '.join(missed_letters)}", font=("Helvetica", 14), bg="#2f2f2f", fg="white")
        missed_label.pack(pady=10)
    else:
        missed_label = tk.Label(result_window, text="Great job! No missed letters.", font=("Helvetica", 14), bg="#2f2f2f", fg="white")
        missed_label.pack(pady=10)

    # Image in results window
    image = Image.open("SirenHead.jpg")
    image = image.resize((150, 150), Image.Resampling.LANCZOS)
    img = ImageTk.PhotoImage(image)
    image_label = tk.Label(result_window, image=img, bg="#2f2f2f")
    image_label.image = img
    image_label.pack(pady=10)

    # Alternate text
    alt_text_label = tk.Label(result_window, text="Image of Siren Head", font=("Helvetica", 10), bg="#2f2f2f", fg="white")
    alt_text_label.pack()

    # Results window close button
    close_button = tk.Button(result_window, text="Close", command=result_window.destroy, font=("Helvetica", 14), bg="#2f2f2f", fg="white")
    close_button.pack(pady=10)

# Function to start the test
def start_test():
    global correct_answers, current_test, attempted_tests, student_name, missed_letters
    student_name = name_entry.get()
    if not student_name:
        # If no name is entered
        messagebox.showwarning("Input Error", "Please enter your name to start the test.")
        return
    correct_answers = 0
    current_test = 0
    attempted_tests = 0
    missed_letters = []
    name_entry.delete(0, tk.END)
    generate_letters()
    show_test_window()

# Function to load the previous results
def load_results():
    if os.path.exists(results_file):
        with open(results_file, "r") as file:
            results = file.read().strip()
        if results:
            results_window = tk.Toplevel(window)
            results_window.title("Previous Results")
            center_window(results_window, 400, 300)
            results_window.configure(bg="#FFFACD")

            results_label = tk.Label(results_window, text="Previous Test Results", font=("Helvetica", 16), bg="#FFFACD")
            results_label.pack(pady=10)

            results_text = tk.Text(results_window, wrap="word", font=("Helvetica", 12))
            results_text.insert(tk.END, results)
            results_text.config(state="disabled")
            results_text.pack(pady=10)

            close_button = tk.Button(results_window, text="Close", command=results_window.destroy)
            close_button.pack(pady=10)
        else:
            messagebox.showinfo("No Results", "No previous results found.")
    else:
        messagebox.showinfo("No Results", "No previous results found.")

# Function to load the user manual
def read_manual():
    if os.path.exists(manual_file):
        with open(manual_file, "r") as file:
            manual_text = file.read()
        manual_window = tk.Toplevel(window)
        manual_window.title("User Manual")
        center_window(manual_window, 600, 400)
        manual_window.configure(bg="#FFFACD")

        manual_label = tk.Label(manual_window, text="User Manual", font=("Helvetica", 16), bg="#FFFACD")
        manual_label.pack(pady=10)

        manual_content = tk.Text(manual_window, wrap="word", font=("Helvetica", 12))
        manual_content.insert(tk.END, manual_text)
        manual_content.config(state="disabled")
        manual_content.pack(pady=10)

        close_button = tk.Button(manual_window, text="Close", command=manual_window.destroy)
        close_button.pack(pady=10)
    else:
        messagebox.showinfo("No Manual", "User manual not found.")

# Function to calculate and display previous results
def calculate_results():
    if os.path.exists(results_file):
        with open(results_file, "r") as file:
            results = file.read().strip()
        if results:
            total_correct = 0
            total_attempted = 0
            with open(results_file, "r") as file:
                for line in file:
                    # Extract correct and attempted results
                    parts = line.split(", ")
                    for part in parts:
                        if part.startswith("Correct:"):
                            total_correct += int(part.split(":")[1].strip())
                        elif part.startswith("Attempted:"):
                            total_attempted += int(part.split(":")[1].strip())

            # Display the totals
            calc_window = tk.Toplevel(window)
            calc_window.title("Total Results")
            center_window(calc_window, 300, 150)
            calc_window.configure(bg="#D3D3D3")

            calc_label = tk.Label(calc_window, text=f"Total Correct: {total_correct}\nTotal Attempted: {total_attempted}", font=("Helvetica", 16), bg="#D3D3D3")
            calc_label.pack(pady=20)

            close_button = tk.Button(calc_window, text="Close", command=calc_window.destroy)
            close_button.pack(pady=10)
        else:
            messagebox.showinfo("No Results", "No previous results found.")
    else:
        messagebox.showinfo("No Results", "No previous results found.")

# Function for the main window
def main():
    global window, name_entry

    window = tk.Tk()
    window.title("Keyboard Test App")
    center_window(window, 400, 600)
    window.configure(bg="#2f2f2f")

    # Branding label
    label = tk.Label(window, text="Welcome to the Keyboard Test!", bg="#2f2f2f", fg="white", font=("Helvetica", 16))
    label.pack(pady=20)

    # Field to enter student name
    name_label = tk.Label(window, text="Enter your name:", font=("Helvetica", 14), bg="#2f2f2f", fg="white")
    name_label.pack(pady=10)
    name_entry = tk.Entry(window, font=("Helvetica", 14))
    name_entry.pack(pady=10)

    # Image for the main window
    image = Image.open("ChooChooCharles.jpg")
    image = image.resize((150, 150), Image.Resampling.LANCZOS)
    img = ImageTk.PhotoImage(image)
    image_label = tk.Label(window, image=img)
    image_label.image = img
    image_label.pack(pady=10)

    # Alternate text
    alt_text_label = tk.Label(window, text="Image of Choo Choo Charles", font=("Helvetica", 10), bg="#2f2f2f", fg="white")
    alt_text_label.pack()

    # Start test button
    start_button = tk.Button(window, text="Start Test", command=start_test, font=("Helvetica", 14))
    start_button.pack(pady=10)

    # Previous results button
    load_results_button = tk.Button(window, text="Load Previous Results", command=load_results, font=("Helvetica", 14))
    load_results_button.pack(pady=10)

    # Total results button
    calc_results_button = tk.Button(window, text="Calculate Total Results", command=calculate_results, font=("Helvetica", 14))
    calc_results_button.pack(pady=10)

    # Read the user manual
    manual_button = tk.Button(window, text="Read User Manual", command=read_manual, font=("Helvetica", 14))
    manual_button.pack(pady=10)

    window.mainloop()

# Start the program
if __name__ == "__main__":
    main()
