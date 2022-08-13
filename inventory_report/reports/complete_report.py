from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(inventory):
        produto_por_empresa = dict()

        for produto in inventory:

            if produto["nome_da_empresa"] in produto_por_empresa:
                produto_por_empresa[produto["nome_da_empresa"]] += 1
            else:
                produto_por_empresa[produto["nome_da_empresa"]] = 1

        lista_produtos = [
            f"- {key}: {value}\n"
            for (key, value) in produto_por_empresa.items()
        ]
        formatado = "".join(index for index in lista_produtos)

        return (
            f"{SimpleReport.generate(inventory)}\n"
            "Produtos estocados por empresa:\n"
            f'{formatado}'
        )
