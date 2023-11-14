import requests
import re
import pandas as pd
import folium
from unidecode import unidecode
# Lista de URLs a serem analisadas
listaURLs = ['https://desaparecidos.policiacivil.mg.gov.br/desaparecido/album']
listaAlbum = []

# Regexs a serem aplicadas
regexLink = r'\/desaparecido\/exibir\/\d{4}'  # Regex para encontrar link
regexIdadesDesaparecimento = r'\d+\sanos'  # Regex para encontrar idade]
regexFaixaEtaria = r'\d{2}'
regexCidade = r'\w[A-Z].+\/MG'
regexBuscaCidade = r'.*(?=[\/])'

# Loop sobre as URLs
for cadaURL in listaURLs:
    # Baixar o conteúdo da página
    resposta = requests.get(cadaURL)

    # Verificar se a requisição foi bem-sucedida
    if resposta.status_code == 200:
        conteudoPagina = resposta.content.decode('utf-8')

        try:
            # Aplicar a regex sobre o conteúdo da página
            retornoRegexLink = re.findall(regexLink, conteudoPagina)
            # Verificar se foram encontrados resultados
            if len(retornoRegexLink) != 0:
                print(f"Nenhum resultado encontrado para a URL {cadaURL}")

        except:
            # Se houver algum erro na aplicação da regex, registrar que houve uma extração incorreta para essa URL
            print(f"Extração incorreta para a URL {cadaURL}")
    else:
        # Se a resposta não for 200, imprimir uma mensagem de erro de requisição para a URL atual
        print(
            f"Erro na requisição da URL {cadaURL} - Status: {resposta.status_code}")

listaAlbum = retornoRegexLink.copy()

for i in range(len(listaAlbum)):
    listaAlbum[i] = 'https://desaparecidos.policiacivil.mg.gov.br' + listaAlbum[i]

fileCidade = open("resultados\\cidades_minas.txt", "w")
fileIdade = open("resultados\\idades_minas.txt", "w")

print(f"Processando...")

for listaAlbumURLs in listaAlbum:
    # Baixar o conteúdo da página
    resposta = requests.get(listaAlbumURLs)

    # Verificar se a requisição foi bem-sucedida
    if resposta.status_code == 200:
        conteudoPagina = resposta.content.decode('utf-8')

        try:

            # Aplicar a regex sobre o conteúdo da página
            retornoRegexIdadeDesaparecimento = re.findall(
                regexIdadesDesaparecimento, conteudoPagina)

            # Verificar se foram encontrados resultados
            if len(retornoRegexIdadeDesaparecimento) > 0:
                # Escrever os resultados
                for combinacao in retornoRegexIdadeDesaparecimento:
                    fileIdade.write(f'{combinacao}\n')

            else:
                # Se nenhum resultado for encontrado, imprimir uma mensagem
                print(
                    f"Nenhum resultado de idade encontrado para a URL {listaAlbumURLs}")

        except:
            # Se houver algum erro na aplicação da regex, registrar que houve uma extração incorreta para essa URL
            print(f"Extração incorreta para a URL {listaAlbumURLs}")

        try:
            # Aplicar a regex sobre o conteúdo da página
            retornoRegexCidade = re.findall(
                regexCidade, conteudoPagina)

            if len(retornoRegexCidade) > 0:
                # Escrever os resultados
                for combinacaoCidade in retornoRegexCidade:
                    fileCidade.write(f'{combinacaoCidade}\n')

            else:
                # Se nenhum resultado for encontrado, imprimir uma mensagem
                print(
                    f"Nenhum resultado de cidade encontrado para a URL {listaAlbumURLs}")

        except:
            # Se houver algum erro na aplicação da regex, registrar que houve uma extração incorreta para essa URL
            print(f"Extração incorreta para a URL {listaAlbumURLs}")
    else:
        # Se a resposta não for 200, imprimir uma mensagem de erro de requisição para a URL atual
        print(
            f"Erro na requisição da URL {listaAlbumURLs} - Status: {resposta.status_code}")


fileIdade.close()
fileCidade.close()
file = open("resultados\\idades_minas.txt", "r")
fileIdadeText = file.read()

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

file = open("resultados\\idades_minas.txt", "a")

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

file = open("resultados\\cidades_minas.txt", "r")
file_cidade = file.read()

listacidades = re.findall(regexBuscaCidade, file_cidade)
listaRepetidoCidades = set(listacidades)

file.close()
file = open("resultados\\cidades_minas.txt", "r")
file_cidade = file.read()

listacidades = re.findall(regexBuscaCidade, file_cidade)
listaRepetidoCidades = set(listacidades)

file.close()


file = open("resultados\\cidades_minas.txt", "a")
lista_ordenada = sorted(listaRepetidoCidades)


for i in lista_ordenada:
    if (i == ''):
        file.write(
            f'\n{listacidades.count(i)} Pessoas desaparecidas sem registro de cidade\n')
    else:
        file.write(
            f'{i} possuí  {listacidades.count(i)} Pessoas desaparecidas\n')

file.close()

coord = pd.read_csv("Dataframe\\municipios.csv", na_values=['?'])
lista_ordenada.remove('')
listaCoord = []

df_minas = coord.query("codigo_uf == 31")

for i, dados in df_minas.iterrows():

    for j in lista_ordenada:
        if unidecode(dados.nome.upper()) == j:
            listaCoord.append(dados.latitude)
            listaCoord.append(dados.longitude)

# print(listaCoord)

mapa = folium.Map(location=[-19.916667, -43.933333], zoom_start=7)


for i in range(0, len(listaCoord), 2):
    folium.Marker(location=[listaCoord[i], listaCoord[i+1]],
                  popup='Numero de desaparecimentos: ' +
                  str(listacidades.count(
                      lista_ordenada[int(i/2)])) + " pessoas",
                  tooltip=str(lista_ordenada[int(i/2)])
                  ).add_to(mapa)

mapa.save("resultados\\mapa.html")
