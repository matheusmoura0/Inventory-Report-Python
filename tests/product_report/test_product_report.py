from inventory_report.inventory.product import Product


def test_relatorio_produto():
    produto = Product(
        1,
        "Rapier",
        "Dungeon",
        "01/01/2020",
        "01/01/2021",
        "4521540540",
        "No bolso do ladino",
    )
    assert produto.__repr__() == (
        "O produto Rapier"
        "fabricado em 01/01/2020 "
        "por Dungeon com validade"
        "até 01/01/2021"
        "precisa ser armazenado No bolso do ladino."
    )
