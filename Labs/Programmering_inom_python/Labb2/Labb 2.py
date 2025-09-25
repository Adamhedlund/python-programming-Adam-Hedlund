import matplotlib.pyplot as plt
import numpy as np

width, height, label = [], [], []
#Läser in txt-fil och rensar bort mellanslag och komma, sparar sen i listorna ovan.
with open(r"python-programming-Adam-Hedlund\Labs\Programmering_inom_python\Labb2\datapoints.txt") as fil:
    next(fil)
    for line in fil:
        parts = line.strip().split(",")
        if len(parts) == 3:
            width.append(float(parts[0]))
            height.append(float(parts[1]))
            label.append(float(parts[2]))
data = np.array(list(zip(width, height, label)))

test_x, test_y= [], []
#Läser in txt-fil och rensar bort mellanslag och komma, sparar sen i listorna ovan.
with open(r"python-programming-Adam-Hedlund\Labs\Programmering_inom_python\Labb2\testpoints.txt")as test:
    next(test)
    for rad in test:
        rad = rad.strip()
        if "(" in rad and ")" in rad:
            testcoordinates_text = rad.split("(")[1].split(")")[0]
            x_val , y_val = testcoordinates_text.split(",")
            test_x.append(float(x_val))
            test_y.append(float(y_val))
        
training_points = np.array(list(zip(width, height)))
pichu = data[data[:,2] == 0]
pikachu = data[data[:,2] == 1]
distances = []   
pred_labels = []
nn_idx =[]

testpoints = np.array(list(zip(test_x,test_y)))
labels_np = np.asanyarray(label)
name_map ={0: "Pichu", 1:"Pikachu"}

for q in testpoints: #Loopar genom 4 testpunkter och klassificerar testpunkternas klasser.
    d = np.linalg.norm(training_points - q, axis =1)
    j = int(np.argmin(d))
    y = int(labels_np[j])
    pred_labels.append(int(y))
    nn_idx.append(int(j))
    print(f"{q} är klassifierad som {name_map.get(y)}")

def user_input(): #Tar input med felhantering och returnerar det i en array.
    while True:
        try:
            user_input_x = float(input("Skriv in ett positivt x-värde: "))
            user_input_y = float(input("Skriv in positivt y-värde: "))
        
            if user_input_x > 0 and user_input_y > 0:
                print(f"Du angav x = {user_input_x}  och = y {user_input_y}!")
                return np.array([user_input_x, user_input_y])
            else:
                print("Båda talen måste vara större än 0, försök igen!")
        except ValueError:
            print("Du måste ange ett tal (heltal/decimaltal), försök igen!")

user_point = user_input()

#1-NN index för närmaste granne och klass.
d = np.linalg.norm(training_points - user_point, axis =1)
j = int(np.argmin(d))
y = int(labels_np[j])
pred_labels.append(int(y))
nn_idx.append(int(j))

#k-NN: tar minsta avstånden för k, räknar sen ihop antal "röster" för att klassificiera inputen.
k = min(10, len(training_points))
k_indices = np.argsort(d)[:k]
k_labels = labels_np[k_indices]
count = np.bincount(k_labels.astype(int))
y10 =np.argmax(count)
print(f"Dina koordinater: {user_point} är klassificerad som {name_map.get(y)} med 1st nn!")
print(f"Dina koordinater: {user_point} är klassificerad som {name_map.get(y10)} med 10 st nn!")    
    
plt.scatter(pichu[:,0], pichu[:,1], label="Pichu", color="blue")
plt.scatter(pikachu[:,0], pikachu[:,1], label="Pickachu", color="yellow")
plt.scatter(test_x, test_y, label="Testpunkter", color="red")
plt.scatter(user_point[0], user_point[1], label=f"{user_point}={name_map.get(y)} med 1st nn", marker="*", color="green")
plt.scatter(user_point[0], user_point[1],label=f"{user_point}={name_map.get(y10)} med 10st nn", marker="*", color="green")
plt.xlabel("Width (cm)")
plt.ylabel("Height (cm)")
plt.title("Pichu vs Pikachu")
plt.legend()
plt.grid(True)
plt.show()
