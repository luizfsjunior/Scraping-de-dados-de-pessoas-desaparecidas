import re

# Lista de URLs a serem analisadas
listaURLs = open(
    'Sites salvos\\SIPOL - Portal de Desaparecidos.html', 'r', encoding="utf-8")

# Regexs a serem aplicadas
regexIdadesDesaparecimento = r'\d+\sanos'  # Regex para encontrar idade]
regexFaixaEtaria = r'\d{2}'


resposta = listaURLs.read()

fileIdade = open("resultados\\idades_rio.txt", "w")

print(f"Processando...")


try:
    # Aplicar a regex sobre o conteúdo da página
    retornoRegexIdadeDesaparecimento = re.findall(
        regexIdadesDesaparecimento, resposta)

    # Verificar se foram encontrados resultados
    if len(retornoRegexIdadeDesaparecimento) > 0:
        # Escrever os resultados
        for combinacao in retornoRegexIdadeDesaparecimento:
            fileIdade.write(f'{combinacao}\n')

    else:
        # Se nenhum resultado for encontrado, imprimir uma mensagem
        print(f"Nenhum resultado de idade encontrado para a URL {listaURLs}")

except:
    # Se houver algum erro na aplicação da regex, registrar que houve uma extração incorreta para essa URL
    print(f"Extração incorreta para a URL {listaURLs}")


fileIdade.close()
file = open("resultados\\idades_rio.txt", "r")
fileIdadeText = file.read()
print(fileIdadeText)

listaIdades = re.findall(regexFaixaEtaria, fileIdadeText)

contadorMenores18 = 0
contadorMenores30 = 0
contadorMenores45 = 0
contadorMenores60 = 0
contadorMenores100 = 0


for i in range(len(listaIdades)):
    if int(listaIdades[i]) > 0 and int(listaIdades[i]) < 18:
        contadorMenores18 = contadorMenores18 + 1
    elif int(listaIdades[i]) > 18 and int(listaIdades[i]) < 30:
        contadorMenores30 = contadorMenores30 + 1
    elif int(listaIdades[i]) > 30 and int(listaIdades[i]) < 45:
        contadorMenores45 = contadorMenores45 + 1
    elif int(listaIdades[i]) > 45 and int(listaIdades[i]) < 60:
        contadorMenores60 = contadorMenores60 + 1
    elif int(listaIdades[i]) > 60 and int(listaIdades[i]) < 100:
        contadorMenores100 = contadorMenores100 + 1


file.close()

file = open("resultados\\idades_rio.txt", "a")

file.write(
    f'Quantidade aproximada de pessoas com a Faixa Etária entre 0 e 17 anos = {contadorMenores18} Pessoas\n')
file.write(
    f'Quantidade aproximada de pessoas com a Faixa Etária entre 18 e 29 anos = {contadorMenores30} Pessoas\n')
file.write(
    f'Quantidade aproximada de pessoas com a Faixa Etária entre 30 e 44 anos = {contadorMenores45} Pessoas\n')
file.write(
    f'Quantidade aproximada de pessoas com a Faixa Etária entre 45 e 59 anos = {contadorMenores60} Pessoas\n')
file.write(
    f'Quantidade aproximada de pessoas com a Faixa Etária entre 60 e 99 anos = {contadorMenores100} Pessoas\n')

file.close()
listaURLs.close()
