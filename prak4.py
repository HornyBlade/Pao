# Ассортимент автосалона раритетных авто (модель:поколение)

Model={'Mazda RX-7' : 'FC3S' , 'Mazda MX-5' : ['ND','NB','NC'] , 'Nissan Skyline' : ['2000','R30','R33','R34'] , 'Buick Grand National' : ['1982','1983','1986'] , 'Plymouth Roadrunner':['Gen1 1968' , 'Gen1 1969' , 'Gen3 1975']}

# Просмотрим Ассортимент по моделям

print('Модели:',Model.keys())

# Просмотрим доступные поколения одной из машин

print('Поколения Mazda MX-5:',Model['Mazda MX-5'])

# 12 числа на склад поступили: Nissan Skyline R32, Mazda RX-7 FD3S, последний Nissan Skyline 2000 нашел своего покупателя.

Model['Mazda RX-7']=['FC3S','FD3S']
Model['Nissan Skyline']=['R30','R32','R33','R34']

print("Ассортимент на 12 число: \n",Model)

# 14 числа появилась новая модель: Chevrolet Corvette, в кузове C3 "Stingray"

Model.update({'Chevrolet Corvette':'C3 "Stingray"'})

# Просмотрим эту модель в каталоге
#check=str(input('Введите модель для просмотра поколений: '))
#print('Поколения',check,':', Model[check])

#Проверка наличия конкретной модели авто
def Наличие():
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
#Наличие()


#Отследим Поставки Buick Grand National 1982 модельного года. Для этого обратимся к документам транспортной компании

Buick_Grand_National_1982_Transfer_Count=[20, 18, -16, 14, 2, -3] # Список перевозок: "+" это направление на склад, "-" это направление со склада, шт

# Сосчитаем остаток авто этой модели на складе.

Buick_Grand_National_1982_Storage_Count=0
for n in range(len(Buick_Grand_National_1982_Transfer_Count)):
    Buick_Grand_National_1982_Storage_Count+=Buick_Grand_National_1982_Transfer_Count[n]
    
# Также, для этой операции можно было воспользоваться функцией sum()

#print('Количество Buick Grand National 1982 на складе:', Buick_Grand_National_1982_Storage_Count)


#^^ Рабочая программа ^^





#Блок разработки
Count={}
i=0
a=[*Model.keys()]

for i in range(len(a)):
    Count.update({str(a[i]):''})
#print(Count.keys())
def Поступление():
    print(Model.keys())
    print("Введите модель")
    b=str(input(''))
    if b in Model.keys():
        print('Введите количество')
        c=int(input(''))
        return b, Count.update({b:c})

def files():
    text1= open('Models.txt', mode= 'r')
    text2= text1.read(10)
    print(text2)
    text1.close()
    
    text3=open('Text1.txt','w')
    text3.write('dvjnkvjbs  77  ')
    L=['dibijcoi','disjcib','dichuiuh','sdcbhib']
    text3.writelines(L)
    text3.close()
    
    text4=open('Text1.txt', mode='a')
    text4.writelines('   2131235')
    text4.close()
files()

        
        
    



    
    
    