def menu(titulo,lista):
    print('========================================')
    print(titulo.upper())
    print('========================================')
    while True:
        i=1
        for elem in lista:
            print(i,'.-',elem)
            i+=1
        print(i,'.- Salir')
        opc=input('Ingrese Opción: ')
        if opc.isdigit():
            opc_int=int(opc)
            if opc_int>=1 and opc_int<=i:
                return opc_int
            else:
                print('Debe Ingresar un Número entre 1 y ',i)
        else:
            print('Ingrese Sólo Números')

def menu_seleccion(titulo,lista):
    print('========================================')
    print(titulo.upper())
    print('========================================')
    while True:
        i=1
        for elem in lista:
            print(i,'.-',elem)
            i+=1
        print(i,'.- Salir')
        opc=input('Ingrese Opción: ')
        if opc.isdigit():
            opc_int=int(opc)
            if opc_int>=1 and opc_int<=i:
                return opc_int-1
            else:
                print('Debe Ingresar un Número entre 1 y ',i)
        else:
            print('Ingrese Sólo Números')

def sueldos_orden(lista):
    total_sueldos=0
    for tra in lista:
        if tra.get('Sueldo')<800000:
            print('----Sueldos menores a $800.000----\n')
            print('Nombre Empleado            Sueldo')
            print(tra.get('Trabajador'), '       ',tra.get('Sueldo'))
            print()
        elif 800000<=tra.get('Sueldo')<2000000:
            print('----Sueldos entre $800.000 y $2.000.000----\n')
            print('Nombre Empleado            Sueldo')
            print(tra.get('Trabajador'), '       ',tra.get('Sueldo'))
            print()
        elif 2000000<=tra.get('Sueldo'):
            print('----Sueldos superiores a $2.000.000----\n')
            print('Nombre Empleado            Sueldo')
            print(tra.get('Trabajador'), '       ',tra.get('Sueldo'))
            print()
            
        total_sueldos=total_sueldos+tra.get('Sueldo')
        print(total_sueldos)


lis_trabajadores_sueldos=[]
trabajadores=['Juan Pérez', 'María García', 'Carlos López', 'Ana Martinez', 'Pedro Rodriguez', 'Laura Hernández', 'Miguel Sánchez', 'Isabel Gómez', 'Francisco Díaz', 'Elena Fernández']
sueldos=[300000, 450000, 500000, 600000, 720000, 1000000, 1300000, 1800000, 2200000, 2500000]


general=['Asignar Sueldos', 'Clasificar Sueldos', 'Ver Estadisticas', 'Reporte de sueldos']

while True:
    opc_men=menu('Menu Principal', general)
    if opc_men==1:
        while True:
            opc_trabajador=menu_seleccion('Elija trabajador', trabajadores)
            dic_trabajadores_sueldos={}
            if 0<=opc_trabajador<=9:
                trabajador_str=trabajadores[opc_trabajador]
                dic_trabajadores_sueldos['Trabajador']=trabajador_str
                while True:
                    opc_sueldo=menu_seleccion('Elija sueldo', sueldos)
                    if 0<=opc_sueldo<=9:
                        sueldo_int=sueldos[opc_sueldo]
                        dic_trabajadores_sueldos['Sueldo']=sueldo_int 
                        lis_trabajadores_sueldos.append(dic_trabajadores_sueldos) 
                        break
                    elif opc_sueldo==10:
                        break
                    else:
                        print('Elija opciones dadas')
            elif opc_trabajador==10:
                print(lis_trabajadores_sueldos)
                break
            else:
                print('Elija entre las opciones dadas')
    elif opc_men==2:
        print(sueldos_orden(lis_trabajadores_sueldos))
        break
    elif opc_men==3:
        def sueldos_orden(lista):
            li_sueldos=[]
            for suel in lista:
                li_sueldos.append(suel.get('Sueldo'))
            return li_sueldos
        salario_listado=sueldos_orden(lis_trabajadores_sueldos)
        salario_ordenado=sorted(salario_listado)
        print('')
        print('Salario mas bajo')
        print('$', salario_ordenado[0])
        print('')
        print('Salario más alto')
        print('$', salario_ordenado[-1])
        print('Promedio salario')
        def sueldos_orden(lista):
            prom_sueldos=0
            for suel in lista:
                prom_sueldos+=suel.get('Sueldo')/len(lista)
            return prom_sueldos
        print(sueldos_orden(trabajadores))
    elif opc_men==4:
        print('opc4')
    elif opc_men==5:
        print('Finalizando programa...\nDesarrollado por Claudio Iribarne\nRUT 16.262.773-2')
        break
    else:
        print('Elija una opcion entre 1 a 5')