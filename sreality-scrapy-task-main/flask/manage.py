from project.crawler import crawl_flats
from project.extensions import db

def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


def load_flats():
    crawl_flats()


if __name__ == "__main__":
    create_db()
    load_flats()
