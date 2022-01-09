from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    content = db.Column(db.Text, nullable=False)
    status = db.Column(db.Boolean, unique=False, default=True)
    publication_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    last_update = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f"<Ogłoszenie {self.id}>"

    def json(self):
        return {
                    'id': self.id, 
                    'title': self.title,
                    'content': self.content,
                    'status': self.status,
                    'publication_date': self.publication_date,
                    'last_update': self.last_update
                }

def get_all_messages():
    '''Funkcja zwraca wszystkie ogłoszenia z bazy danych
    '''
    data = Message.query.all()
    print(data)
    return data


def get_active_messages():
    '''Funkcja zwraca aktywne ogłoszenia z bazy danych
    '''
    return Message.query.filter_by(status=True).all()


def post_message(data: dict):
    '''Funkcja zapisuje do bazy danych ogłoszenia
    '''
    pass

def add_message():
    pass

def get_message_details(id: int):
    """Funkcja zwraca z bazy danych rekord ogłoszenia o podanym id
    """
    return [Message.query.get(id)]


def delete_message(id: int):
    """Funkcja usuwa z bazy danych rekord ogłoszenia o podanym id
    """
    pass

def put_message(id: int):
    """Funkcja aktualizuje w bazie danych rekord ogłoszenia o podanym id
    """
    message = Message.query.get(id)
    if not message:
        return 

    db.session.delete(message)
    db.session.commit()

    return f"Ogłoszenie {id} zostało poprawnie usuniete"

def patch_message(id: int, field: str):
    """Funkcja aktualizuje w bazie danych pole rekordu ogłoszenia o podanym id
    :param [int] id: id rekordu do zaktualizowania
    :param [str] field: pole rekordu do zaktualizowania
    """
    pass