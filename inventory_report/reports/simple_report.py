from datetime import date


class SimpleReport:
    @staticmethod
    def generate(inventory):
        nome_da_empresa = [i["nome_da_empresa"] for i in inventory]
        data_de_fabricacao = min([i["data_de_fabricacao"] for i in inventory])
        data_de_validade = min([i["data_de_validade"] for i in inventory
                                if i['data_de_validade'] >= str(date.today())])
        empresa_com_mais_produtos = max(set(nome_da_empresa),
                                        key=nome_da_empresa.count)

        return (
            f"Data de fabricação mais antiga: {data_de_fabricacao}\n"
            f"Data de validade mais próxima: {data_de_validade}\n"
            f"Empresa com mais produtos: {empresa_com_mais_produtos}"
        )
