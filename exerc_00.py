nome = str(input('Qual é seu nome? '))
if nome == 'Rodrigo':
    print('Que nome bonito!')
elif nome == 'Israel' or nome == 'Samara' or nome == 'Valdiana':
    print('seu nome é muito popular no Brasil.')   
else:
    print('Seu nome é normal.')
print('Tenha um bom dia, {}!'.format(nome))        