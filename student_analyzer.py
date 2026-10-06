import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("students.csv")

print("===== STUDENT PERFORMANCE ANALYZER =====")
print(data)

print("\n===== SUBJECT AVERAGES =====")

print("Average Maths:", data["Maths"].mean())
print("Average Physics:", data["Physics"].mean())
print("Average Programming:", data["Programming"].mean())

print("\n===== TOP STUDENT OVERALL =====")

data["Average"] = data[["Maths", "Physics", "Programming"]].mean(axis=1)

top_student = data.loc[data["Average"].idxmax()]

print("Top student:", top_student["Name"])
print("Average marks:", round(top_student["Average"], 2))

print("\n===== TOPPER IN EACH SUBJECT =====")

print("Maths:", data.loc[data["Maths"].idxmax(), "Name"])
print("Physics:", data.loc[data["Physics"].idxmax(), "Name"])
print("Programming:", data.loc[data["Programming"].idxmax(), "Name"])

print("\n===== CREATING GRAPH =====")

plt.bar(data["Name"], data["Average"])

plt.title("Student Average Marks")
plt.xlabel("Students")
plt.ylabel("Average Marks")

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()