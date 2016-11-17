from bson.dbref import DBRef
from mongokat import Document


class Document(Document):
    def __init__(self, **kwargs):
        super(Document, self).__init__(**kwargs)
        self.database = self.mongokat_collection.database
        self.client = self.mongokat_collection.client

    def as_dict(self, fields=None):
        if not fields:
            fields = self.structure.keys()

        fields = list(set(fields))
        document = dict(zip(fields, [self[f] for f in set(fields)]))

        def dereference_level(level):
            if isinstance(level, DBRef):
                return self.database.dereference(level)
            elif type(level) is dict:
                return dict(zip(level.keys(),
                                map(dereference_level, level.values())))
            elif type(level) is list:
                return map(dereference_level, level)
            else:
                return level

        return dereference_level(document)

    def get_sub(self, name, _id):
        try:
            return filter(lambda s: s['_id'] == _id, self[name])[0]
        except IndexError:
            return None

    def increment_sub(self, name):
        counter_name = name + 'id'
        return int(self.database.system_js.getNextSequence(counter_name))

    def add_sub(self, name, fields):
        fields['_id'] = self.increment_sub(name)
        self[name].append(fields)
        return fields['_id']

    def update_sub(self, name, _id, fields):
        fields['_id'] = _id
        self[name] = [e if e['_id'] is not fields['_id'] else fields
                      for e in self[name]]
        return True

    def remove_sub(self, name, _id):
        sub = self.get_sub(name, _id)
        if not sub:
            return False

        self[name] = filter(lambda s: s['_id'] != _id, self[name])
        return True
