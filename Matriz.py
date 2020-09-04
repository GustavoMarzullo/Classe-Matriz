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
     
        
    def ordem(self):
        '''Ordem m x n da matriz.'''
        return len(self.vetor),len(self.vetor[0])
    
    
    def __add__(self,other):
        '''Retorna a adição de duas matrizes.'''
        
        def somar(_vetor1,_vetor2):
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
                _matriz[i]=somar(_matriz[i],other.vetor[i])
            return matriz(_matriz)
    
    
    def __sub__(self,other):
        
        def subtrair(_vetor1,_vetor2):
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
                _matriz[i]=subtrair(_matriz[i],other.vetor[i])
            return matriz(_matriz)
    
    
    def __mul__(self,other):
        if type(self) == matriz and type(other) == matriz:
            pass
        
        else:
            def multiplicar(_vetor1,k):
                '''k*[A,B,C]=[k*A,k*B,k*C]'''
                _vetor3=_vetor1.copy()
                for i in range(len(_vetor3)):
                    _vetor3[i]=_vetor3[i]*k
                return _vetor3
            
            _matriz=self.vetor.copy()
            for i in range(len(_matriz)):
                _matriz[i]=multiplicar(_matriz[i],other)
            return matriz(_matriz)
                
    def __truediv__(self,other):
        if type(self) == matriz and type(other) == matriz:
            pass
        
        else:
            def dividir(_vetor1,k):
                '''[A,B,C]/k=[A/k,B/k,C/k]'''
                _vetor3=_vetor1.copy()
                for i in range(len(_vetor3)):
                    _vetor3[i]=_vetor3[i]/k
                return _vetor3
            
            _matriz=self.vetor.copy()
            for i in range(len(_matriz)):
                _matriz[i]=dividir(_matriz[i],other)
            return matriz(_matriz)
        
    def __round__(self,n):
        for linha in range(len(self.vetor)):
            for coluna in range(len(self.vetor[0])):
                self.vetor[linha][coluna]=round(self.vetor[linha][coluna],n)
        return matriz(self.vetor)
                
    
            
            
            
        
        
        
    
    
    