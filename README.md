# Classe-Matriz
Em construção.

Não é nada de novo que estou fazendo. Estou apenas treinando.

## Como usar:
    1. Acesse a pasta onde se encontra o arquivo Matriz.py
    2. Rode via terminal/cmd com o comando 'python -i Matriz.py'. Se estive no Jupyter Notebook pode-se importar com 'from Matriz import *' 
 
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

**lin(self,vetor,i):**

Insere o vetor na linha i.

**col(self,vetor,j):**

Insere o vetor na coluna j. 

**perm(self,i,j)**

Permuta a linha i com a linha j. L_i <-> L_j

**mult(self,i,k):**

Multiplica a linha i pelo número real k.

**somar(self,i,i2,k):**

Soma à linha i k vezes os valores de i2.
[a,b,c]+k[a',b',c']=[a+ka',b+kb',c+kc']

**sub(self,i,i2,k):**

Subtrai à linha i k vezes os valores de i2.
[a,b,c]-k[a',b',c']=[a-ka',b-kb',c-kc']
  
**cofat(self,i,j):**

Retorna o cofator da posição i,j.

**macofat(self):**

Retorna a matriz de cofatores.

**inversa(self)**:

Retorna a matriz inversa.

E, claro, as funções somar(+), subtrair(-), multiplicar(*) e igual (==). 
 
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
  
  
**Int(self):**

Converte uma matriz de float em uma matriz de int.

**cramer(self):**

Resolve o sistema de equações lineares.

a11*x1, a12*x2,...,a1n*xn=b1
	.
	.
	.
	
an1*x1,an2*x2,...,ann*xn=bn
