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
<<<<<<< HEAD
=======
    from storage import save_habits
>>>>>>> feature/list_habits
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
<<<<<<< HEAD
=======
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
        completed_count = len(habit['completed_days'])
        print(f"Выполнено: {completed_count} раз")
        print(f"Создана: {habit['created_at']}")
        print()
>>>>>>> feature/list_habits
def main():
    while True:
        show_menu()
        choice = input("Выберите пункт (1-5): ")
        if choice == "1":
            add_habit()
<<<<<<< HEAD
=======
        elif choice == "2":
            list_habits()
>>>>>>> feature/list_habits
        elif choice == "5":
            print("До свидания!")
            break
        else:
            print(f"\n[Функция {choice} - будет добавлена позже]")
if __name__ == "__main__":
    main()