import tkinter as tk
from tkinter import messagebox
import random

# Function to determine the winner
def determine_winner(user_choice):
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    result = ""
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        result = "You win!"
        global user_score
        user_score += 1
    else:
        result = "You lose!"
        global computer_score
        computer_score += 1
    result_label.config(text=f"You chose: {user_choice}\nComputer chose: {computer_choice}\n{result}")
    score_label.config(text=f"Score - You: {user_score} Computer: {computer_score}")

# Function to reset the game
def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    result_label.config(text="Make your choice!")
    score_label.config(text=f"Score - You: {user_score} Computer: {computer_score}")

# Function to handle the user's choice
def user_choice(choice):
    determine_winner(choice)

# Initialize the main window
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")

# Initialize scores
user_score = 0
computer_score = 0

# Create and place labels and buttons
tk.Label(root, text="Choose Rock, Paper, or Scissors:", font=("Helvetica", 14)).pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=10)

rock_button = tk.Button(frame, text="Rock", command=lambda: user_choice('rock'), width=10)
rock_button.grid(row=0, column=0, padx=5)

paper_button = tk.Button(frame, text="Paper", command=lambda: user_choice('paper'), width=10)
paper_button.grid(row=0, column=1, padx=5)

scissors_button = tk.Button(frame, text="Scissors", command=lambda: user_choice('scissors'), width=10)
scissors_button.grid(row=0, column=2, padx=5)

result_label = tk.Label(root, text="Make your choice!", font=("Helvetica", 12))
result_label.pack(pady=10)

score_label = tk.Label(root, text=f"Score - You: {user_score} Computer: {computer_score}", font=("Helvetica", 12))
score_label.pack(pady=10)

reset_button = tk.Button(root, text="Reset Game", command=reset_game, width=20)
reset_button.pack(pady=10)

# Run the main loop
root.mainloop()
