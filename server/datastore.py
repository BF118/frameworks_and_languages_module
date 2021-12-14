

ITEMS ={"user_id": "user1234","keywords": ["hammer", "nails","tools"],
"description": "A hammer and nails set",
"lat": 51.2798438,
"lon": 1.0830275,
"date_from": "2019-08-24T14:15:22Z",
"date_to": "2019-08-24T14:15:22Z"}

class DataModelPythonDict:
    def __init__(self, items):
        self.items = items or {}
        self.items_id_max = max(self.items.keys() or (0,0))
    def get_item(self, id):
        return self.items.get(id)
    def delete_item(self, id):
        del self.items[id]
    def create_item(self, data):
        self.items_id_max +=1
        _id = self.items_id_max
        self.items[_id] = data
        data['id'] = _id
        return data

datastore = DataModelPythonDict(ITEMS)




