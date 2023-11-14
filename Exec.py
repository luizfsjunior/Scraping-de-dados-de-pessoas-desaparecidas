import os

if not os.path.exists("resultados"):

    os.makedirs("resultados")

exec(open("Estado_Rio_de_Janeiro.py").read())
exec(open("Estado_Minas_Gerais.py").read())
exec(open("Instagram.py").read())


os.rename("desaparecidosdhppce", 'resultados\\desaparecidosdhppce')
os.rename("desaparecidospcba", 'resultados\\desaparecidospcba')
os.rename("sinalidplidal", 'resultados\\sinalidplidal')
