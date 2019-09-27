from bot import chatbot

while True:
    user = input("Voce: ")
    response = chatbot.get_response(user)
    print("Bot: " + str(response))
    print("Confidence: " + str(response.confidence))
