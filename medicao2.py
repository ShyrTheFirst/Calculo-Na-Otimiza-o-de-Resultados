import pandas as pd
import matplotlib.pyplot as plt


planilha1 = pd.read_excel("Medições das plantas das hortas.xlsx", sheet_name="Amostra 1")
planilha2 = pd.read_excel("Medições das plantas das hortas.xlsx", sheet_name='Amostra 2')
planilha3 = pd.read_excel("Medições das plantas das hortas.xlsx", sheet_name='Amostra 3')
planilha4 = pd.read_excel("Medições das plantas das hortas.xlsx", sheet_name='Amostra 4')
planilha5 = pd.read_excel("Medições das plantas das hortas.xlsx", sheet_name='Amostra 5')



planilha1_alturaControle = planilha1["Altura Controle"]
planilha1_larguraControle = planilha1["Largura Controle"]
planilha1_alturaH = planilha1["Altura H"]
planilha1_larguraH = planilha1["Largura H"]
planilha1_alturaV = planilha1["Altura V"]
planilha1_larguraV = planilha1["Largura V"]

planilha2_alturaControle = planilha2["Altura Controle"]
planilha2_larguraControle = planilha2["Largura Controle"]
planilha2_alturaH = planilha2["Altura H"]
planilha2_larguraH = planilha2["Largura H"]
planilha2_alturaV = planilha2["Altura V"]
planilha2_larguraV = planilha2["Largura V"]

planilha3_alturaControle = planilha3["Altura Controle"]
planilha3_larguraControle = planilha3["Largura Controle"]
planilha3_alturaH = planilha3["Altura H"]
planilha3_larguraH = planilha3["Largura H"]
planilha3_alturaV = planilha3["Altura V"]
planilha3_larguraV = planilha3["Largura V"]

planilha4_alturaControle = planilha4["Altura Controle"]
planilha4_larguraControle = planilha4["Largura Controle"]
planilha4_alturaH = planilha4["Altura H"]
planilha4_larguraH = planilha4["Largura H"]
planilha4_alturaV = planilha4["Altura V"]
planilha4_larguraV = planilha4["Largura V"]

planilha5_alturaControle = planilha5["Altura Controle"]
planilha5_larguraControle = planilha5["Largura Controle"]
planilha5_alturaH = planilha5["Altura H"]
planilha5_larguraH = planilha5["Largura H"]
planilha5_alturaV = planilha5["Altura V"]
planilha5_larguraV = planilha5["Largura V"]


fig, ax = plt.subplots()

ax.plot(planilha1_alturaControle, label="Amostra 1 Altura Controle")
ax.plot(planilha1_larguraControle, label="Amostra 1 Largura Controle")
ax.plot(planilha1_alturaH, label="Amostra 1 Altura H")
ax.plot(planilha1_larguraH, label="Amostra 1 Largura H")
ax.plot(planilha1_alturaV, label="Amostra 1 Altura V")
ax.plot(planilha1_larguraV, label="Amostra 1 Largura V")

ax.plot(planilha2_alturaControle, label="Amostra 2 Altura Controle")
ax.plot(planilha2_larguraControle, label="Amostra 2 Largura Controle")
ax.plot(planilha2_alturaH, label="Amostra 2 Altura H")
ax.plot(planilha2_larguraH, label="Amostra 2 Largura H")
ax.plot(planilha2_alturaV, label="Amostra 2 Altura V")
ax.plot(planilha2_larguraV, label="Amostra 2 Largura V")

ax.plot(planilha3_alturaControle, label="Amostra 3 Altura Controle")
ax.plot(planilha3_larguraControle, label="Amostra 3 Largura Controle")
ax.plot(planilha3_alturaH, label="Amostra 3 Altura H")
ax.plot(planilha3_larguraH, label="Amostra 3 Largura H")
ax.plot(planilha3_alturaV, label="Amostra 3 Altura V")
ax.plot(planilha3_larguraV, label="Amostra 3 Largura V")

ax.plot(planilha4_alturaControle, label="Amostra 4 Altura Controle")
ax.plot(planilha4_larguraControle, label="Amostra 4 Largura Controle")
ax.plot(planilha4_alturaH, label="Amostra 4 Altura H")
ax.plot(planilha4_larguraH, label="Amostra 4 Largura H")
ax.plot(planilha4_alturaV, label="Amostra 4 Altura V")
ax.plot(planilha4_larguraV, label="Amostra 4 Largura V")

ax.plot(planilha5_alturaControle, label="Amostra 5 Altura Controle")
ax.plot(planilha5_larguraControle, label="Amostra 5 Largura Controle")
ax.plot(planilha5_alturaH, label="Amostra 5 Altura H")
ax.plot(planilha5_larguraH, label="Amostra 5 Largura H")
ax.plot(planilha5_alturaV, label="Amostra 5 Altura V")
ax.plot(planilha5_larguraV, label="Amostra 5 Largura V")

ax.set_xlabel('Observações')
ax.set_ylabel('cm')
ax.set_title('Alface Roxa - Observação Amostras')    
ax.legend()

