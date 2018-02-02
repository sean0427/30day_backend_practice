from shop import db

class Number(db.Model):
    __tablename__ = 'number'

    id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    password = db.Column(db.Text, nullable=False)
    e_mail = db.Column(db.Text, nullable=False, unique=True)
    user_classification_id = db.Column(db.Integer, nullable=False)

    def __repr__(self):
       """Define a base way to print models"""
       return '%s(%s)' % (self.__class__.__name__, {
           column: value
           for column, value in dict(self).items()
           })

    def __iter__(self):
        yield 'id', self.id
        yield 'e_mail', self.e_mail
