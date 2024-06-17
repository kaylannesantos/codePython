#se o rendimento do cidadão for inferior a 85.528 thalers, o imposto era igual a 18% do rendimento menos 556 thalers e 2 cêntimos
#se o rendimento fosse superior a 85.528 thalers, o imposto seria igual a 14.839 thalers e 2 cêntimos, mais 32% do excedente acima de 85.528 thalers.

#entrada
rendimento = float(input("Informe seu rendimento anual: "))
#variaveis
limite = 85528.00
desagravamentoFiscal = 556.02
taxa_inicial = 18/100
taxa_excedente = 32/100
imposto_fixo = 14839.00

#processamento
if rendimento <= limite and rendimento > 0:
    imposto = round((rendimento * (18/100)) - 556.2, 0)
elif rendimento > limite: 
    excedente = rendimento - limite
    imposto = round(imposto_fixo + (excedente * taxa_excedente), 0)
elif rendimento <= 0:
    imposto = 0

print('Valor do imposto: ', imposto, ' thaler')