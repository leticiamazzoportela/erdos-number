'''
    Erdos Number Class
'''

import graph


def main():
    qtdInput = int(input())  # le o input do usuario

    no_teste = 1
    gp = {}  # cria uma estrutura para armazenar todos os testes

    while(qtdInput != 0):  # le novos inputs até digitar um 0
        gp[no_teste] = graph.Graph()  # grafo para o novo teste
        for i in range(qtdInput):  # le todos os autores de todos os artigos
            authors = input()

            # quebra a string na ','... separando assim todos os autores
            authors_array = authors.split(',')
            for i in range(len(authors_array)):
                # caso exista um espaco em branco no comeco de cada nome
                # remover este espaco
                if authors_array[i][0] == ' ':
                    authors_array[i] = authors_array[i][1:]

                # adicionar o autor ao grafo
                if authors_array[i]:
                    gp[no_teste].add_vertex(authors_array[i])

            # adicionar todas as ligacoes entre os autores
            for author in authors_array:  # passa por todos os autores

                # para cada autor.. comparar com todos os outros
                for other_author in authors_array:

                    # evitar comparar um autor com ele mesmo
                    if(author != other_author):

                        # verifica se os dois autores sao vertex do grafo
                        if gp[no_teste].get_vertex(
                            other_author) and gp[no_teste].get_vertex(
                                author):

                            # adicionar uma aresta entre estes vertex
                            gp[no_teste].add_edge(gp[no_teste].get_vertex(
                                other_author), gp[no_teste].get_vertex(author))

        qtdInput = int(input())  # le o novo input
        no_teste += 1

    for key in gp:
        print("")
        print("Teste", key)

        authors = gp[key].get_all_vertex()
        authors = sorted(authors, key=cmp_to_key(compare))

        distanciaAteErdos = gp[key].breadth_search(
            gp[key].get_vertex('P. Erdos'))

        for author in authors:
            if distanciaAteErdos[author] == float("inf"):
                print(author, ": infinito", sep='')
            else:
                print(author, ": ", distanciaAteErdos[author], sep='')


def compare(item1, item2):
    # P. Erdos
    # 0123
    name1 = item1.get_name()
    name2 = item2.get_name()

    lastname1 = name1[3:]
    lastname2 = name2[3:]

    if lastname1 == lastname2:
        if name1[0] < name2[0]:
            return -1
        else:
            return 1

    if max(lastname1, lastname2) == lastname1:
        return 1
    else:
        return -1


def cmp_to_key(mycmp):
    'Convert a cmp= function into a key= function'
    class K(object):
        def __init__(self, obj, *args):
            self.obj = obj

        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0

        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0

        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0

        # def __le__(self, other):
        #     return mycmp(self.obj, other.obj) <= 0

        # def __ge__(self, other):
        #     return mycmp(self.obj, other.obj) >= 0

        # def __ne__(self, other):
        #     return mycmp(self.obj, other.obj) != 0
    return K


if __name__ == '__main__':
    main()
