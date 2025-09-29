import random

dice_counts = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}


for _ in range(1000000):
    roll = random.randint(1,6)
    dice_counts[roll] += 1

for face, count in dice_counts.items():
    print(face, count)
        