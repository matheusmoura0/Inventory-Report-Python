class Product:
    def __init__(
        self,
        id,
        nome_do_produto,
        nome_da_empresa,
        data_de_fabricacao,
        data_de_validade,
        numero_de_serie,
        instrucoes_de_armazenamento,
    ):
        self.id = id
        self.nome_do_produto = nome_do_produto
        self.nome_da_empresa = nome_da_empresa
        self.data_de_fabricacao = str(data_de_fabricacao)
        self.data_de_validade = str(data_de_validade)
        self.numero_de_serie = numero_de_serie
        self.instrucoes_de_armazenamento = instrucoes_de_armazenamento

    def __repr__(self):
        return (
            f"O produto {self.nome_do_produto}"
            f" fabricado em {self.data_de_fabricacao}"
            f" por {self.nome_da_empresa} com validade"
            f" até {self.data_de_validade}"
            f" precisa ser armazenado {self.instrucoes_de_armazenamento}."
        )


def test_cria_produto():
    produto = Product(
        id=1,
        nome_do_produto="Rapier",
        nome_da_empresa="Dungeon",
        data_de_fabricacao="01/01/2020",
        data_de_validade="01/01/2021",
        numero_de_serie="4521540540",
        instrucoes_de_armazenamento="No bolso do rogue",
    )
    assert produto.id == 1
    assert produto.nome_do_produto == "Rapier"
    assert produto.nome_da_empresa == "Dungeon"
    assert produto.data_de_fabricacao == "01/01/2020"
    assert produto.data_de_validade == "01/01/2021"
    assert produto.numero_de_serie == "4521540540"
    assert produto.instrucoes_de_armazenamento == "No bolso do rogue"
