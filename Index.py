

def getReferencies(consulta, arquivo):
    aparicoes = 0
    result = {}
    pla = False
    string = ''
    strings = ''
    inserida = ''


    for palavra in consulta:
        for element in arquivo:
            for palavraElemento in element:
                
                if(palavra == palavraElemento and type(palavraElemento) == str):
                    aparicoes = aparicoes + 1
                    pla = True
            
            if(pla):   
                num = len(element)
                string = string + ' ' + str(aparicoes) + ',' + str(element[num - 1])
                result[palavra] = string

            aparicoes = 0
            pla = False

        string = ''


    # for element in arquivo:
    #     for palavra in element:
    #         for essa in consulta:

    #             if(palavra == essa and type(essa) == str):

    #                 aparicoes = aparicoes + 1                    
    #                 pla = True
            
    #         if(pla):
    #             num = len(element)             
    #             string = string + ' ' + str(aparicoes) + ',' + str(element[num - 1])
    #             #string = result[palavra] + string
    #             result[palavra] = string

    #     aparicoes = 0
    #     string = ""
    #     resultado = ""
    #     pla = False

    return result


def main(conjunto:str, desconsideradas:str, consulta:str):

    with open(conjunto,"r") as arquivo:
        base = arquivo.readlines()

    links = []
    count = 0
    arq = []
    result = []
    

    for x in base:
        links.append(x)
        
    def chr_remove(old, to_remove):
        new_string = old
        for x in to_remove:
            new_string = new_string.replace(x, ' ')
        return new_string

    def add(links):
        count = ''
        for linksArquivo in links:      
            with open(linksArquivo.strip(), "r") as arquivo:
                isso = arquivo.readlines()                
                for x in isso:
                    count = count + x
                arq.append(count)
                count = ''
                #print(arq)
        return arq
            
    arq = add(links)
    soma = 0
    ss = 0
    for x in arq:
        semponto = chr_remove(x," . , ? !")
        count = semponto.split()                    
        count.append(soma)
        soma = soma + 1
        result.append(count)

    palavras = {}
    aux = 0
    for x in result:
        for s in x:
            for essa in desconsideradas:
                if(s != essa and type(s) == str):
                    palavras[s] = ''

    arq = getReferencies(palavras, result)
    print(arq)
    
consulta = ['casa', 'engracada']
desconsideradas = ['o','a','e','de','da','das','do','na','nas','no','em','nao','um','uns','uma','umas']

main("base.txt", desconsideradas, consulta)