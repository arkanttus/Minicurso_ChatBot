from chatterbot import ChatBot
from chatterbot.comparisons import LevenshteinDistance
from chatterbot.response_selection import get_first_response
from chatterbot.languages import POR

chatbot = ChatBot(
    "My ChatterBot",
    language=POR,
    logic_adapters=[
        {
            "import_path": "chatterbot.logic.BestMatch",
            "statement_comparison_function": LevenshteinDistance,
            "response_selection_method": get_first_response
        },
        {
            'import_path': 'adapter.TemperatureAdapter'
        },
        {
            'import_path': 'chatterbot.logic.MathematicalEvaluation',
        },
    ]
)
