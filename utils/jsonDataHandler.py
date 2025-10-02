import json

class JsonDataHandler:
    def __init__(self, file_path):
        self.file_path = file_path

    def store_data(self, data):
        with open(self.file_path, 'w') as json_file:
            json.dump(data, json_file, indent=2)

    def load_data(self):
        try:
            with open(self.file_path, 'r') as json_file:
                data = json.load(json_file)
            return data
        except FileNotFoundError:
            # Return an empty dictionary if the file doesn't exist
            return {}
