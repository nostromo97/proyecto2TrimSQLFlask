from typing import Callable 

from flask_sqlalchemy import SQLAlchemy


def init_db(app) -> dict[str, Callable]:
    db = SQLAlchemy(app)

    
    class Contact(db.Model):
        
        __tablename__ = "contacts" 
        uid = db.Column("id", db.Integer, primary_key=True)
        nick = db.Column(db.String(16))
        first_name = db.Column(db.String(128))
        last_name = db.Column(db.String(128))
        phone = db.Column(db.Integer())

        
        def __str__(self): 
            return f"[{self.uid}] {self.first_name} {self.last_name}"

        
        @property
        def fullname(self) -> str:
            return f"{self.first_name} {self.last_name}"

  
    def create_contact(nick: str, first_name: str, last_name: str, phone: int):
        contact = Contact(
            nick=nick, first_name=first_name, last_name=last_name, phone=phone
        )
        db.session.add(contact)
        db.session.commit()

    def read_contact(uid: int) -> Contact:
        return Contact.query.get(uid)

    def update_contact(
        uid: int, nick: str, first_name: str, last_name: str, phone: int
    ):
        contact = Contact.query.get(uid)
        contact.nick = nick
        contact.first_name = first_name
        contact.last_name = last_name
        contact.phone = phone
        db.session.commit()

    def delete_contact(uid: int):
        contact = Contact.query.get(uid)
        db.session.delete(contact)
        db.session.commit()

    def list_contacts() -> list[Contact]:
        contacts = Contact.query.all()
        return [contact for contact in contacts]

    db.create_all()

    return {
    	
        "create": create_contact,
        "read": read_contact,
        "update": update_contact,
        "delete": delete_contact,
        "list": list_contacts,
    }


