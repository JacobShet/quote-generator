import random

# Make a list of the quotes to pull from
quotes = [
    ("Perfection is not attainable, but if we chase perfection we can catch excellence.", "Vince Lombardi"),
    ("Believe you can, and you're halfway there.", "Theodore Roosevelt"),
    ("It is during our darkest moments that we must focus to see the light.", "Aristotle Onassis"),
    ("There is nothing impossible to him who will try", "Alexander the Great"),
    ("Your present circumstances don't determine where you can go; they merely determine where you start.", "Nido Qubein"),
    ("Be faithful to that which exists within yourself.", "Andre Gide"),
    ("What we think, we become.", "Buddha"),
    ("It is only in sorrow bad weather masters us; in joy we face the storm and defy it.", "Amelia Barr"),
    ("Reach for it. Push yourself as far as you can.", "Christa McAuliffe"),
    ("It always seems impossible until it's done.", "Nelson Mandela"),
    ("Start where you are. Use what you have. Do what you can.", "Arthur Ashe"),
    ("Problems are not stop signs, they are guidelines.", "Robert H. Schuller"),
    ("Accept the challenges so that you can feel the exhilaration of victory.", "George S. Patton"),
    ("Setting goals is the first step in turning the invisible into the visible.", "Tony Robbins"),
    ("No bird soars too high if he soars with his own wings.", "William Blake")
]

# Assign a random quote to a variable
random_quote = random.choice(quotes)

# Split the tuple into two variables to allow easier formatting
quote, author = random_quote

# Print the random quote in an easy to read format
print("=" * 40)
print(f'"{quote}" --{author}')
print("=" * 40)