from datetime import datetime


def tipo_pan_chosen():
    tipo_pan = int((input('> Elige la opción 1, 2, 3 o 4: ')))
    if tipo_pan == 1:
        tipo_pan = 0.25
    elif tipo_pan == 2:
        tipo_pan = 0.30
    elif tipo_pan == 3:
        tipo_pan = 0.50
    elif tipo_pan == 4:
        tipo_pan = 0.20
    else:
        print('Has elegido una opción errónea. Vuelve a intentarlo.')
        tipo_pan_chosen()
    return tipo_pan

# validar porque cuando elijo varias opciones erroneas y luego la opcion correcta arroja un calculo erroneo


def costo_pan_normal():
    costo = tipo_pan_chosen()
    cantidad_pan = int(input('> Cantidad de panes: '))
    costo = round(costo * cantidad_pan, 2)
    print(f'El precio de {cantidad_pan} panes es de ${costo}.')


def costo_pan_dscto():
    costo = tipo_pan_chosen()
    cantidad_pan = int(input('> Cantidad de panes: '))
    costo = round((costo * cantidad_pan), 2)
    precio_dscto = round(costo - (costo*0.25), 2)
    ahorro = round(costo - precio_dscto, 2)
    print(f"""\n\nEl precio de {cantidad_pan} panes es de ${precio_dscto}.
> Debido a la hora actual tuviste un descuento de 25%.
> El dscto por la hora fue de ${ahorro}.
> El costo real hubiera sido de ${costo}""")


print('\t<Panadería Deliccie>')

hora_actual = datetime.now().time()
hora_actual2 = hora_actual.strftime("%H:%M:%S")
hora_dscto1 = datetime.strptime("10:00:00", "%X").time()
hora_dscto2 = datetime.strptime("16:00:00", "%X").time()
print(f"""\nSelecciona el tipo de pan a vender:\n
1. Pan Francés  - $0.25
2. Pan Caracol  - $0.30
3. Pan Ciabatta - $0.50
4. Pan Integral - $0.20 
\nLa hora actual es: {hora_actual2}\n""")

if hora_actual >= hora_dscto1 and hora_actual < hora_dscto2:
    costo_pan_dscto()
else:
    costo_pan_normal()
