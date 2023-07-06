from .models import Conta, Categoria


def total_contas(classes: Conta | Categoria, atributo: str) -> float:
    total = 0
    for classe in classes:
        total += getattr(classe, atributo)
    return total
