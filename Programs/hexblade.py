import random


damage_bonus = 7
attack_bonus = 7

def calculate_damage(ac: int, attack_bonus: int, damage_bonus: int) -> int:

    
    roll = random.randint(1, 20)
    damage_roll_1 = random.randint(1, 6)
    damage_roll_2 = random.randint(1, 6)
    damage_roll_3 = random.randint(1, 6)
    damage_roll_4 = random.randint(1, 6)
    if damage_roll_1 in [1, 2]:
        damage_roll_1 = random.randint(1, 6)
    if damage_roll_2 in [1, 2]:
        damage_roll_2 = random.randint(1, 6)
    if damage_roll_3 in [1, 2]:
        damage_roll_3 = random.randint(1, 6)
    if damage_roll_4 in [1, 2]:
        damage_roll_4 = random.randint(1, 6)

    if roll in ([19, 20]):
        return 2 * (damage_roll_1 + damage_roll_2 + damage_roll_3 + damage_roll_4) + damage_bonus
    elif roll + attack_bonus >= ac:
        return damage_roll_1 + damage_roll_2 + damage_bonus
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


ac = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
      20, 21, 22]

for i in ac:
    normal, advantage = calculate_average_damage(
        i, attack_bonus, damage_bonus, 1000)

    normal_with_gwm, advantage_with_gwm = calculate_average_damage(
        i, attack_bonus - 5, damage_bonus + 10, 1000)

    print(f"AC: {i}, Normal: {normal:.2f}, Advantage: {advantage:.2f}, Normal with Sharpshooter: {
          normal_with_gwm:.2f}, Advantage with Sharpshooter: {advantage_with_gwm:.2f}")
