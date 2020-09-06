class matriz:
    def __init__(self,vetor):
        self.vetor=vetor
    
    def __repr__(self):
        return ('\n'.join([''.join(['{:6}'.format(item) for item in row]) for row in self.vetor]))
    
    
    def __str__(self):
        return ('\n'.join([''.join(['{:6}'.format(item) for item in row]) for row in self.vetor]))
    
    
    def valor(self,i=None,j=None):
        '''Retorna o valor da posição i,j. Caso um dois dois se omita, retorna a linha i ou a coluna j.'''
        if j==None: #retornando só a linha
            return self.vetor[i-1]
        
        elif i==None: #retornando só a coluna
            L=[]
            for linha in self.vetor:
                L.append(linha[j-1])
            return L
        
        else: #retornando um valor i,j
            return self.vetor[i-1][j-1] 
     

    def __getitem__(self,pos):
        '''Retorna o item na posição i,j.'''
        i,j=pos
        return self.vetor[i-1][j-1]
    
    
    def __setitem__(self,pos,valor): 
        i,j=pos
        self.vetor[i-1][j-1] = valor
        
 
    def ordem(self):
        '''Ordem m x n da matriz.'''
        return len(self.vetor),len(self.vetor[0])


    def __round__(self,n):
        for i in range(len(self.vetor)):
            for j in range(len(self.vetor[0])):
                self.vetor[i][j]=round(self.vetor[i][j],n)
        return matriz(self.vetor)    
    
    
    def __add__(self,other):
        '''Retorna a adição de duas matrizes.'''
        
        def _somar(_vetor1,_vetor2):
            '''[A,B,C] + [D,E,F]=[A+D,B+E,C+F]'''
            _vetor3=_vetor1.copy()
            for i in range(len(_vetor3)):
                _vetor3[i]=_vetor3[i]+_vetor2[i]
            return _vetor3 
    
        if self.ordem()!=other.ordem():
            raise ValueError ('Matrizes com ordens diferentes.')
        
        else:
            _matriz=self.vetor.copy()
            for i in range(len(_matriz)):
                _matriz[i]=_somar(_matriz[i],other.vetor[i])
            return matriz(_matriz)
    
    
    def __sub__(self,other):
        def _subtrair(_vetor1,_vetor2):
            '''[A,B,C] - [D,E,F]=[A-D,B-E,C-F]'''
            _vetor3=_vetor1.copy()
            for i in range(len(_vetor3)):
                _vetor3[i]=_vetor3[i]-_vetor2[i]
            return _vetor3 
    
        if self.ordem()!=other.ordem():
            print('Matrizes com ordens diferentes.')
        
        else:
            _matriz=self.vetor.copy()
            for i in range(len(_matriz)):
                _matriz[i]=_subtrair(_matriz[i],other.vetor[i])
            return matriz(_matriz)
    
    
    
    def __mul__(self,other):
        
        if type(self) == type(other): #mutiplicação de matrizes
        
                m,n=self.ordem()[0] ,self.ordem()[1] #linhas de self, colunas de self
                p,q=other.ordem()[0],other.ordem()[1] #linhas de other, colunas de other
                
                if n!=p:
                    raise ValueError ('Matrizes incompatíveis') 
                    
                C=nula(m,q)
                for i in range(1,m+1): #iterando sobre as linhas de self
                    for j in range(1,other.ordem()[1]+1): #iterando sobre as colunas de other
                        soma=0
                        for k in range(1,other.ordem()[0]+1): #iterando sobre as linhas de other
                            soma+= self[i,k] * other[k,j] 
                        C[i,j]=soma
                return C 
        
        else: #multiplicação de matriz por escalar  
            def _multiplicar(_vetor1,k):
                '''k*[A,B,C]=[k*A,k*B,k*C]'''
                _vetor3=_vetor1.copy()
                for i in range(len(_vetor3)):
                    _vetor3[i]=_vetor3[i]*k
                return _vetor3
            
            _matriz=self.vetor.copy()
            for i in range(len(_matriz)):
                _matriz[i]=_multiplicar(_matriz[i],other)
            return matriz(_matriz)
  
              
    def __truediv__(self,other):
        
        if type(self) == matriz and type(other) == matriz:   
            return  self * matriz(inverter(other))
              
        else:
            def _dividir(_vetor1,k):
                '''[A,B,C]/k=[A/k,B/k,C/k]'''
                _vetor3=_vetor1.copy()
                
                for i in range(len(_vetor3)):
                    _vetor3[i]=_vetor3[i]/k
                return _vetor3
            
            _matriz=self.vetor.copy()
            for i in range(len(_matriz)):
                _matriz[i]=_dividir(_matriz[i],other)
            return matriz(_matriz)
        

    def __eq__(self,other):
        if self.ordem() != other.ordem():
            return False

        for i in range(len(self.vetor)):
            for j in range(len(self.vetor[0])):
                if self.vetor[i][j] != other.vetor[i][j]:
                    return False
        return True
        
        
    def T(self): 
        '''Transpõe a matriz.'''
        transposta=[]
        for _ in range(len(self.vetor[0])):
            transposta.append(self.valor(j=_+1))
        return matriz(transposta)
    
#funções fora da classe 

def para_matriz(A,_float=False,sep=';'):
    '''Converte uma string em um vetor de vetores.
    \nsep => separador das linhas da matriz.
    \n_float => se True, converte para float, caso contrário, converte para int.'''
    
    def converter(lista,_float):
        '''Converte lista de string para lista de int ou float.'''
        if _float==False:
            for i in range(len(lista)):
                lista[i]=int(lista[i])
        else:
            for i in range(len(lista)):
                lista[i]=float(lista[i])

    A_split=A.split(sep)
    L=[]
    for i in A_split:
        L.append(i.split(','))
    for i in L:
        converter(i,_float)
    return matriz(L)       

def nula(m,n):
    '''Cria uma matriz nula de ordem m x n.'''
    vetor=[[0 for coluna in range(n)] for linha in range(m)] #evitar "reference share" 
    return matriz(vetor)

def identidade(m):
    '''Cria uma matriz identidade de ordem m.'''
    identidade=nula(m,m)
    for i in range(1,m+1):
        for j in range(1,m+1):
            if i==j:
                identidade[i,j]=1
    return identidade

def inverter(_matriz):
    '''[A,B,C] => [1/A,1/B,1/C]'''
    _vetor1=[[1/coluna for coluna in linha] for linha in _matriz.vetor] #evitar "reference share" 
    return _vetor1

def oposta(_matriz):
    '''[A,B,C] => [-A,-B,-C]'''
    _vetor1=[[-coluna for coluna in linha] for linha in _matriz.vetor] #evitar "reference share" 
    return matriz(_vetor1)
