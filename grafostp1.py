# Hugo Galli - 31/05/2021 - Disciplina GRAFOS - UFSJ #

# CLASSE GRAFO, CASO QUEIRA ATUALIZAR E COLOCAR TANTO LISTAS QUANTO MATRIZES #
class Grafo:
    def __init__(self, qa):
        self.qa = qa


# CLASSE LISTA, HERDEIRA DE GRAFO E COM SEUS PROPRIOS METODOS #
class Lista(Grafo):
    def __init__(self, qa):
        super().__init__(qa)

        # INICIALIZANDO UMA LISTA PARA ARMAZENAR OS DADOS RECEBIDOS POSTERIORMENTE DO ARQUIVO #
        self.lista = list()

    # CRIACAO DE UMA ARESTA A PARTIR DOS DADOS #
    def criaAresta(self, aresta, origem, destino, peso):
        self.lista.append([aresta, origem.upper(), destino.upper(), peso])

    # FUNCAO QUE TRADUZ AS INFORMACOES DOS VERTICES PARA UM SIMPLES VETOR COM A LISTA DE TODOS OS VERTICES EXISTENTES #
    def verticesCount(self):
        check = list()
        for i in range(qa):
            if self.lista[i][1] not in check:
                check.append(self.lista[i][1])
            if self.lista[i][2] not in check:
                check.append(self.lista[i][2])
        return check

    # FUNCAO QUE RECEBE A LISTA DE VERTICES E UM VERTICE, E RETORNA SEUS ANTECESSORES E SUCESSORES #
    def verticeDiscover(self, vertices, vertice):
        vertice = vertice.upper()
        antecessores, sucessores, p = list(), list(), list()
        antecessores.clear()
        sucessores.clear()
        if vertice not in vertices:
            print("O Vertice informado nao faz parte do Grafo recebido.")
        else:
            for i in range(qa):
                if self.lista[i][1] == vertice:
                    sucessores.append(self.lista[i][2])
                    p.append(self.lista[i][3])
                if self.lista[i][2] == vertice:
                    antecessores.append(self.lista[i][1])
        return sucessores, antecessores, p

    # FUNCAO PARA IMPRIMIR O GRAFO DO ARQUIVO EM FORMA DE LISTA FORMATADA (VERTICE -> DESTINO (PESO) #
    def imprimeGrafo(self, vertices):
        print("Grafo em forma de lista:")
        for i in range(len(vertices)):
            print()
            s, a, p = self.verticeDiscover(vertices, vertices[i])
            for j in range(len(s)):
                print(f"{vertices[i].upper()} -> {s[j].upper()} ({p[j]})", end="; ")

    # METODO PARA PRINTAR O SUMARIO #
    def sumario(self, vertices):
        v, a = len(vertices), len(self.lista)
        print(f"Numero de arestas do grafo: {a}")
        print(f"Numero de vertices do grafo: {v}")
        densidade = a / (v * (v - 1))
        print(f"Densidade do grafo: {densidade}")

    # FIM DA CLASSE LISTA #


# FUNCAO DESIGNADA PARA LEITURA DO ARQUIVO #
# ARQUIVO DEVE ESTAR NO MESMO DIRETORIO COM O NOME "grafo" PARA QUE FUNCIONE CORRETAMENTE
# EXEMPLO DE UM ARQUIVO FUNCIONAL PARA ESTE CODIGO: 1 A B 2
#                                                   2 B C 3
def lerGrafo(arq):
    arquivo = open(arq, 'r')
    text = arquivo.readlines()
    grafo = [i.split('\n', 1)[0] for i in text]
    return grafo


# MENU BASE DO PROGRAMA #
def menu():
    x = int(input("1 - Sumario\n"
                  "2 - Grau de Vertice\n"
                  "3 - Sucessores de algum Vertice\n"
                  "4 - Antecessores de algum Vertice\n"
                  "5 - Exibir grafo em forma de lista\n"
                  "6 - Terminar o aplicativo\n"))
    return x


# FUNCAO MAIN DO CODIGO, MANIPULANDO AS DEMAIS #
if __name__ == '__main__':

    # CRIACAO DO GRAFO #
    info = lerGrafo('grafo')
    qa = len(info)
    grafo = Lista(qa)
    for i in range(qa):
        grafo.criaAresta(int(info[i][0]), info[i][2], info[i][4], info[i][6])
    vertices = grafo.verticesCount()
    ########################

    # COMUNICACAO COM O USURARIO #
    escolha = 0
    while escolha != 6:
        escolha = menu()
        if escolha == 1:
            grafo.sumario(vertices)
        if escolha == 2:
            v = input("Insira o vertice: ")
            suc, ant, p = grafo.verticeDiscover(vertices, v)
            print(
                f"Grau do vertice {v.upper()}: {len(suc) + len(ant)}, sendo {len(suc)} sucessores {suc} e {len(ant)} antecessores {ant}")
        if escolha == 3:
            v = input("Insira o vertice: ")
            suc, ant, p = grafo.verticeDiscover(vertices, v)
            print(f"Sucessores de {v.upper()}: {suc}")
        if escolha == 4:
            v = input("Insira o vertice: ")
            suc, ant, p = grafo.verticeDiscover(vertices, v)
            print(f"Antecessores de {v.upper()}: {ant}")
        if escolha == 5:
            grafo.imprimeGrafo(vertices)
        if escolha == 6:
            break
    # FIM DA MAIN #
# FIM DO CODIGO #