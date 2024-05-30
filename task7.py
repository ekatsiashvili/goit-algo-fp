import random
import matplotlib.pyplot as plt

# Встановлюємо кількість симуляцій
num_simulations = 1000000

# Список для зберігання сум
sums = []

# Симулюємо кидки двох кубиків
for _ in range(num_simulations):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    sums.append(dice1 + dice2)

# Підрахунок частоти кожної суми
sum_counts = {i: 0 for i in range(2, 13)}
for sum_ in sums:
    sum_counts[sum_] += 1

# Обчислюємо імовірності
sum_probabilities = {k: v / num_simulations for k, v in sum_counts.items()}

# Теоретичні імовірності для порівняння
theoretical_probabilities = {
    2: 1/36, 3: 2/36, 4: 3/36, 5: 4/36, 6: 5/36, 7: 6/36,
    8: 5/36, 9: 4/36, 10: 3/36, 11: 2/36, 12: 1/36
}

# Виводимо результати у вигляді таблиці
print(f"{'Сума':<10}{'Імовірність (Монте-Карло)':<25}{'Імовірність (Теоретична)':<25}")
for sum_ in range(2, 13):
    print(f"{sum_:<10}{sum_probabilities[sum_]:<25.5f}{theoretical_probabilities[sum_]:<25.5f}")

# Візуалізація
sums_sorted = sorted(sum_probabilities.keys())
mc_probs = [sum_probabilities[sum_] for sum_ in sums_sorted]
theoretical_probs = [theoretical_probabilities[sum_] for sum_ in sums_sorted]

plt.figure(figsize=(10, 6))
plt.plot(sums_sorted, mc_probs, label="Монте-Карло", marker='o')
plt.plot(sums_sorted, theoretical_probs, label="Теоретичні", marker='x')
plt.xlabel("Сума")
plt.ylabel("Імовірність")
plt.title("Імовірності сум при киданні двох кубиків")
plt.legend()
plt.grid(True)
plt.show()
