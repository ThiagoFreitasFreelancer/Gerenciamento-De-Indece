
def PrimeiroCaso(consulta, arquivo):
    aparicoes = 0
    result = {}
    pla = False
    string = ''

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

    return result

def SegundoCaso(consulta, arquivo, nomeArquivo):
    aparicoes = 0
    result = []
    pla = False
    contu = 0
    aux = ''

    for palavra in consulta:
        for element in arquivo:
            
            for palavraElemento in element:
                
                if(palavra == palavraElemento and type(palavraElemento) == str):
                    aparicoes = aparicoes + 1
                    pla = True
            
            if(pla):
                num = len(element)
                elem = element[num - 1]
                if nomeArquivo[elem] not in aux:
                    aux = aux + ' ' + nomeArquivo[elem]
                contu = aparicoes + contu

            aparicoes = 0
            pla = False
            
        result = str(contu) + aux
        #aux = ''
            
           
            

    return result

def main(conjunto:str, desconsideradas:str, consulta:str, tipoConsulta:str):

    with open(conjunto,"r") as arquivo:
        base = arquivo.readlines()

    links = []
    count = 0
    arq = []
    result = []
    nomeArquivo = []
    

    for x in base:
        links.append(x)
        nomeArquivo.append(x[len(x) - 6:len(x) - 1])
        
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

    if(tipoConsulta == ','):
        if(consulta):
            arq = PrimeiroCaso(consulta, result)
            print(arq)
        else:
            arq = PrimeiroCaso(palavras, result)
            print(arq)
    else:
        arq = SegundoCaso(consulta, result, nomeArquivo)
        print(arq)

consulta = ['casa', "engracada"] #Caso vazio, todas a palavras do arquivo exeto as desconsideradas serao retornadas

desconsideradas = ['o','a','e','de','da','das','do','na','nas','no','em','nao','um','uns','uma','umas']

main("base.txt", desconsideradas, consulta, ',')

main("base.txt", desconsideradas, consulta, ';')