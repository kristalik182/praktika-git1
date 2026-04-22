from storage import load_habits, save_habits
from datetime import datetime
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
        print(f"   Всего выполнений: {len(selected_habit['completed_days'])}")
    except ValueError:
        print("Пожалуйста, введите число!")
def show_stats():
    print("\n--- СТАТИСТИКА ---")
    habits = load_habits()
    if not habits:
        print("Нет привычек. Добавьте первую через пункт 1!")
        return
    total_habits = len(habits)
    total_completions = sum(len(h['completed_days']) for h in habits)
    print(f"\nВсего привычек: {total_habits}")
    print(f"Всего выполнений: {total_completions}")
    if total_habits > 0:
        avg = total_completions / total_habits
        print(f"Среднее выполнений: {avg:.1f}")
    if total_completions > 0:
        best = max(habits, key=lambda x: len(x['completed_days']))
        print(f"\nЛучшая привычка: {best['name']} - {len(best['completed_days'])} выполнений")
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