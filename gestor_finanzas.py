def pedir_ingresos_por_dia():
    ingresos_del_lunes = float(input("Ingrese las ganancias de el dia lunes: "))
    ingresos_del_martes = float(input("Ingrese las ganancias de el dia martes: "))
    ingresos_del_miercoles = float(input("Ingrese las ganancias de el dia miercoles: "))
    ingresos_del_jueves = float(input("Ingrese las ganancias de el dia jueves: "))
    ingresos_del_viernes = float(input("ingrese las ganancias de el dia viernes: "))

    total_ingresos = ingresos_del_lunes + ingresos_del_martes + ingresos_del_miercoles + ingresos_del_jueves + ingresos_del_viernes 
    print(total_ingresos) 
    return total_ingresos 
def pedir_gastos_semanal():
    gastos_del_lunes = float(input("Ingrese los gastos de el dia lunes: "))
    gastos_del_martes = float(input("Ingrese los gastos de el dia martes: "))
    gastos_del_miercoles = float(input("Ingrese los gastos de el dia miercoles: "))
    gastos_del_jueves = float(input("Ingrese los gastos de el dia jueves: "))
    gastos_del_viernes = float(input("ingrese los gastos de el dia viernes: "))
    
    total_gastos = gastos_del_lunes + gastos_del_martes + gastos_del_miercoles + gastos_del_jueves + gastos_del_viernes
    print(total_gastos)
    return total_gastos
def calcular_y_mostrar_balance(ingresos, gastos):
    balance = ingresos - gastos
    if balance < 1000:
     print("Alerta: estás gastando demasiado")
    elif balance == 1000:
     print("Ingresos estables")
    elif balance > 1000: 
     print("Felicidades, está semana has tenido un buen rendimiento")

print("Control semanal de finanzas")
ingresos_totales = pedir_ingresos_por_dia()
gastos_totales = pedir_gastos_semanal()
calcular_y_mostrar_balance(ingresos_totales, gastos_totales)
