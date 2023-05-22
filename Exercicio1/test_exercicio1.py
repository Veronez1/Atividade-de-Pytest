import pytest
import sqlite3


@pytest.fixture(scope="module")
def database():
    conn = sqlite3.connect(':memory:')
    yield conn
    conn.close()


def test_connection(database):
    cursor = database.cursor()
    cursor.execute("SELECT SQLITE_VERSION()")
    data = cursor.fetchone()
    assert data is not None, "Failed to establish database connection"
