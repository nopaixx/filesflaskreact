from api.app import db


class Images(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    path = db.Column(db.String(1024))

    def serialize(self):
        ret = dict()

        ret['name'] = self.name
        ret['path'] = self.path

        return ret

    @classmethod
    def update(cls, model, path, name):

        model.name = name
        model.path = path

        db.session.commit()

        return model
        
    @classmethod
    def create(cls, path, name):
        model = cls()

        model.name = name
        model.path = path

        db.session.add(model)
        db.session.commit()

        return model
