"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from homework.models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 10)

@pytest.fixture
def cart(product):
    return Cart()


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(5) is True
        assert product.check_quantity(10) is True
        assert product.check_quantity(0) is True
        assert product.check_quantity(5.2) is True

        assert product.check_quantity(11) is False

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        product_on_storage = product.quantity
        product.buy(3)
        assert product.quantity == 7

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError):
            product.buy(11)


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_cart_add_product(self, product, cart):
        cart.add_product(product, 5)
        assert cart.products[product] == 5
        cart.add_product(product, 1)
        assert cart.products[product] == 6
        cart.add_product(product, 0)
        assert cart.products[product] == 6

    def test_cart_remove_some_product(self, product, cart):
        cart.add_product(product, 5)
        cart.remove_product(product, 3)
        assert cart.products[product] == 2

    def test_cart_remove_all_product(self, product, cart):
        cart.add_product(product, 5)
        cart.remove_product(product, 5)
        assert product not in cart.products
        cart.add_product(product, 5)
        cart.remove_product(product, 10)
        assert product not in cart.products
        cart.add_product(product, 5)
        cart.remove_product(product)
        assert product not in cart.products

    def test_cart_clear(self, product, cart):
        cart.add_product(product, 5)
        cart.clear()
        assert product not in cart.products

    def test_cart_get_total_price(self, product, cart):
        cart.add_product(product, product.quantity)
        assert cart.get_total_price() == product.price * product.quantity

    def test_cart_buy(self, product, cart):
        cart.add_product(product, 5)
        cart.buy()
        assert product.quantity == 5
        assert cart.products == {}

    def test_cart_buy_more_available(self, product, cart):
        cart.add_product(product, 15)
        with pytest.raises(ValueError):
            cart.buy()
