from app import db


class BaseDao:
    def __init__(self, model):
        self.model = model

    def get_by_id(self, id):
        return self.model.query.get(id)

    def get_all(self):
        return self.model.query.all()

    def purge_all(self):
        return self.model.query.delete()

    def add(self, object):
        db.session.add(object)
        db.session.flush()
        return object

    def add_all(self, objects):
        for object in objects:
            self.add(object)
        return objects
