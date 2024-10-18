import tkinter as tk
from tkinter import messagebox
import random

class WordleGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Wordle Game")
        self.geometry("400x300")
        
        self.configure(bg="lightblue") 
        
        self.hidden_word = ""
        self.attempts_left = 6
        
        self.game_instruction_label = tk.Label(self, text="Wordle is a single player game\n"
                                                          "A player has to guess a six-letter hidden word\n"
                                                          "You have six attempts\n"
                                                          "Your Progress Guide '✔❌❌✔➕'\n"
                                                          "'✔' Indicates that the letter at that position was guessed correctly\n"
                                                          "'➕' indicates that the letter at that position is in the hidden word, but in a different position\n"
                                                          "'❌' indicates that the letter at that position is wrong, and isn't in the hidden word",
                                               bg="lightblue", fg="navy", font=("Times New Roman", 10, "italic"))
        self.game_instruction_label.pack(pady=10)
        
        self.word_entry = tk.Entry(self, width=20)
        self.word_entry.pack()
        
        self.guess_button = tk.Button(self, text="Guess", command=self.check_word, bg="green", fg="white")
        self.guess_button.pack(pady=5)
        
        self.attempts_label = tk.Label(self, text=f"Attempts left: {self.attempts_left}", bg="lightblue", fg="navy", font=("Arial", 10, "bold"))
        self.attempts_label.pack()
        
        self.progress_label = tk.Label(self, text="Your Progress:", bg="lightblue", fg="navy", font=("Arial", 10, "bold"))
        self.progress_label.pack()
        
        self.progress_text = tk.Text(self, height=5, width=30, bg="white", fg="navy", font=("Arial", 10))
        self.progress_text.pack()
        
        self.new_game()
        
    def calculate_score(self, guess):
        score = 0
        for char, word in zip(self.hidden_word, guess):
            if word == char:
                score += 2
            elif word in self.hidden_word:
                score += 1
        return score
    
    def check_word(self):
        guess = self.word_entry.get().lower()
        
        if len(guess) != len(self.hidden_word):
            messagebox.showerror("Error", "The word is not the right length!")
            return
        
        if guess == self.hidden_word:
            messagebox.showinfo("Congratulations", "You guessed the word correctly! WIN 🕺🕺🕺")
            self.new_game()
            return
        
        self.attempts_left -= 1
        self.attempts_label.config(text=f"Attempts left: {self.attempts_left}")
        
        score = self.calculate_score(guess)
        
        self.progress_text.insert(tk.END, f"Your Score: {score}\n")
        for char, word in zip(self.hidden_word, guess):
            if word in self.hidden_word and (word == char):
                self.progress_text.insert(tk.END, f"{word} ✔ ")
            elif word in self.hidden_word:
                self.progress_text.insert(tk.END, f"{word} ➕ ")
            else:
                self.progress_text.insert(tk.END, f"{word} ❌ ")
        self.progress_text.insert(tk.END, "\n\n")
        
        if self.attempts_left == 0:
            messagebox.showinfo("Game Over", f"You lost! The word was {self.hidden_word}")
            self.new_game()
            return
        
        self.word_entry.delete(0, tk.END)
    
    def new_game(self):
        self.hidden_word = random.choice(['snails', 'apples', 'banana', 'cherry', 'orange', 'anyway', 'lemons', 'corner', 'skater', 'budget'])
        self.attempts_left = 6
        self.attempts_label.config(text=f"Attempts left: {self.attempts_left}")
        self.progress_text.delete(1.0, tk.END)

if __name__ == "__main__":
    app = WordleGame()
    app.mainloop()
