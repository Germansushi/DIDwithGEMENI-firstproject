tasks = []

print("Введите ваши задачи. Чтобы закончить, напишите 'стоп'.")

while True:  # Этот цикл бесконечный, пока мы его сами не прервем
    new_task = input("Что нужно сделать? ")

    if new_task == "стоп":
        break  # Команда break мгновенно останавливает любой цикл


    elif new_task =="очистить":
        tasks.clear()
    tasks.append(new_task)

print("--- Твой список дел на сегодня ---")
for t in tasks:
    print(f"- {t}")