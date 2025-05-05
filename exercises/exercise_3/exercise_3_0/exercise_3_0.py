# Exercise 3 - Taipy for creating web apps

# 0. Palindrome game

# A palindrome is a set of characters that is read the same backwards as forwards.
# Example of palindromes (case-insensitive and ignoring spaces):

# Anna
# racecar
# Ni talar bra latin

# Your task is to create a palindrome game in Taipy, where the user can input a string and a button to submit the input.
# The written string should also be displayed in a text instantaneously.

# After clicking the submit button, the game displays a GPT4o-generated cat image if it is a palindrome.

# If it is not a palindrome, then a GPT4o-generated sad bunny is shown

# Also keep track of points, give one star for each correct answer and deduct one star for each incorrect answer.
# You can choose an appropriate icon/emoji/image for negative scores.

# Something else you want your palindrome game to have - go ahead and try implement it?

from taipy.gui import Gui
import taipy.gui.builder as tgb
from pathlib import Path

assets_path = Path(__file__).parent / "assets"

image_url = ""
input_text = ""
display_text = ""
result_text = ""
score = 0

def on_text_change(state, var_name, var_value):
    state.input_text = var_value
    state.display_text = var_value


def on_submit(state):
    if is_palindrome(state.input_text):
        state.image_url = "./fake_cat.png"
        state.score += 1
        state.result_text = "**Good work**, that was a Palindrome!"
    else:
        state.image_url = "./fake_sad_rabbit.png"
        state.score -= 1
        state.result_text = "That was not a Palindrome, **Try again**!"


def is_palindrome(text):
    clean_text = "".join(c.lower() for c in text if c.isalnum())
    return clean_text == clean_text[::-1]


with tgb.Page() as page:
    tgb.text("## Palindrome Game", mode="md")
    tgb.text("Input your text below:")
    tgb.input(value="{input_text}", on_change=on_text_change)
    tgb.text("**You Wrote:**", mode="md")
    tgb.text("{display_text}")
    tgb.text("**Score:** {score}", mode="md")
    tgb.text("{result_text}", mode="md")
    tgb.button("Check!", on_action=on_submit)
    tgb.image("{image_url}", width="300px", default_value="")

if __name__ == "__main__":
    Gui(pages={"/": page}).run(
        dark_mode=True,
        use_reloader=True,
        port=8080
    )