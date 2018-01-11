import random
EMPTY_QUOTES_MESSAGE: str = "No quotes were found :("
QUOTES_MARKDOWN = "```"
class Quotes():

    quotes_dict = {}

    def __init__(self, quotes_load: dict, wrap: bool = True):
        if wrap:
            for key, value in quotes_load:
                self.quotes_dict[key] = self.wrap_quotes(value)
        else:
            self.quotes_dict = quotes_load

    def get_quote(self, id: str):
        return self.quotes_dict.get()

    def get_random_quote(self):
        if self.quotes_dict != None:
            return self.wrap_quotes(random.choice(self.quotes_dict.values()))
        else:
            return EMPTY_QUOTES_MESSAGE

    def remove_quote(self, id: str):
        pass

    def load_quotes(self, quotes_add: dict):
        pass

    def from_json(self, json: str):
        pass

    def to_json(self):
        pass

    def load_from_json_file(self, file_path: str):
        pass

    def save_to_json_file(self, file_path: str):
        pass

    def wrap_quotes(self, input):
        return "%s%s%s" % (QUOTES_MARKDOWN,input,QUOTES_MARKDOWN)

    def empty(self):
        self.quotes_dict = { }
