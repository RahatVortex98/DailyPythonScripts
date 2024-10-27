def get_input(word_type: str):
    user_input: str = input(f"Enter a {word_type}: ")
    return user_input

# Get user inputs
noun1 = get_input("noun")  # Character 1
noun2 = get_input("noun")  # Character 2
verb1 = get_input("verb")   # Action 1
verb2 = get_input("verb")   # Action 2
adjective1 = get_input("adjective")  # Description 1
adjective2 = get_input("adjective")  # Description 2
place = get_input("place")  # Setting
emotion = get_input("emotion")  # Emotion
time_period = get_input("time period")  # Time setting

# Create the story using formatted strings
story = f"""Once upon a time, in a {adjective1} {place}, there lived a {noun1} named Charlie. 
Charlie was known for his adventurous spirit and often dreamt of flying high above the clouds.

One sunny day, while wandering through the enchanted forest, Charlie met a {adjective2} {noun2} named Bella. 
Bella was graceful and loved to {verb1}. 

Charlie approached Bella and said, "Hello! I am Charlie the {noun1}. What do you like to do?" 

Bella replied, "Hi, Charlie! I’m Bella, the {noun2}. I love to {verb1}. Would you like to join me?"

Excited, Charlie exclaimed, "That sounds amazing! I wish I could {verb2} with you!" 

Bella smiled and said, "We can do anything if we put our minds to it. Let’s fly together and see the world!"

As they soared through the sky, Charlie felt a rush of {emotion}. They flew over mountains and rivers, exploring new lands. 

After hours of adventure, Bella said, "Charlie, do you remember when we first met? It was such a {adjective2} day."

Charlie nodded and replied, "Yes, I was feeling a bit {emotion} before I met you. But now, with you, I feel free!"

They both laughed and continued to {verb2} joyfully. 

At the end of the day, they found a cozy spot in the clouds to rest. Bella looked at Charlie and said, "Let’s promise to always have adventures together, no matter what happens in the {time_period}."

Charlie agreed, "Yes! I promise we will always explore the skies and face any challenges that come our way."

And from that day on, Charlie the {noun1} and Bella the {noun2} became the best of friends, embarking on countless adventures, spreading joy and laughter wherever they went. 
And they lived {emotion} ever after!"""

# Print the story
print(story)
