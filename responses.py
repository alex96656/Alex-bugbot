import random

HELLO = [
    "👋 Heyyy",
    "🎀 Hello there",
    "😊 Hi hi",
    "🤖 I'm here"
]

ROAST = [
    "🎀 did you lose your typing fingers or what?",
    "💞 that message took centuries to type huh?",
    "🥹 be honest… you just stared at the screen",
    "😹 your keyboard is crying right now"
]

LOVE_VIBES = [
    "💞 group romance detected...",
    "🎀 love energy is crazy here",
    "🥹 emotional damage loading..."
]

BOT_REPLY = [
    "🤖 yes?",
    "👀 I'm listening...",
    "⚡ say it again"
]


def pick(list_data):
    return random.choice(list_data)