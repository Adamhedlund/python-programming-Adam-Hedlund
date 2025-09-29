import random

for i in range(20):
    roll = random.randint(1,6)
    print(f"{roll}")


with open(dice_rolls.txt, "a") as f:
    f.write({roll} + ", ".join(map(str, dice_rolls))+"\n")

 