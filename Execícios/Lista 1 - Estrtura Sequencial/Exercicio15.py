valor_recebido = float(input("Insira o valor recebido por hora trabalhada: R$"))
horas_traba_mes = float(input("Insira as horas trabalhadas no mes: "))

salario_bruto = valor_recebido * horas_traba_mes
valor_inss = salario_bruto * 0.08
valor_sindicato = salario_bruto * 0.05
valor_ir = salario_bruto * 0.11
salario_liquido = salario_bruto - valor_inss - valor_ir - valor_sindicato

print("Salario Bruto: R$", salario_bruto, "\nIR(11%): R$", valor_ir, "\nINSS(8%): R$", valor_inss, "\nSindicato(5%): R$", valor_sindicato)