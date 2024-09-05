from myopen import MyOpen


with MyOpen('meuarquivo.txt', 'w') as file:
    file.write('Linha 01\n')
    file.write('Linha 02\n')
    file.write('Linha 03\n')
