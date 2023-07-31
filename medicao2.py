import pandas as pd
import matplotlib.pyplot as plt


planilha1 = pd.read_excel("Medições das plantas das hortas.xlsx", sheet_name="Amostra 1")
planilha2 = pd.read_excel("Medições das plantas das hortas.xlsx", sheet_name='Amostra 2')
planilha3 = pd.read_excel("Medições das plantas das hortas.xlsx", sheet_name='Amostra 3')
planilha4 = pd.read_excel("Medições das plantas das hortas.xlsx", sheet_name='Amostra 4')
planilha5 = pd.read_excel("Medições das plantas das hortas.xlsx", sheet_name='Amostra 5') 


planilha1_alturaH = planilha1["Altura H"]
planilha1_larguraH = planilha1["Largura H"]
planilha1_alturaV = planilha1["Altura V"]
planilha1_larguraV = planilha1["Largura V"]

planilha2_alturaH = planilha2["Altura H"]
planilha2_larguraH = planilha2["Largura H"]
planilha2_alturaV = planilha2["Altura V"]
planilha2_larguraV = planilha2["Largura V"]

planilha3_alturaH = planilha3["Altura H"]
planilha3_larguraH = planilha3["Largura H"]
planilha3_alturaV = planilha3["Altura V"]
planilha3_larguraV = planilha3["Largura V"]

planilha4_alturaH = planilha4["Altura H"]
planilha4_larguraH = planilha4["Largura H"]
planilha4_alturaV = planilha4["Altura V"]
planilha4_larguraV = planilha4["Largura V"]

planilha5_alturaH = planilha5["Altura H"]
planilha5_larguraH = planilha5["Largura H"]
planilha5_alturaV = planilha5["Altura V"]
planilha5_larguraV = planilha5["Largura V"]


fig, ax = plt.subplots()

ax.plot(planilha1_alturaH, label="Amostra 1 Altura H")
ax.plot(planilha1_larguraH, label="Amostra 1 Largura H")
ax.plot(planilha1_alturaV, label="Amostra 1 Altura V")
ax.plot(planilha1_larguraV, label="Amostra 1 Largura V")

ax.plot(planilha2_alturaH, label="Amostra 2 Altura H")
ax.plot(planilha2_larguraH, label="Amostra 2 Largura H")
ax.plot(planilha2_alturaV, label="Amostra 2 Altura V")
ax.plot(planilha2_larguraV, label="Amostra 2 Largura V")

ax.plot(planilha3_alturaH, label="Amostra 3 Altura H")
ax.plot(planilha3_larguraH, label="Amostra 3 Largura H")
ax.plot(planilha3_alturaV, label="Amostra 3 Altura V")
ax.plot(planilha3_larguraV, label="Amostra 3 Largura V")

ax.plot(planilha4_alturaH, label="Amostra 4 Altura H")
ax.plot(planilha4_larguraH, label="Amostra 4 Largura H")
ax.plot(planilha4_alturaV, label="Amostra 4 Altura V")
ax.plot(planilha4_larguraV, label="Amostra 4 Largura V")

ax.plot(planilha5_alturaH, label="Amostra 5 Altura H")
ax.plot(planilha5_larguraH, label="Amostra 5 Largura H")
ax.plot(planilha5_alturaV, label="Amostra 5 Altura V")
ax.plot(planilha5_larguraV, label="Amostra 5 Largura V")

ax.set_xlabel('Observações')
ax.set_ylabel('cm')
ax.set_title('Alface Roxa - Observação Amostras')    
ax.legend()
plt.show()
