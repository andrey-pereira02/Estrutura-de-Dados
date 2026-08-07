class Estoque:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def valorEstoque(self):
        print(
            f'O valor somado do estoque de {self.nome} é {self.quantidade * self.preco}')


estoque = Estoque("açai", 10, 50)
estoque.valorEstoque()
