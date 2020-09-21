# Classe-Matriz
Em construção.

Não é nada de novo que estou fazendo. Estou apenas treinando.

## Como usar:
    1. Acesse a pasta onde se encontra o arquivo Matriz.py
    2. Rode o python via terminal/cmd
    3. Importe usando o comando "from Matriz import *"
 
 Para criar um objeto da classe matriz: matriz([[a11,a12,...,a1n],....[an1,an2,...,anm]] ou com a função Matriz. 
 
 ## Funções disponíveis dentro da classe Matriz:
 
 **valor(self, i=None, j= None):**
 
Retorna o valor da posição i,j. Caso algum se omita retorna a linha i ou a coluna j. 
 
 **getitem(self,pos):**
 
Retorna o item na pos i,j. Ex: A[i,j]. Tem o setitem que define o item na posição i,j. 

**ordem(self):**

Retorna a ordem (mxn) da matriz.

**T(self):**

Tranpõe a matriz. 

**inverter(self):** 

[A,B,C] => [1/A,1/B,1/C]

**oposta(self):**

[A,B,C] => [-A,-B,-C]

**det(self):**

Retorna o determinante da matriz. Referência: _https://www.blogcyberini.com/2017/10/determinantes-via-triangularizacao.html_.
 
**tr(self):**

Calcula o traço (soma dos valors nas diagonais) da matriz.

**perm(self,i,j)**

Permuta a linha i com a linha j. L_i <-> L_j

**mult(self,i,k):**

Multiplica a linha i pelo número real k.

**somar(self,i,i2):**

Soma à linha i os valores de i2.
[a,b,c]+[a',b',c']=[a+a',b+b',c+c']

**sub(self,i,i2):**

Subtrai à linha i os valores de i2.
[a,b,c]-[a',b',c']=[a-a',b-b',c-c']
  
  
E, claro, as funções somar(+), subtrair(-) e multiplicar(*). 
 
# Funções fora da classe

**Matriz(A,_float=False,sep_linhas=';',sep_col=','):**

Converte uma string em uma matriz. 
sep => separador das linhas da matriz.
_float => se True, converte para float, caso contrário, converte para int.

**nula(m,n):**

Cria uma matriz identidade de ordem m,n.

**I(m,n):**

Cria uma matriz identidade de ordem m,n.

**diagonal(vetor):**

Cria uma matriz diagonal seguindo a ordem dos números do vetor.
  
