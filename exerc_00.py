nome = str(input('Qual é seu nome? '))
if nome == 'Rodrigo':
    print('Que nome bonito!')
elif nome == 'Israel' or nome == 'Samara' or nome == 'Valdiana':
    print('seu nome é muito popular no Brasil.')  
elif nome in 'Ana Marijalma Carol Luciene':
    print('Lindo nome do integrante de sua familia')     
else:
    print('Seu nome é normal.')
print('Tenha um bom dia, {}!'.format(nome))        