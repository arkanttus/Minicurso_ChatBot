from chatterbot import ChatBot

chatbot = ChatBot('Irineu')

while True:
    try:
        user = input("Voce: ")
        response = chatbot.get_response(user)
        print("bot: " + str(response))
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
