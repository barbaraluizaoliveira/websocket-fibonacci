from sqlalchemy.orm import Session
from app.models.connected_user import ConnectedUser

def save_user_connected(db: Session, username: str, connected_at):
    new_user = ConnectedUser(username=username, connected_at=connected_at)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def remove_user_connected(db: Session, username: str):
    db.query(ConnectedUser).filter(ConnectedUser.username == username).delete()
    db.commit()
