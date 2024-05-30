items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

def greedy_algorithm(items, budget):
    # Сортування предметів за спаданням співвідношення калорій до вартості
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    
    total_cost = 0
    total_calories = 0
    selected_items = []

    for item, details in sorted_items:
        if total_cost + details['cost'] <= budget:
            selected_items.append(item)
            total_cost += details['cost']
            total_calories += details['calories']

    return selected_items, total_cost, total_calories

def dynamic_programming(items, budget):
    n = len(items)
    item_names = list(items.keys())
    costs = [items[name]['cost'] for name in item_names]
    calories = [items[name]['calories'] for name in item_names]

    # Ініціалізація таблиці DP
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

    # Заповнення таблиці DP
    for i in range(1, n + 1):
        for w in range(1, budget + 1):
            if costs[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - costs[i - 1]] + calories[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    # Визначення обраних предметів
    selected_items = []
    w = budget
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(item_names[i - 1])
            w -= costs[i - 1]

    total_calories = dp[n][budget]
    total_cost = sum(items[item]['cost'] for item in selected_items)

    return selected_items, total_cost, total_calories

# Test
budget = 100

print("Жадібний алгоритм:")
selected_items_greedy, total_cost_greedy, total_calories_greedy = greedy_algorithm(items, budget)
print("Обрані предмети:", selected_items_greedy)
print("Загальна вартість:", total_cost_greedy)
print("Загальна калорійність:", total_calories_greedy)

print("\nДинамічне програмування:")
selected_items_dp, total_cost_dp, total_calories_dp = dynamic_programming(items, budget)
print("Обрані предмети:", selected_items_dp)
print("Загальна вартість:", total_cost_dp)
print("Загальна калорійність:", total_calories_dp)
