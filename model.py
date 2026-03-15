import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

stop_words = set(stopwords.words('english'))

emotion_keywords = {
    "anxiety": ["anxious","nervous","exam","worried"],
    "sadness": ["sad","depressed","unhappy"],
    "stress": ["stress","pressure","tired"],
    
    "anger": ["angry","mad","furious","annoyed","irritated","frustrated"],

    "fear": ["afraid","fear","terrified","scared","frightened"],

    "loneliness": ["alone","lonely","isolated","nobody","empty"],

    "confusion": ["confused","lost","uncertain","unsure","doubt"],

    "motivation": ["motivation","inspire","improve","success","goal","dream"],

    "happiness": ["happy","joy","great","good","excited","wonderful","amazing"],

       }

responses = {
    "anxiety": "It's normal to feel anxious about exams. Try deep breathing and take short breaks.",
    "sadness": "It's okay to feel sad sometimes. Talk to someone you trust.",
    "stress": "Take some rest and relax.",
    "default": "Tell me more about how you feel.",
     "anger": "I understand you're feeling angry. Try to take deep breaths and step away from the situation for a moment.",

    "fear": "Feeling afraid is natural. Remember that you are safe and you can overcome challenges step by step.",

    "loneliness": "Feeling lonely can be hard. Try reaching out to friends, family, or doing activities you enjoy.",

    "confusion": "It's okay to feel confused sometimes. Take your time and try to think through the situation calmly.",

    "motivation": "Stay positive and keep working toward your goals. Small steps lead to big success.",

    "happiness": "That's wonderful to hear! Keep enjoying the positive moments in life.",
    


}

def process_input(text):

    text = text.lower()

    tokens = word_tokenize(text)

    tokens = [word for word in tokens if word not in stop_words and word not in string.punctuation]

    important_words = tokens

    detected_emotion = "default"

    for emotion, words in emotion_keywords.items():
        for word in important_words:
            if word in words:
                detected_emotion = emotion

    response = responses.get(detected_emotion, responses["default"])

    return important_words, detected_emotion, response