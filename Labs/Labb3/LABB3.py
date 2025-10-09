import matplotlib.pyplot as plt
import numpy as np
import os
import csv

here = os.path.dirname(os.path.abspath(__file__))
csv.path = os.path.join(here, "unlabelled_data.csv")

x = []
y = []
label = []

with open(csv.path, newline="") as f:
    reader = csv.reader(f, delimiter=",")
    for row in reader:
        x.append(float(row[0]))
        y.append(float(row[1]))
  
def classify(x, y, k, m):
    distance = y - (k * x + m)
    return np.where(distance < 0,0,1)

label_y = np.array(label)
x = np.array(x)
y = np.array(y)

def compare(label_original, label_new):
    diff = label_original != label_new
    count = np.sum(diff)
    diff_percent = 100 * count /len(label_original)
    return float(diff_percent)

label_y = classify(x,y, -1, 0)
label_f = classify(x,y, -0.489, 0)
label_g = classify(x,y, -2, 0.16)
label_h = classify(x,y, 800, -120)

diff_percent_f = compare(label_y, label_f)
diff_percent_g = compare(label_y, label_g)
diff_percent_h = compare(label_y, label_h)

with open("labelled_data.csv", "w") as outfile:
    writer = csv.writer(outfile, delimiter=",")
    writer.writerow(["x", "y", "label"])

    for xi, yi, li in zip(x, y, label_y):
        writer.writerow([xi, yi, li])

x_under = x[label_y == 0]
y_under = y[label_y == 0]

x_over = x[label_y == 1]
y_over = y[label_y == 1]

x_point = [-6,6]
y_point = [6,-6]

x_val = np.linspace(-6,6,200)
f = (-0.489 * x_val)
g = (-2 * x_val + 0.16)
h = (800 * x_val - 120)

def plot_data_punkter(x_over,y_over,x_under,y_under,x_point,y_point):
    plt.title("Data punkter")
    plt.scatter(x_over,y_over,color="red", label="klass 1")
    plt.scatter(x_under, y_under, color="blue", label="Klass 0")
    plt.plot(x_point, y_point, label="Y=-X", color="black")
    plt.axhline(0, color="black", linewidth=0.8)
    plt.axvline(0, color="black", linewidth=0.8)
    plt.xlim(-6,6)
    plt.ylim(-6,6)
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend(loc="lower right")
    plt.show()

def plot_classification_results(x,y,x_point,y_point,x_val,f,g,h,diff_percent_f,diff_percent_g,diff_percent_h):
    fig, axes = plt.subplots(1,2,figsize=(10,4))

    axes[0].scatter(x,y, color="orange", label="datapunkter")
    axes[0].plot(x_point, y_point, color="black", label="Y=-X")
    axes[0].plot(x_val,f, color="green", label="f(x)=-0.489x")
    axes[0].plot(x_val,g, color="purple", label="g(x)=-2x+ 0.16")
    axes[0].plot(x_val,h, color="red", label="h(x)=800x-120")
    axes[0].set_title("Datapunkter med flera funktioner")
    axes[0].grid(True, linestyle="--", alpha=0.6)
    axes[0].axhline(0, color="black", linewidth=0.8)
    axes[0].axvline(0, color="black", linewidth=0.8)
    axes[0].set_xlim(-6,6)
    axes[0].set_ylim(-6,6)
    axes[0].legend(loc="lower right")
    labels=["f(x)", "g(x)", "h(x)"]
    difference = [diff_percent_f, diff_percent_g, diff_percent_h]
    axes[1].bar(labels, difference)
    axes[1].set_title("Antal procent felklassificering mot funktion: y=-x")
    axes[1].set_xlabel("Funktioner")
    axes[1].set_ylabel("Antal % fel")
    for i, val in enumerate(difference):
        axes[1].text(i,val + 0.5, f"{val:.3f}%", ha="center", va="bottom",
                        fontsize=10, fontweight="bold")
        
    plt.show()
