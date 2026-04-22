from storage import load_habits, save_habits
from datetime import datetime, timedelta
def show_menu():
    print("   ТРЕКЕР ПРИВЫЧЕК")
    print("1. Добавить привычку")
    print("2. Список привычек")
    print("3. Отметить выполнение")
    print("4. Статистика")
    print("5. Выход")
def add_habit():
    print("\n--- ДОБАВЛЕНИЕ НОВОЙ ПРИВЫЧКИ ---")
    name = input("Название привычки: ").strip()
    if not name:
        print("Название привычки не может быть пустым!")
        return
    description = input("Описание (необязательно): ").strip()
    habits = load_habits()
    for habit in habits:
        if habit['name'].lower() == name.lower():
            print(f"Привычка '{name}' уже существует!")
            return
    new_habit = {
        'id': len(habits) + 1,
        'name': name,
        'description': description if description else "",
        'completed_days': [],
        'created_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    habits.append(new_habit)
    save_habits(habits)
    print(f"Привычка '{name}' успешно добавлена!")
def list_habits():
    print("\n--- ВАШИ ПРИВЫЧКИ ---")
    habits = load_habits()
    if not habits:
        print("Нет привычек. Добавьте первую через пункт 1!")
        return
    print(f"\nВсего привычек: {len(habits)}\n")
    for habit in habits:
        print(f"[{habit['id']}] {habit['name']}")
        if habit['description']:
            print(f"{habit['description']}")
        today = datetime.now().strftime("%Y-%m-%d")
        if today in habit['completed_days']:
            print(f"ВЫПОЛНЕНО СЕГОДНЯ!")
        completed_count = len(habit['completed_days'])
        print(f"Выполнено: {completed_count} раз")
        print(f"Создана: {habit['created_at']}")
        print()
def complete_habit():
    print("\n--- ОТМЕТКА ВЫПОЛНЕНИЯ ПРИВЫЧКИ ---")
    habits = load_habits()
    if not habits:
        print("Нет привычек! Сначала добавьте хотя бы одну.")
        return
    print("\nВыберите привычку для отметки:")
    for habit in habits:
        print(f"  [{habit['id']}] {habit['name']}")
    try:
        choice = int(input("\nВведите ID привычки: "))
        selected_habit = None
        for habit in habits:
            if habit['id'] == choice:
                selected_habit = habit
                break
        if not selected_habit:
            print("Неверный ID привычки!")
            return
        today = datetime.now().strftime("%Y-%m-%d")
        if today in selected_habit['completed_days']:
            print(f"Привычка '{selected_habit['name']}' уже отмечена сегодня!")
            return
        selected_habit['completed_days'].append(today)
        save_habits(habits)
        print(f"Отлично! '{selected_habit['name']}' выполнена сегодня!")
        print(f"Всего выполнений: {len(selected_habit['completed_days'])}")
    except ValueError:
        print("Пожалуйста, введите число!")
def show_stats():
    print("\n   СТАТИСТИКА")
    habits = load_habits()
    if not habits:
        print("Нет привычек. Добавьте несколько, чтобы увидеть статистику!")
        return
    total_habits = len(habits)
    total_completions = sum(len(h['completed_days']) for h in habits)
    avg_completions = total_completions / total_habits if total_habits > 0 else 0
    print(f"\n ОБЩАЯ СТАТИСТИКА:")
    print(f"   Всего привычек: {total_habits}")
    print(f"   Всего выполнений: {total_completions}")
    print(f"   Среднее выполнений на привычку: {avg_completions:.1f}")
    if total_completions > 0:
        best_habit = max(habits, key=lambda x: len(x['completed_days']))
        print(f"\n САМАЯ ВЫПОЛНЯЕМАЯ ПРИВЫЧКА:")
        print(f"   {best_habit['name']} - {len(best_habit['completed_days'])} выполнений")
    print(f"\n ПОСЛЕДНИЕ 7 ДНЕЙ:")
    today = datetime.now()
    for i in range(7):
        date = (today - timedelta(days=i)).strftime("%Y-%m-%d")
        completions_on_date = sum(1 for h in habits if date in h['completed_days'])
        bar = "█" * completions_on_date if completions_on_date > 0 else "░"
        print(f"   {date}: {bar} ({completions_on_date} привычек)")
    print(f"\n РЕКОМЕНДАЦИИ:")
    inactive_habits = [h for h in habits if len(h['completed_days']) == 0]
    if inactive_habits:
        print(f"Начните выполнять: {', '.join(h['name'] for h in inactive_habits)}")
    today_str = today.strftime("%Y-%m-%d")
    completed_today = [h for h in habits if today_str in h['completed_days']]
    if completed_today:
        print(f"Отличная работа сегодня! Вы выполнили {len(completed_today)} привычек")
    else:
        print(f"Сегодня вы ещё не выполнили ни одной привычки. Начните прямо сейчас!")
def main():
    while True:
        show_menu()
        choice = input("Выберите пункт (1-5): ")
        if choice == "1":
            add_habit()
        elif choice == "2":
            list_habits()
        elif choice == "3":
            complete_habit()
        elif choice == "4":
            show_stats()
        elif choice == "5":
            print("До свидания!")
            break
        else:
            print("Неверный выбор! Пожалуйста, выберите 1-5")
if __name__ == "__main__":
    main()