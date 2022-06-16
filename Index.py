

def getReferencies(consulta, arquivo):
    aparicoes = False
    result = {}
    pla = ''
    string = ''
    strings = ''
    inserida = ''

    for element in arquivo:
        #inserida = ''
        pla = ''
        for palavra in element:
            for essa in consulta:
                if(palavra == str(essa)):

                    pla = palavra                                 
                    aparicoes = aparicoes + 1

                    if(pla == str(inserida)):

                        num = len(element)
                        strings = strings + ' ' + str(aparicoes) + ',' + str(element[num-1])
                        result[essa] = strings
                        #strings = ''

                    else:

                        num = len(element)
                        string = string + ' ' + str(aparicoes) + ',' + str(element[num-1])
                        resultado = essa + ": " + string
                        result[essa] = string
                        #string = ''

                    inserida = pla 

        aparicoes = False     

    return result


def main(conjunto:str, desconsideradas:str, consulta:str):

    with open(conjunto,"r") as arquivo:
        base = arquivo.readlines()

    links = []
    arq = []
    result = []
    count = ''

    for x in base:
        links.append(x)
        
    def chr_remove(old, to_remove):
        new_string = old
        for x in to_remove:
            new_string = new_string.replace(x, ' ')
        return new_string

    def add(links):

        for linksArquivo in links:      
            with open(linksArquivo.strip(), "r") as arquivo:
                isso = arquivo.readlines()
                for x in isso:
                    arq.append(x[:len(x)])
                 
        return arq
            
    arq = add(links)
    soma = 0
    for x in arq:
        semponto = chr_remove(x,".,?!")
        count = semponto.split()
        count.append(soma)
        soma = soma + 1
        result.append(count)

    arq = getReferencies(consulta, result)
    print(arq)
    
consulta = ['casa', 'engracada']
desconsideradas = ['o','a','e','de','da','das','do','na','nas','no','em','nao','um','uns','uma','umas']

main("base.txt", desconsideradas, consulta)