class SimpleReport:
    def __init__(self, product):
        self.product = product


def generate_report(product):
    report = SimpleReport(product)
    return report
