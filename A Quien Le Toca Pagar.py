# A Quien Le Toca Pagar

giles = ["Juan Prodimac", "Negro AmigoAjeno", "FacuMec", "Cucchi", "Negro", "Grandote", "Bruno Cornelio", "Mojarita", "Bicho"]

from datetime import date, datetime

today = date.today() # today. year/month/day

variable_ano = False # Se usa en linea 88
variable_dia = False # Se usa en linea 145

meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]

dias = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]

def funcion_real():
  print(" ")
  dia = (input(f"Ingrese el numero del Dia que cae el {str_dia_semana.title()}:"))
  try:
    int(dia)
    datetime(ano,mes,int(dia), 00, 00, 00, 00000)
    return int(dia)
  except ValueError:
    print(" ")
    print ("No se ingreso un numero valido")
    return funcion_real()
   
def funcion_fecha_unida():
    fecha_unida = datetime(ano,mes,dia, 00, 00, 00, 00000)
    #fecha_unida.weekday() dia de la semana en un int, lunes es 0 domingo es 6
    return fecha_unida

def funcion_fecha():
  print(" ")
  print("La Fecha que usted ingreso es:")
  print(" ")
  print("Año: ", ano, " Mes: ", mes, " Dia: ", dia, " Dia Semana: ", str_dia_semana.title())
  print(" ")

def funcion_semana():
  print(" ")
  str_dia_semana = str(input("Ingrese el Dia de la Semana que se organiza la comida en el Sector: ")).lower()
  return str_dia_semana

def funcion_ano():
  print(" ")
  ano = (input("Ingrese el Año solicitado: "))
  try:
    int(ano)
    return int(ano)
  except ValueError:
    print(" ")
    print ("No se ingreso un numero")
    return funcion_ano()

def funcion_mes():
  print(" ")
  str_mes = str(input("Ingrese el Mes solicitado: ")).lower()
  return str_mes

str_dia_semana = funcion_semana() #pido el dia de la semana

while not(str_dia_semana in dias):
  print(" ")
  print("No se selecciono un Dia de la Semana valido")
  str_dia_semana = funcion_semana()
if str_dia_semana == "lunes":
  dia_semana = 0
elif str_dia_semana == "martes":
  mdia_semana = 1
elif str_dia_semana == "miercoles":
  dia_semana = 2
elif str_dia_semana == "jueves":
  dia_semana = 3
elif str_dia_semana == "viernes":
  dia_semana = 4
elif str_dia_semana == "sabado":
  dia_semana = 5
elif str_dia_semana == "domingo":
  dia_semana = 6
else:
  print(" ")
  print("Conseguiste Romper Todo Amigo")
  exit()

ano = funcion_ano() #pido el año

while variable_ano == False:
  if ano > today.year+1 or ano <= 1921:
    print(" ")
    print("No se selecciono un año valido")
    ano = funcion_ano()
  else:
    variable_ano = True

str_mes = funcion_mes() #pido el mes

while not(str_mes in meses):
  print(" ")
  print("No se selecciono un Mes valido")
  str_mes = funcion_mes()
if str_mes == "enero" or str_mes == "1":
  str_mes = "enero"
  mes = 1
elif str_mes == "febrero" or str_mes == "2":
  str_mes = "febrero"
  mes = 2
elif str_mes == "marzo" or str_mes == "3":
  str_mes = "marzo"
  mes = 3
elif str_mes == "abril" or str_mes == "4":
  str_mes = "abril"
  mes = 4
elif str_mes == "mayo" or str_mes == "5":
  str_mes = "mayo"
  mes = 5
elif str_mes == "junio" or str_mes == "6":
  str_mes = "junio"
  mes = 6
elif str_mes == "julio" or str_mes == "7":
  str_mes = "julio"
  mes = 7
elif str_mes == "agosto" or str_mes == "8":
  str_mes = "agosto"
  mes = 8
elif str_mes == "septiembre" or str_mes == "9":
  str_mes = "septiembre"
  mes = 9
elif str_mes == "octubre" or str_mes == "10":
  str_mes = "octubre"
  mes = 10
elif str_mes == "noviembre" or str_mes == "11":
  str_mes = "noviembre"
  mes = 11
elif str_mes == "diciembre" or str_mes == "12":
  str_mes = "diciembre"
  mes = 12
else:
  print(" ")
  print("Conseguiste Romper Todo Amigo")
  exit()

dia = funcion_real() #pido el dia

while variable_dia == False:
  fecha_unida = funcion_fecha_unida()
  if fecha_unida.weekday() != dia_semana:
    print(" ")
    print(f"El Dia {dia} no corresponde al Dia de la Semana {str_dia_semana.title()} del Mes {str_mes.title()} del Año {ano}")
    dia = funcion_real()
  else:
    variable_dia = True
    fecha_unida = funcion_fecha_unida()

funcion_fecha()

contador_weak = 0
ano_e=1921
mes_e=1
dia_e=1
ano_empieza = datetime(ano_e,mes_e,dia_e, 00, 00, 00, 00000)

semana_ano_empieza = ano_empieza.isocalendar()

semana_ano_empieza_week = semana_ano_empieza[1]

semana_fecha_unida = fecha_unida.isocalendar()

semana_fecha_unida_week = semana_fecha_unida[1]

anos_diferencia = fecha_unida.year - ano_empieza.year

contador_anos_diferencia = 0

while contador_anos_diferencia < anos_diferencia-1:
    mes_e=12
    dia_e=31
    ano_e+=1
    ano_empieza = datetime(ano_e,mes_e,dia_e, 00, 00, 00, 00000)
    contador_weak += semana_ano_empieza_week
    contador_anos_diferencia+=1

contador_final = contador_weak + semana_fecha_unida_week

ubicacion_giles = contador_final%len(giles)
ubicacion_giles2 = (contador_final + int((len(giles)/2)+1))%len(giles)
print('-'*75)
print(f'''
Paga los Sanguchitos -->  {giles[ubicacion_giles]}

Paga las gaseosas -->  {giles[ubicacion_giles2]}
''')
print('-'*75)
