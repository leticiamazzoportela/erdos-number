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
                print(author, ": infinito")
        else:
            pass  # fazer a busca em largura


if __name__ == '__main__':
    main()
