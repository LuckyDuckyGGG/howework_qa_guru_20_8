import pytest
import csv


@pytest.fixture
def users():
    with open("users.csv") as f:
        users = list(csv.DictReader(f, delimiter=";"))
        return users

@pytest.fixture
def workers(users):
    workers = [user for user in users if user["status"] == "worker"]
    return workers

def test_workers_are_adult_v2(workers):
    for worker in workers:
        assert user_is_adult(worker), f"Рабочий {worker['name']} младше 18 лет"

def user_is_adult(user):
    return int(user["age"]) >= 18
