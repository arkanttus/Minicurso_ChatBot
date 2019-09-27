from chatterbot.logic import LogicAdapter
import my_functions

class TemperatureAdapter(LogicAdapter):

    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)

    def can_process(self, statement):
        """
        Return true if the input statement contains
        'what' and 'is' and 'temperature'.
        """
        words = ['Qual', 'temperatura']
        if all(x in statement.text.split() for x in words):
            return True
        else:
            return False

    def process(self, input_statement, additional_response_selection_parameters):
        from chatterbot.conversation import Statement
        import requests

        # Make a request to the temperature API
        response = requests.get('https://api.hgbrasil.com/weather?woeid=447216')
        data = response.json()

        # Let's base the confidence value on if the request was successful
        if response.status_code == 200:
            confidence = 1
        else:
            confidence = 0

        temperature = data.get('results', 'indisponivel')
        temperature = temperature['temp']

        response_statement = Statement(text='A temperatura atual é de {} graus celsius'.format(temperature))
        response_statement.confidence = confidence

        return response_statement
