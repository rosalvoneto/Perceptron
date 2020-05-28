class Mcp:
    
    def __init__(self, w1, w2, w3, n):
        self.w1 = w1
        self.w2 = w2
        self.w3 = w3
        self.n  = n
        
    def output(self, pattern):
        if ((pattern.x1 * self.w1) + (pattern.x2 * self.w2) + ((-1) * self.w3)) > 0:
            return 1
        else:
            return 0
        
    def delta(self, pattern, out):
        self.w1 = self.w1 + self.n * (pattern.y - out) * pattern.x1
        self.w2 = self.w2 + self.n * (pattern.y - out) * pattern.x2
        self.w3 = self.w3 + self.n * (pattern.y - out) * (-1) 
        
    def mostrarPesos(self):
        print ("W1: " ,self.w1, "W2: ", self.w2, "w0: ", self.w3)