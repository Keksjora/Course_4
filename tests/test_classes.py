import pytest

from src.classes import Category, Product


@pytest.fixture
def category_pasta():
    category = Category(
        "Паста",
        "Разные макаронные изделия",
        [Product("спагетти", "Макароны", 50.0, 20), Product("перья", "Макароны", 60.0, 15)],
    )
    return category


@pytest.fixture
def category_gaming_consoles():
    category = Category(
        "Консоли",
        "Игровые приставки",
        [
            Product("Playstation", "Игровая консоль", 40000.0, 10),
            Product("Nintendo Switch", "Игровая консоль", 30000.0, 8),
        ],
    )
    return category
  
@pytest.fixture()
def category_pasta():
    return Category("Паста", "Разные макаронные изделия", ["спагетти", "перья"])


@pytest.fixture()
def category_gaming_consoles():
    return Category("Консоли", "Игровые приставки", ["Playstation", "Nintendo Switch"])



def test_category_init(category_pasta, category_gaming_consoles):
    assert category_pasta.category_name == "Паста"
    assert category_pasta.description == "Разные макаронные изделия"
    assert Category.category_count == 2  # Проверяем общее количество категорий

    assert category_gaming_consoles.category_name == "Консоли"
    assert category_gaming_consoles.description == "Игровые приставки"
    assert Category.category_count == 2  # Проверяем общее количество категорий


def test_product_init():
    product = Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    assert product.product_name == "Samsung Galaxy C23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5

    product = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    assert product.product_name == '55" QLED 4K'
    assert product.description == "Фоновая подсветка"
    assert product.price == 123000.0
    assert product.quantity == 7


def test_product_addition():
    product1 = Product("Phone1", "Smartphone", 1000.0, 10)
    product2 = Product("Phone2", "Smartphone", 2000.0, 5)
    result = product1 + product2
    assert result == 20000.0  # Проверяем правильность сложения продуктов


def test_list_of_products(category_pasta):
    expected_output = "спагетти, 50.0 руб. Остаток: 20 шт.\nперья, 60.0 руб. Остаток: 15 шт."
    assert category_pasta.list_of_products == expected_output


def test_add_non_product_to_category(category_pasta):
    with pytest.raises(TypeError):
        category_pasta.add_product("not a product")
    assert category_pasta.products == ["спагетти", "перья"]
    assert category_pasta.unique_products == 4
    assert category_pasta.category_count == 2

    assert category_gaming_consoles.category_name == "Консоли"
    assert category_gaming_consoles.description == "Игровые приставки"
    assert category_gaming_consoles.products == ["Playstation", "Nintendo Switch"]
    assert category_gaming_consoles.unique_products == 4
    assert category_gaming_consoles.category_count == 2


@pytest.fixture()
def product_smartphone():
    return Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture()
def product_tv():
    return Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)


def test_product_init(product_smartphone, product_tv):
    assert product_smartphone.product_name == "Samsung Galaxy C23 Ultra"
    assert product_smartphone.description == "256GB, Серый цвет, 200MP камера"
    assert product_smartphone.price == 180000.0
    assert product_smartphone.quantity == 5
    assert product_tv.product_name == '55" QLED 4K'
    assert product_tv.description == "Фоновая подсветка"
    assert product_tv.price == 123000.0
    assert product_tv.quantity == 7
