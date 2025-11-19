import pytest
import allure
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import ItemList


DATABASE_URL = "postgresql://postgres:admin@postgres:5432/postgres"


@pytest.fixture(scope="session")
def engine():
    engine = create_engine(DATABASE_URL)
    return engine


@pytest.fixture(scope="function")
def session(engine):
    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(ItemList).delete()
    session.commit()

    yield session

    session.close()

@allure.feature("Database")
def test_db_connection(engine):
    """Check the database connection"""
    conn = engine.connect()

    with allure.step("verify connect to database"):
        assert conn is not None
    conn.close()

@allure.feature("Item database management")
def test_add_record(session):
    """Check create a new record in DB"""
    with allure.step("create data for test"):
        item = ItemList(
            item_name="TestAdd",
            item_descript="Test description",
            item_price=123
        )
    with allure.step("Execute query"):
        session.add(item)
        session.commit()

    with allure.step("Get data about last execute and verify the result"):
        saved = session.query(ItemList).filter_by(item_name="TestAdd").first()
        assert saved is not None
        assert saved.item_price == 123

@allure.feature("Item database management")
def test_get_all(session):
    """Check the receiving records from DB"""
    with allure.step("create data for test"):
        session.add_all([
            ItemList(item_name="A", item_descript="dA", item_price=10),
            ItemList(item_name="B", item_descript="dB", item_price=20),
        ])
        session.commit()

    with allure.step("Get data about last execute and verify the result"):
        items = session.query(ItemList).order_by(ItemList.id.asc()).all()

        assert len(items) == 2
        assert items[0].item_name == "A"
        assert items[1].item_name == "B"

@allure.feature("Item database management")
def test_update_record(session):
    """Check update data in record in DB"""
    with allure.step("create data for test"):
        item = ItemList(item_name="OldName", item_descript="Old", item_price=1)
        session.add(item)
        session.commit()

    with allure.step("execute update query"):
        item.item_name = "NewName"
        item.item_price = 999
        session.commit()

    with allure.step("Get data about last execute and verify the result"):
        updated = session.query(ItemList).filter_by(id=item.id).first()
        assert updated.item_name == "NewName"
        assert updated.item_price == 999

@allure.feature("Item database management")
def test_delete_record(session):
    """Check delete record from DB"""
    with allure.step("create data for test"):
        item = ItemList(item_name="ToDelete", item_descript="Del it", item_price=0)
        session.add(item)
        session.commit()

    with allure.step("execute delete query"):
        session.delete(item)
        session.commit()

    with allure.step("Get data about last execute and verify the result"):
        deleted = session.query(ItemList).filter_by(id=item.id).first()
        assert deleted is None