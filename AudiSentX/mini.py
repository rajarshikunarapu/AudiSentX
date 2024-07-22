from textblob import TextBlob
from dataclasses import dataclass

@dataclass
class Mood:
    emoji: str
    sentiment: float

def get_mood(input_text: str, threshold: float) -> Mood:
    sentiment = TextBlob(input_text).sentiment.polarity
    friendly_threshold = threshold
    hostile_threshold = -threshold
    if sentiment >= friendly_threshold:
        return Mood('😊', sentiment)
    elif sentiment <= hostile_threshold:
        return Mood('😡', sentiment)
    else:
        return Mood('😐', sentiment)

if _name_ == "_main_":
    while True:
        text = input('Text: ')
        mood = get_mood(text, threshold=0.5)
        print(f"{mood.emoji} ({mood.sentiment})")