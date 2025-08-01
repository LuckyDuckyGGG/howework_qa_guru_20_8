import csv

# -------------------------------------------------------------------
# Прямолинейный вариант теста
# -------------------------------------------------------------------


def test_workers_are_adults():
    """
    Тестируем, что все работники старше 18 лет
    """
    with open("users.csv") as f:
        users = csv.DictReader(f, delimiter=";")
        workers = [user for user in users if user["status"] == "worker"]
        print(workers)

    for worker in workers:
        assert int(worker["age"]) >= 18, f"Рабочий {worker['name']} младше 18 лет"

        # workers = []
        # for user in users:
        #     if user["status"] == "worker":
        #         workers.append(user)