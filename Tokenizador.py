
#Adaptado por Victor Félix Arinos... rs

def separador (texto, adicionada = False, simbolos = ['.', "!", "?", ","]):
	tokensFinal = []
	tokens = texto.split(' ')
	print(tokens)
	for token in tokens:
		print(token)
		
		for simbolo in simbolos:
			subTokens = token.split(simbolo)
			print(subTokens)
			if(len(subTokens) > 1):
				if(not adicionada):				
					tokensFinal.append(subTokens[0])
				i = 1
				aux = simbolo
				while(subTokens[i] == '' and i < len(subTokens) -1):
					aux = aux + simbolo
					i = i + 1
		
				tokensFinal.append(aux)
	
				aux = subTokens[1]
				if(aux != ''):
					tokensFinal.append(aux)
				adicionada = True
	
		if(not adicionada):
			tokensFinal.append(token)
		adicionada = False
	
	return tokensFinal





FinaldosToken = separador("Mas amada, o que está acontecendo??? Voce parece triste. Se cuida!")


print(FinaldosToken)
