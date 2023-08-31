import pandas as pd
import matplotlib.pyplot as plt

grupo_planilha = []


num_amostras = 5
while num_amostras > 0:
    sheet_name = 'Amostra ' + str(num_amostras)
    planilha = pd.read_excel("Medições das plantas das hortas.xlsx", sheet_name=sheet_name)
    grupo_planilha.append(planilha)
    num_amostras -= 1

planilha1 = pd.read_excel("Medições das plantas das hortas.xlsx", sheet_name='Amostra 1')

              

num_planilhas = len(grupo_planilha)-1

num_show = 1

while num_planilhas >= 0:
    planilha_atual = grupo_planilha[num_planilhas]
    dados_alturaH = planilha_atual["Altura H"]
    dados_larguraH = planilha_atual["Largura H"]
    dados_alturaV = planilha_atual["Altura V"]
    dados_larguraV = planilha_atual["Largura V"]
    dados_alturaControle = planilha_atual["Altura Controle"]
    dados_larguraControle = planilha_atual["Largura Controle"]
    
    fig, ax = plt.subplots()
    ax.plot(dados_alturaH, label = 'Altura H', color = 'blue', linestyle='--')
    ax.plot(dados_alturaV, label = 'Altura V', color = 'red', linestyle='--')
    ax.plot(dados_larguraH, label = 'Largura H', color = 'blue', linestyle=':')
    ax.plot(dados_larguraV, label = 'Largura V', color = 'red', linestyle=':' )
    ax.plot(dados_larguraControle, label = 'Largura Controle', color = 'black', linestyle='-' )
    ax.plot(dados_alturaControle, label = 'Altura Controle', color = 'black', linestyle='-' )
    ax.set_xlabel('Observações')
    ax.set_ylabel('cm')
    ax.set_title('Alface Roxa - Observação Amostra ' + str(num_show))
    num_planilhas -= 1
    num_show += 1
    ax.legend()


num_planilhas = len(grupo_planilha)-1
num_show = 1

while num_planilhas >= 0:
    planilha_atual = grupo_planilha[num_planilhas]
    dados_alturaH = planilha_atual["Altura H R"]
    dados_larguraH = planilha_atual["Largura H R"]
    dados_alturaV = planilha_atual["Altura V R"]
    dados_larguraV = planilha_atual["Largura V R"]
    dados_alturaControle = planilha_atual["Altura Controle R"]
    dados_larguraControle = planilha_atual["Largura Controle R"]
    
    fig, ax = plt.subplots()
    ax.plot(dados_alturaH, label = 'Altura H', color = 'blue', linestyle='--')
    ax.plot(dados_alturaV, label = 'Altura V', color = 'red', linestyle='--')
    ax.plot(dados_larguraH, label = 'Largura H', color = 'blue', linestyle=':')
    ax.plot(dados_larguraV, label = 'Largura V', color = 'red', linestyle=':' )
    ax.plot(dados_larguraControle, label = 'Largura Controle', color = 'black', linestyle='-' )
    ax.plot(dados_alturaControle, label = 'Altura Controle', color = 'black', linestyle='-' )
    ax.set_xlabel('Observações')
    ax.set_ylabel('cm')
    ax.set_title('Rucula - Observação Amostra ' + str(num_show))
    num_planilhas -= 1
    num_show += 1
    ax.legend()


    

plt.show()

