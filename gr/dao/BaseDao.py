from app import db


class BaseDao:
    def __init__(self, model):
        self.model = model

    def get_by_id(self, id):
        return self.model.query.get(id)

    def get_all(self):
        return self.model.query.all()

    def purge(self, model):
        db.session.delete(model)
        db.session.commit()

    def purge_all(self):
        return self.model.query.delete()

    def upsert(self, object):
        db.session.add(object)
        db.session.commit()
        return object

    def upsert_all(self, objects):
        for object in objects:
            db.session.add(object)
        db.session.commit()
        return objects
