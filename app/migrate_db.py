from sqlalchemy import create_engine

from models.task import TaskModel

engine = create_engine("mysql+pymysql://root@db:3306/demo?charset=utf8", echo=True)


def migrate_database():
    TaskModel.metadata.drop_all(bind=engine)
    TaskModel.metadata.create_all(bind=engine)


if __name__ == "__main__":
    migrate_database()