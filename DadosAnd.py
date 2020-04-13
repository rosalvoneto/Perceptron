from Pattern import Pattern

class DadosAnd:
    
    def getDados(self):
        # Padrao 1 
        x1 = 0
        x2 = 0
        y  = 0
        p1 = Pattern(x1, x2, y)
        
        # Padrao 2 
        x1 = 0
        x2 = 1
        y  = 0
        p2 = Pattern(x1, x2, y)
        
        # Padrao 3 
        x1 = 1
        x2 = 0
        y  = 0
        p3 = Pattern(x1, x2, y)
        
        # Padrao 4 
        x1 = 1
        x2 = 1
        y  = 1
        p4 = Pattern(x1, x2, y)
        
        dados = []
        
        dados.append(p1)
        dados.append(p2)
        dados.append(p3)
        dados.append(p4)
        
        return dados