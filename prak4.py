# Ассортимент автосалона раритетных авто (модель:поколение)

Model={'Mazda RX-7' : 'FC3S' , 'Mazda MX-5' : ['ND','NB','NC'] , 'Nissan Skyline' : ['2000','R30','R33','R34'] , 'Buick Grand National' : ['1982','1983','1986'] , 'Plymouth Roadrunner':['Gen1 1968' , 'Gen1 1969' , 'Gen3 1975']}

# Просмотрим Ассортимнт по моделям

print(Model.keys())

# Просмотрим доступные поколения одной из машин

print('Поколения Mazda MX-5:',Model['Mazda MX-5'])

# 12 числа на склад поступили: Nissan Skyline R32, Mazda RX-7 FD3S, последний Nissan Skyline 2000 нашел своего покупателя.

Model['Mazda RX-7']=['FC3S','FD3S']
Model['Nissan Skyline']=['R30','R32','R33','R34']

print("Ассортимент на 12 число: \n",Model)

# 14 числа появилась новая модель: Chevrolet Corvette, в кузове C3 "Stingray"

Model.update({'Chevrolet Corvette':'C3 "Stingray"'})

# Просмотрим эту модель в каталоге

print('Поколения Corvette:', Model['Chevrolet Corvette'])

#Проверка наличия конкретной модели авто

print('Введите модель')
M1=str(input(''))
if M1 in Model.keys():
    print('Введите код кузова/модельный год')
    M2=str(input(''))
    M0=Model[M1]
    if M2 in M0:
        print('В наличии')
    else:
        print('Отсутствует')
else:
    print('Отсутствует')
    