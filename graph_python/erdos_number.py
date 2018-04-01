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

        # caso não exista Erdos.. todos os numeros sao infinitos
        if not gp[key].get_vertex('P. Erdos'):
            for author in gp[key].get_all_vertex():
                print(author, ": infinito", sep='')
        else:
            authors = gp[key].get_all_vertex()
            sorted(authors, key=cmp_to_key(compare))  # Ordenar authores

            distanciaAteErdos = gp[key].breadth_search(
                gp[key].get_vertex('P. Erdos'))

            # print(distanciaAteErdos)
            # gp[key].print_adjacent_list()

            for author in authors:
                if distanciaAteErdos[author] == float("inf"):
                    print(author, ": infinito", sep='')
                else:
                    print(author, ": ", distanciaAteErdos[author], sep='')


def compare(item1, item2):
    # P. Erdos
    # 0123
    if item1.get_name()[3:] < item2.get_name()[3:]:
        return -1
    elif item1.get_name()[3:] > item2.get_name()[3:]:
        return 1
    else:
        if item1.get_name()[0] < item2.get_name()[0]:
            return -1
        elif item1.get_name()[0] > item2.get_name()[0]:
            return 1
        else:
            return 0


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

        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0

        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0

        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0
    return K


if __name__ == '__main__':
    main()
