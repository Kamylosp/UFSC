lista_nome_meses = ["janeiro", "fevereiro", "marco",
         "abril", "maio", "junho",
         "julho", "agosto", "setembro",
         "outubro", "novembro", "dezembro"]

entrada = input("Digite a data no formato (dd/mm/aaaa): ")

dia, mes, ano = int(entrada[:2]), int(entrada[3:5]), int(entrada[6:])

mes_nome = lista_nome_meses[mes-1]

print(f"{dia}/{mes}/{ano} -> mes: {mes_nome}")
