import json

class Loadstore:

    def __init__(self) -> None:
        pass

    def load_list(self):
        pass

    def load_file_json(self):
        with open("slutuppgift\items.json") as f:
            items = json.load(f)
            print(items)
            for item in items['items']:
                # Use this in executes second argument
                executeValues = tuple(item.values())
                print(executeValues)


    def load_file_json_2(self):
        with open("slutuppgift\items.json") as f:
            data_to_database_executemany = []
            items = json.load(f)
            for item in items['items']:
                data_to_database_executemany.append(tuple(item.values()))

        print(data_to_database_executemany)