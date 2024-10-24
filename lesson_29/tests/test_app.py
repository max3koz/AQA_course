import pytest

from app import create_table, insert_record, update_record, delete_record, select_records
from assertpy import assert_that


@pytest.fixture(scope="module")
def setup_db():
    create_table()

def test_insert_record(setup_db):
    insert_record("TestName")
    records = select_records()
    assert_that(len(records)).is_equal_to(1)
    assert_that(records[0][1]).is_equal_to("TestName")

def test_update_record(setup_db):
    insert_record("OldName")
    update_record(1, "NewName")
    records = select_records()
    assert_that(records[0][1]).is_equal_to("OldName")

def test_delete_record(setup_db):
    insert_record("ToBeDeleted")
    delete_record(1)
    records = select_records()
    assert_that(len(records)).is_equal_to(0)
