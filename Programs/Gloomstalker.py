import random


ac = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
      20, 21, 22]

attack_bonus = 9
damage_bonus = 4


def calculate_damage(ac: int, attack_bonus: int, damage_bonus: int) -> int:

    roll = random.randint(1, 20)
    if roll == 20:
        return 2 * random.randint(1, 8) + 2*random.randint(1, 6) + damage_bonus
    elif roll + attack_bonus >= ac:
        return random.randint(1, 8) + random.randint(1, 6) + damage_bonus
    else:
        return 0


def calculate_average_damage(ac: int, attack_bonus: int, damage_bonus: int, iterations: int) -> tuple:
    normal_damage = 0
    advantage_damage = 0
    for i in range(iterations):
        normal_damage += calculate_damage(ac, attack_bonus, damage_bonus)
        advantage_damage += max(calculate_damage(ac, attack_bonus, damage_bonus),
                                calculate_damage(ac, attack_bonus, damage_bonus))

    return normal_damage / iterations, advantage_damage / iterations


for i in ac:
    normal, advantage = calculate_average_damage(
        i, attack_bonus, damage_bonus, 1000)

    normal_with_sharpshooter, advantage_with_sharpshooter = calculate_average_damage(
        i, attack_bonus - 5, damage_bonus + 10, 1000)

    print(f"AC: {i}, Normal: {normal:.2f}, Advantage: {advantage:.2f}, Normal with Sharpshooter: {
          normal_with_sharpshooter:.2f}, Advantage with Sharpshooter: {advantage_with_sharpshooter:.2f}")
