from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot("Meu chat")

conversation = [
    "Ola",
    "Oi!",
    "Como voce esta?",
    "Eu estou bem",
    "Que bom",
    "Obrigado.",
    "Por nada"
]

trainer = ListTrainer(chatbot)
trainer.train(conversation)

while True:
    user = input("Voce: ")
    response = chatbot.get_response(user)
    print("Bot: " + str(response))
