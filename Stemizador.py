palavra = 'Correr'

#Redução de plural
tam = len(palavra)
if(palavra[tam -1] =='s'):
    palavra = palavra[:tam-1]
    tam = len(palavra)


#Redução de Feminino
if(palavra[tam -1 ] =='a'):
    palavra[tam-1] ='0'
    palavra = palavra[:-1]+ '0'


#Redução de Aumentativo
if(palavra[-2:] =='ão' or palavra[-2:] =='õe'):
    palavra = palavra[:-2]
    tam = len(palavra)


#Redução de advérbio
if(palavra[-5:]=='mente'):
    palavra=palavra[:-5]


#redução de substantivo
if(palavra[-3:] =='dor'):
    palavra=palavra[:-3]
    tam = len(palavra)

#Redução de Verbo
if(any(palavra[-2:]== f for f in ['ar','er','ir'])):
    palavra=palavra[:-2]
    tam=len(palavra)

#Redução da Vogal


print(palavra)