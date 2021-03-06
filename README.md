# Gerenciamento-De-Indece
## ORI 2022.1 - UESC 
## Professor: Elinaldo Santos de Goes Júnior 
### Atividade 
#### Descrição 
#### Esse trabalho consiste na criação de um programa de gerenciamento de índices para um conjunto de arquivos no contexto de um sistema de Recuperação da Informação. 
#### O conjunto de arquivos 
#### É composto por número arbitrário de arquivos de texto. Nesses arquivos, as palavras são separadas por um ou mais dos seguintes caracteres: espaço ( ), ponto (.), vírgula (,), exclamação (!) ou interrogação (?). Assuma também que todo o conteúdo dos arquivos está escrito em caracteres minúsculos e sem acentuação. 
#### Entrada do programa 
#### Seu programa deverá receber três argumentos como entrada. O primeiro argumento deve especificar o caminho de um arquivo texto que contém os caminhos de todos os arquivos da base “conjunto de arquivos”, cada um em uma linha. O segundo argumento especifica o caminho de um arquivo texto que traz uma lista de palavras que devem ser desconsideradas, com uma palavra por linha. Essas palavras não possuem significado semântico para o sistema, portanto, não devem ser consideradas na construção do índice. O último argumento é o caminho de um arquivo contendo uma consulta a ser respondida. 
#### Exemplo: Vamos supor que nosso conjunto inicial é composto pelos arquivos a.txt, b.txt e c.txt. Vamos supor também que nosso executável se chama “indice.exe”. Assim, chamamos nosso programa pela linha de comando fazendo: 
#### $ indice.exe conjunto.txt desconsideradas.txt consulta.txt 
#### Onde o arquivo conjunto.txt contém caminhos para os demais arquivos: 
#### a.txt 
#### b.txt 
#### c.txt



#### conjunto.txt 
#### O arquivo desconsideradas.txt possui uma lista de palavras que não deverão ser consideradas na construção do índice:
-----------------------------------------------------------------------
#### o 
#### a 
#### e 
#### de 
#### da 
#### das 
#### do 
#### das 
#### na 
#### nas
#### no 
#### nas 
#### em 
#### nao 
#### um 
#### uns 
#### uma 
#### umas
----------------------------------------------------------------------
#### desconsideradas.txt 
#### E o arquivo consulta.txt contém o conteúdo de uma consulta. Assuma que a consulta é composta por termos do vocabulário da base de documentos, com um operador AND (,) entre eles. Por exemplo: 
#### casa,engracada



#### consulta1.txt 
#### No exemplo acima, a consulta requisita documentos com os termos “casa” e “engracada”. 
#### Já no exemplo a seguir, é exemplificada uma consulta utilizando o operador OR (;): 
#### engracada;favor



#### consulta2.txt 
#### No exemplo acima, a consulta requisita documentos com os termos “engracada” ou “favor”. 
#### O programa deverá gerar dois arquivos de saída: 
#### 1 – indice.txt: arquivo com o índice invertido; 
#### 2 – resposta.txt: arquivo com a resposta a consulta de entrada. 
#### 1 – Arquivo indice.txt 
#### O arquivo de saída indice.txt, conterá o índice gerado a partir dos documentos da base. Para a geração desse índice, é preciso considerar cada palavra não desconsiderada que apareça em algum dos documentos da base. Para cada uma dessas palavras no índice, é preciso apontar o número do arquivo em que a mesma aparece, e a quantidade de vezes em que a mesma aparece no arquivo. Os arquivos são numerados segundo a ordem em que aparecem no arquivo que indica os documentos do conjunto, que, para o nosso exemplo, foi denominado como conjunto.txt. Assim, o arquivo a.txt é o arquivo 1, o arquivo b.txt é o arquivo 2 e, por fim, o arquivo c.txt é o arquivo 3. 
#### Suponha que estes arquivos estejam preenchidos conforme abaixo:
#### a.txt b.txt c.txt 

#### Nesse, exemplo, o arquivo indice.txt gerado seria composto por:
_______________________________________________________________
#### amor: 3,1 
#### casa: 1,1 2,4 3,1 
#### casar: 3,2 
#### comigo: 3,2 
#### engracada: 1,1 
#### era: 1,1 
#### faca: 3,1 
#### favor: 3,1 
#### minha: 3,1 
#### mora: 2,1 3,1 
#### muito: 1,1 
#### nada: 1,1 
#### quem: 2,2 
#### quer: 2,2 3,2 
#### tambem: 2,1 
#### teto: 1,1 
#### tinha: 1,2
______________________________________________________________

#### indice.txt 
#### Observe que, para cada palavra no índice, temos uma lista de pares a,q onde a é o número do arquivo em que a palavra aparece, e q é a quantidade de vezes em que a palavra aparece no arquivo. Assim, para a palavra “casa”, por exemplo, temos o par 1,1, indicando que no arquivo 1, este termo aparece uma vez. Em seguida, temos o par 2,4, indicando que no arquivo 2 este termo apareceu 4 vezes. Por fim, temos o par 3,1, indicando que, no arquivo 3, este termo aparece uma vez. Note que as palavras desconsideradas não devem entrar no índice! 
#### 2 – Arquivo resposta.txt 
#### O arquivo resposta.txt contém a resposta à consulta em consulta.txt. A primeira linha desse arquivo deve conter a quantidade de documentos que satisfazem a consulta. As demais linhas contêm os arquivos da base que atendem a consulta, conforme os exemplos: 
#### O arquivo resposta1.txt demonstra a resposta que o programa deve retornar para a primeira consulta, no arquivo consulta1.txt.
#### 1 
#### a.txt



#### resposta1.txt 
#### Já o arquivo resposta2.txt demonstra a resposta que o programa deve retornar para a segunda consulta, no arquivo consulta2.txt. 
#### 2 
#### a.txt 
#### c.txt



#### resposta2.txt 
#### Linguagens 
#### C, C++, Java, Python, Ruby, etc.
