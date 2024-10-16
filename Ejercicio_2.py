'''Dada una cadena que contiene solo los caracteres "(" y ")", implementa una función
que determina si los paréntesis están correctamente balanceados. Un conjunto de
paréntesis está equilibrado si:
● Cadaparéntesisdeapertura tiene un paréntesis de cierre correspondiente.
● Losparéntesisdeapertura se cierran en el orden correcto.'''

def estan_balanceados(parentesis: str) -> bool:
    # Pila para almacenar los parentesis de apertura
    pila = []
    
    # Recorre cada carácter en la cadena
    for char in parentesis:
        if char == '(':  # Si encuentra un parentesis de apertura
            pila.append(char)  # Lo apila
        elif char == ')':  # Si encuentra un parentesis de cierre
            if not pila:  # Si la pila está vacía, no hay paréntesis de apertura correspondiente
                return False
            pila.pop()  # Saca un parentesis de apertura correspondiente
    
    # Al final, la pila debe estar vacía si todos los paréntesis están balanceados
    return len(pila) == 0

print(estan_balanceados("()"))        # True
print(estan_balanceados("(()())"))    # True
print(estan_balanceados(")("))        # False
print(estan_balanceados("((())"))     # False