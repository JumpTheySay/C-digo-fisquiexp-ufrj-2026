
import matplotlib.pyplot as plt
import numpy as np

def interpolar(x, x_inf, x_sup, y_inf, y_sup):

    # Isolando matematicamente o 'y' da equação fornecida no relatório:
    y = ((y_sup - y_inf) * (x - x_inf)) / (x_sup - x_inf) + y_inf
    return y

celsius_alvo = 60.0
f_calculado = interpolar(x=celsius_alvo, x_inf=0.0, x_sup=100.0, y_inf=32.0, y_sup=212.0)

print(f"Resultado do script: {celsius_alvo}°C equivale a {f_calculado}°F")

print("LEGADO: CÁLCULO AUTOMÁTICO DE Λ0 PARA AS PRÓXIMAS TURMAS")

# Dicionário de referência da literatura para o Ácido Acético:
# Chave: Temperatura em °C | Valor: Lambda_0 (mho.cm²/Eq-g)
tabela_literatura = {
    23: 378.0,
    24: 384.0
}

# Dados coletados no experimento (Temperaturas efetivas de cada solução)
temperaturas_experimentais = {
    "Solução 1 (0,0050 N)": 23.4,
    "Solução 2 (0,0100 N)": 23.3,
    "Solução 3 (0,0500 N)": 23.6,
    "Solução 4 (0,1000 N)": 23.1
}

# Definição dos limites fixos com base na tabela disponível (23°C e 24°C)
T_inf, Lambda_inf = 23, tabela_literatura[23]
T_sup, Lambda_sup = 24, tabela_literatura[24]

# Loop para processar e exibir os resultados de forma organizada
for solucao, T_efetiva in temperaturas_experimentais.items():
    lambda_0_calculado = interpolar(
        x=T_efetiva,
        x_inf=T_inf,
        x_sup=T_sup,
        y_inf=Lambda_inf,
        y_sup=Lambda_sup
    )
    print(f"> {solucao}: Temperatura = {T_efetiva}°C -> Λ0 calculado = {lambda_0_calculado:.1f} mho.cm²/Eq-g")

# Dicionário de referência da literatura para o Ácido Acético:
# Chave: Temperatura em °C | Valor: Lambda_0 (mho.cm²/Eq-g)
tabela_literatura = {
    23: 378.0,
    24: 384.0
}

# Dados coletados no experimento (Temperaturas efetivas de cada solução)
temperaturas_experimentais = {
    "Solução 1 (0,0050 N)": 23.4,
    "Solução 2 (0,0100 N)": 23.3,
    "Solução 3 (0,0500 N)": 23.6,
    "Solução 4 (0,1000 N)": 23.1
}

# Definição dos limites fixos com base na tabela disponível (23°C e 24°C)
T_inf, Lambda_inf = 23, tabela_literatura[23]
T_sup, Lambda_sup = 24, tabela_literatura[24]

# Loop para processar e exibir os resultados de forma organizada
for solucao, T_efetiva in temperaturas_experimentais.items():
    lambda_0_calculado = interpolar(
        x=T_efetiva,
        x_inf=T_inf,
        x_sup=T_sup,
        y_inf=Lambda_inf,
        y_sup=Lambda_sup
    )
    print(f"> {solucao}: Temperatura = {T_efetiva}°C -> Λ0 calculado = {lambda_0_calculado:} mho.cm²/Eq-g")

# 1. Função de Interpolação Linear (O Legado)
def interpolar(x, x_inf, x_sup, y_inf, y_sup):
    return ((y_sup - y_inf) * (x - x_inf)) / (x_sup - x_inf) + y_inf

# 2. Dados de Referência da Literatura (Limites de 23°C e 24°C)
t_inf, lambda_inf = 23.0, 378.0
t_sup, lambda_sup = 24.0, 384.0

# 3. Dados Experimentais do Grupo (Temperatura vs Lambda_0 calculado)
solucoes = ["Sol. 1 (0,0050 N)", "Sol. 2 (0,0100 N)", "Sol. 3 (0,0500 N)", "Sol. 4 (0,1000 N)"]
temps_exp = np.array([23.4, 23.3, 23.6, 23.1])
lambdas_exp = np.array([interpolar(t, t_inf, t_sup, lambda_inf, lambda_sup) for t in temps_exp])

# 4. Construção do Gráfico
plt.figure(figsize=(9, 5), dpi=100)

# Linha contínua representando o comportamento linear teórico nesse intervalo térmico
t_linha = np.linspace(22.9, 24.1, 100)
lambda_linha = interpolar(t_linha, t_inf, t_sup, lambda_inf, lambda_sup)
plt.plot(t_linha, lambda_linha, color='#2c3e50', linestyle='--', alpha=0.7, label='Reta de Interpolação Teórica')

# Pontos de controle da literatura (os limites da tabela)
plt.scatter([t_inf, t_sup], [lambda_inf, lambda_sup], color='#e74c3c', s=100, zorder=5, label='Pontos da Literatura (Tabela)')

# Pontos experimentais calculados pelo script
plt.scatter(temps_exp, lambdas_exp, color='#2980b9', s=120, edgecolors='black', zorder=6, label='Lambda Ajustado')

# Adicionando rótulos de texto para cada solução experimental no gráfico
for i, txt in enumerate(solucoes):
    plt.annotate(f" {txt}\n ({temps_exp[i]}°C, {lambdas_exp[i]:.1f})",
                 (temps_exp[i], lambdas_exp[i]),
                 textcoords="offset points",
                 xytext=(10,-10),
                 ha='left', fontsize=9, color='#34495e',
                 bbox=dict(boxstyle="round,pad=0.3", fc="yellow", alpha=0.2, ec="gray"))

# Customização estética do gráfico
plt.title('Legado - Ajuste Lambda por Interpolação Linear', fontsize=12, fontweight='bold', pad=15)
plt.xlabel('Temperatura (C)', fontsize=11, labelpad=10)
plt.ylabel('mho.cm2/eq.g)', fontsize=11, labelpad=10)
plt.xlim(22.9, 24.1)
plt.ylim(376, 386)
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(loc='upper left', frameon=True, facecolor='white', edgecolor='none')

# Exibir o gráfico na tela
plt.tight_layout()
plt.show()
