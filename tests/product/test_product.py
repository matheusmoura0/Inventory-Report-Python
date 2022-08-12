from inventory_report.inventory.product import Product


def test_cria_produto():
    produto = Product(
        1,
        "Rapier",
        "Dungeon",
        "01/01/2020",
        "01/01/2021",
        "4521540540",
        "No bolso do ladino",
    )
    assert produto.id == 1
    assert produto.nome_do_produto == "Rapier"
    assert produto.nome_da_empresa == "Dungeon"
    assert produto.data_de_fabricacao == "01/01/2020"
    assert produto.data_de_validade == "01/01/2021"
    assert produto.numero_de_serie == "4521540540"
    assert produto.instrucoes_de_armazenamento == "No bolso do ladino"
