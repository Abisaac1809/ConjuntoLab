class OperadorConjuntos:
    def __init__(self):
        self.operaciones = {
            '∪': lambda a, b: a.union(b),
            '∩': lambda a, b: a.intersection(b),  
            '-': lambda a, b: a.difference(b),  
        }
        self.precedencia = {'∩': 3, '∪': 2, '-': 2, "'": 4, '(': 1} 

    def tokenizar(self, expresion):
        tokens = []
        i = 0
        while i < len(expresion):
            c = expresion[i]
            if c in "∪∩-'()":
                tokens.append(c)
                i += 1
            elif c.isupper():
                j = i
                while j < len(expresion) and expresion[j].isupper():
                    j += 1
                tokens.append(expresion[i:j])
                i = j
            else:
                i += 1
        return tokens

    def infix_a_postfix(self, tokens):
        cola = []
        pila = []
        for token in tokens:
            if token == '(':
                pila.append(token)
            elif token == ')':
                while pila and pila[-1] != '(':
                    cola.append(pila.pop())
                pila.pop()
            elif token in self.precedencia:
                while pila and self.precedencia[pila[-1]] >= self.precedencia[token]:
                    cola.append(pila.pop())
                pila.append(token)
            else:
                cola.append(token) 
        while pila:
            cola.append(pila.pop())
        return cola

    def evaluar_postfix(self, postfix, conjuntos):
        pila = []
        for token in postfix:
            if token in conjuntos:
                pila.append(conjuntos[token])
            elif token == "'":  
                if len(pila) < 1:
                    return -1  
                a = pila.pop()
                if 'U' not in conjuntos:
                    return -1 
                U = conjuntos['U']
                resultado = U.difference(a)
                pila.append(resultado)
            elif token in self.operaciones:
                if len(pila) < 2:
                    return -1  
                b = pila.pop()
                a = pila.pop()
                resultado = self.operaciones[token](a, b)
                pila.append(resultado)
            else:
                return -1  
        if len(pila) != 1:
            return -1  
        if len(pila[0]) == 0:
            return 0  
        return pila[0]

    def evaluar_operacion(self, expresion, conjuntos):
        tokens = self.tokenizar(expresion)
        postfix = self.infix_a_postfix(tokens)
        return self.evaluar_postfix(postfix, conjuntos)