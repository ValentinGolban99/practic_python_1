# Максим программирует целый день на работе и вечером идёт домой. 
# Каждый час начальство кидает ему несколько задач, которые нужно решить до следующего рабочего часа. 
# Вдобавок каждый час Максиму звонит супруга. Он знает, что если он возьмёт трубку, 
# то жена попросит зайти вечером в магазин.
# Напишите программу, в которой считается, сколько задач выполнил Максим за день (восемь часов). 
# Если он хотя бы раз взял трубку, то в конце дополнительно выводите сообщение: «Нужно зайти в магазин».

count = 0
task_max = 0
count_call = 0
print("Начался 8-часовой рабочий день.")
while count != 8:
    
    count += 1
    print(count, "й час")
    task = int(input("Сколько задач решит Максим? "))
    task_max += task
    
    phone_call = int(input("Звонит жена, взять трубку?(1 - да, 0 - нет): "))
    if phone_call == True:
        count_call += 1
    
print("Рабочий день закончился. Всего выполнено задачь: ", task_max)
if count_call > 0:
    print("Нужно сходить в магазин.")


