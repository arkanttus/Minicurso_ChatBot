from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot("Meu chat")

trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train('./cumpliments.yml')

while True:
    user = input("Voce: ")
    response = chatbot.get_response(user)
    print("Bot: " + str(response))
    print("Confidence: " + str(response.confidence))
