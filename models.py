from app import db

ROLE_USER = 0
ROLE_ADMIN = 1

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nickname = db.Column(db.String(32), index = True, unique = True)
    email = db.Column(db.String(128), index = True, unique = True)
    role = db.Column(db.SmallInteger, default = ROLE_USER)
    '''messages = """list of messages"""'''

    def __repr__(self):
        return '<User %r>' % (self.nickname)

class Messages(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.String(256))
    timestamp = db.Column(db.DateTime)
    authorid = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Posts %r>' % (self.subject)

class Events(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(128), index = True)
    description = db.Column(db.String(512))
    '''authors = """list of authors"""'''

    def __repr(self):
        return '<Events %r>' % (self.name)
