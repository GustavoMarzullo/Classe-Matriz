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
            '''[A,B,C] + [D,E,F]=[A-D,B-E,C-F]'''
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
        if type(self) == matriz and type(other) == matriz:
            if len(self.valor(i=1)) != len(other.valor(j=1)):
                raise ValueError ('Número de colunas da primeira diferente do número de linhas da segunda')
            #a continuar
                
        else:
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
            pass #a fazer
        
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
