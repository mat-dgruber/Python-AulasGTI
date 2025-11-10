import collections.abc

class ListaHistorico:
    """
    Uma classe que age como uma lista, mas mantém um 
    histórico de todos os itens que já foram adicionados.
    """
    
    def __init__(self):
        # self.itens armazena a lista *atual*
        self._itens = []
        # self.historico armazena *todos* os itens que já passaram pela lista
        self._historico = set()

    def adicionar(self, item):
        """
        Adiciona um item à lista e ao histórico.
        (Requisito: O usuário deve ser capaz de adicionar algo na lista)
        """
        self._itens.append(item)
        self._historico.add(item)
        print(f"Item '{item}' adicionado.")

    def deletar(self, item):
        """
        Deleta um item da lista atual, mas o mantém no histórico.
        (Requisito: O usuário deve ser capaz de deletar um item da lista)
        """
        try:
            self._itens.remove(item)
            print(f"Item '{item}' deletado da lista atual.")
        except ValueError:
            print(f"Erro: Item '{item}' não encontrado na lista *atual*.")

    def verificar_historico(self, item):
        """
        Verifica se um item já esteve presente na lista em algum momento.
        (Requisito: ...ser capaz de checar se um item já esteve presente)
        """
        return item in self._historico

    def __len__(self):
        """
        Retorna o tamanho da lista *atual*.
        (Requisito: O usuário deve ser capaz de verificar o tamanho da lista)
        """
        return len(self._itens)

    def __str__(self):
        """Retorna uma representação em string da lista *atual*."""
        return f"Lista atual: {self._itens}"
        
    def __repr__(self):
        """Retorna uma representação mais detalhada do objeto."""
        return f"ListaHistorico(itens={self._itens}, historico={self._historico})"

# --- Exemplo de Uso ---
print("Criando a lista com histórico...")
minha_lista = ListaHistorico()
print("---")

# 1. Adicionando itens
minha_lista.adicionar("banana")
minha_lista.adicionar("maçã")
minha_lista.adicionar("uva")
print(minha_lista)
print("---")

# 2. Verificando o tamanho
print(f"Tamanho atual da lista: {len(minha_lista)}")
print("---")

# 3. Deletando um item
minha_lista.deletar("maçã")
print(minha_lista)
print(f"Tamanho da lista após deletar: {len(minha_lista)}")
print("---")

# 4. Verificando o histórico
print(f"A 'maçã' está na lista atual? {'maçã' in minha_lista._itens}")
print(f"A 'maçã' já esteve na lista? {minha_lista.verificar_historico('maçã')}")
print(f"A 'uva' já esteve na lista? {minha_lista.verificar_historico('uva')}")
print(f"O 'abacaxi' já esteve na lista? {minha_lista.verificar_historico('abacaxi')}")
print("---")

# 5. Tentando deletar item que não existe
minha_lista.deletar("pera")