planilha1_alturaControleR = planilha1["Altura Controle R"]
planilha1_larguraControleR = planilha1["Largura Controle R"]
planilha1_alturaHR = planilha1["Altura H R"]
planilha1_larguraHR = planilha1["Largura H R"]
planilha1_alturaVR = planilha1["Altura V R"]
planilha1_larguraVR = planilha1["Largura V R"]

planilha2_alturaControleR = planilha2["Altura Controle R"]
planilha2_larguraControleR = planilha2["Largura Controle R"]
planilha2_alturaHR = planilha2["Altura H R"]
planilha2_larguraHR = planilha2["Largura H R"]
planilha2_alturaVR = planilha2["Altura V R"]
planilha2_larguraVR = planilha2["Largura V R"]

planilha3_alturaControleR = planilha3["Altura Controle R"]
planilha3_larguraControleR = planilha3["Largura Controle R"]
planilha3_alturaHR = planilha3["Altura H R"]
planilha3_larguraHR = planilha3["Largura H R"]
planilha3_alturaVR = planilha3["Altura V R"]
planilha3_larguraVR = planilha3["Largura V R"]

planilha4_alturaControleR = planilha4["Altura Controle R"]
planilha4_larguraControleR = planilha4["Largura Controle R"]
planilha4_alturaHR = planilha4["Altura H R"]
planilha4_larguraHR = planilha4["Largura H R"]
planilha4_alturaVR = planilha4["Altura V R"]
planilha4_larguraVR = planilha4["Largura V R"]

planilha5_alturaControleR = planilha5["Altura Controle R"]
planilha5_larguraControleR = planilha5["Largura Controle R"]
planilha5_alturaHR = planilha5["Altura H R"]
planilha5_larguraHR = planilha5["Largura H R"]
planilha5_alturaVR = planilha5["Altura V R"]
planilha5_larguraVR = planilha5["Largura V R"]

fig2, ax2 = plt.subplots()

ax2.plot(planilha1_alturaControleR, label="Amostra 1 Altura Controle Rucula")
ax2.plot(planilha1_larguraControleR, label="Amostra 1 Largura Controle Rucula")
ax2.plot(planilha1_alturaHR, label="Amostra 1 Altura H Rucula")
ax2.plot(planilha1_larguraHR, label="Amostra 1 Largura H Rucula")
ax2.plot(planilha1_alturaVR, label="Amostra 1 Altura V Rucula")
ax2.plot(planilha1_larguraVR, label="Amostra 1 Largura V Rucula")

ax2.plot(planilha2_alturaControleR, label="Amostra 2 Altura Controle Rucula")
ax2.plot(planilha2_larguraControleR, label="Amostra 2 Largura Controle Rucula")
ax2.plot(planilha2_alturaHR, label="Amostra 2 Altura H Rucula")
ax2.plot(planilha2_larguraHR, label="Amostra 2 Largura H Rucula")
ax2.plot(planilha2_alturaVR, label="Amostra 2 Altura V Rucula")
ax2.plot(planilha2_larguraVR, label="Amostra 2 Largura V Rucula")

ax2.plot(planilha3_alturaControleR, label="Amostra 3 Altura Controle Rucula")
ax2.plot(planilha3_larguraControleR, label="Amostra 3 Largura Controle Rucula")
ax2.plot(planilha3_alturaHR, label="Amostra 3 Altura H Rucula")
ax2.plot(planilha3_larguraHR, label="Amostra 3 Largura H Rucula")
ax2.plot(planilha3_alturaVR, label="Amostra 3 Altura V Rucula")
ax2.plot(planilha3_larguraVR, label="Amostra 3 Largura V Rucula")

ax2.plot(planilha4_alturaControleR, label="Amostra 4 Altura Controle Rucula")
ax2.plot(planilha4_larguraControleR, label="Amostra 4 Largura Controle Rucula")
ax2.plot(planilha4_alturaHR, label="Amostra 4 Altura H Rucula")
ax2.plot(planilha4_larguraHR, label="Amostra 4 Largura H Rucula")
ax2.plot(planilha4_alturaVR, label="Amostra 4 Altura V Rucula")
ax2.plot(planilha4_larguraVR, label="Amostra 4 Largura V Rucula")

ax2.plot(planilha5_alturaControleR, label="Amostra 5 Altura Controle Rucula")
ax2.plot(planilha5_larguraControleR, label="Amostra 5 Largura Controle Rucula")
ax2.plot(planilha5_alturaHR, label="Amostra 5 Altura H Rucula")
ax2.plot(planilha5_larguraHR, label="Amostra 5 Largura H Rucula")
ax2.plot(planilha5_alturaVR, label="Amostra 5 Altura V Rucula")
ax2.plot(planilha5_larguraVR, label="Amostra 5 Largura V Rucula")

ax2.set_xlabel('Observações')
ax2.set_ylabel('cm')
ax2.set_title('Rucula - Observação Amostras')    
ax2.legend()


plt.show()
