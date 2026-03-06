import random

compliments = [
    "You make difficult things look easy.",
    "Your creativity has no off switch.",
    "You bring good energy wherever you go.",
    "You learn faster than you realize.",
    "Your ideas are always worth hearing.",
    "You have a talent for making people feel comfortable.",
    "Your curiosity is one of your superpowers.",
    "You’re more capable than you give yourself credit for.",
    "You have a great sense of humor.",
    "You notice details others miss.",
    "You’re the kind of person people trust instantly.",
    "Your perspective is refreshing.",
    "You’re genuinely fun to talk to.",
    "You handle challenges with style.",
    "You’re growing every single day.",
    "You make smart decisions.",
    "You’re surprisingly good at figuring things out.",
    "You have a calming presence.",
    "You’re full of potential.",
    "You’re better at this than you think.",
    "You’re someone people want on their team.",
    "You’re brave enough to try.",
    "You’re interesting in the best way.",
    "You have a natural spark.",
    "You’re thoughtful and it shows.",
    "You’re the kind of person who makes things happen.",
    "You’re easy to root for.",
    "You’re sharper than you look.",
    "You’re the definition of quietly impressive.",
    "You’re doing great — even if you don’t always feel it."
]

while True:
    name = input("What is your name? ").strip()

    if not name:
        print("Please enter a valid name.")
        continue

    print(f"{name}, {random.choice(compliments)}")

    go_again = input("Would you like another compliment? (y/n): ").strip().lower()
    if go_again not in {"y", "yes"}:
        print("Thanks for using the compliment generator. Have a great day!")
        break
