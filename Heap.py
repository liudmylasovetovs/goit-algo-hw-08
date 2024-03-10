import heapq


def minimize_cable_costs(cables):
    # Ініціалізуємо купу
    heapq.heapify(cables)

    total_costs = 0

    while len(cables) > 1:
        # Беремо два найменших кабелі
        cable1 = heapq.heappop(cables)
        cable2 = heapq.heappop(cables)

        # Об'єднуємо їх та додаємо суму назад до купи
        merged_cable = cable1 + cable2
        total_costs += merged_cable
        heapq.heappush(cables, merged_cable)

    return total_costs


# Приклад використання
network_cables = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = minimize_cable_costs(network_cables)
print("Мінімальні витрати на об'єднання кабелів:", result)
