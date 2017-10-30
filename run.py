from peewee import IntegrityError

from kettocritic import models, router, serializers, views

from db_utils import create_tables, create_data, drop_tables


if __name__ == '__main__':
    try:
        create_tables()
        create_data()
    except IntegrityError:
        pass