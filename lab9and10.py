import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tkinter as tk
from tkinter import ttk


def show_dataframe_in_window(df):
    root = tk.Tk()
    root.title("Election Data Table")

    tree = ttk.Treeview(root)
    tree["columns"] = list(df.columns)
    tree["show"] = "headings"

    for column in df.columns:
        tree.heading(column, text=column)
        tree.column(column, anchor="center", width=120)

    for _, row in df.iterrows():
        tree.insert("", "end", values=list(row))

    tree.pack(expand=True, fill="both")

    root.mainloop()    

data = [
    {"State": "Madhya Pradesh", "Party": "BJP", "Seats_Won": 163, "Total_Seats": 230, "Voter_Turnout (%)": 72.1},
    {"State": "Madhya Pradesh", "Party": "INC", "Seats_Won": 66, "Total_Seats": 230, "Voter_Turnout (%)": 72.1},
    {"State": "Madhya Pradesh", "Party": "BSP", "Seats_Won": 0, "Total_Seats": 230, "Voter_Turnout (%)": 72.1},
    {"State": "Madhya Pradesh", "Party": "Others", "Seats_Won": 1, "Total_Seats": 230, "Voter_Turnout (%)": 72.1},
    {"State": "Rajasthan", "Party": "BJP", "Seats_Won": 115, "Total_Seats": 200, "Voter_Turnout (%)": 74.2},
    {"State": "Rajasthan", "Party": "INC", "Seats_Won": 69, "Total_Seats": 200, "Voter_Turnout (%)": 74.2},
    {"State": "Rajasthan", "Party": "BSP", "Seats_Won": 2, "Total_Seats": 200, "Voter_Turnout (%)": 74.2},
    {"State": "Rajasthan", "Party": "Others", "Seats_Won": 13, "Total_Seats": 200, "Voter_Turnout (%)": 74.2},
]

file_name = 'election_data.csv'

#question 1> Check if the file `election_data.csv` exists in the directory. If not, create the file and 
# write the election data into it. Handle file-related exceptions gracefully.
if not os.path.exists(file_name):
    try:
        df = pd.DataFrame(data)
        df.to_csv(file_name, index=False)
        print(f"{file_name} created and data written successfully.")
    except Exception as e:
        print(f"Error writing to file: {e}")
else:
    print(f"{file_name} already exists.")

#question 2> Read the data into a Pandas DataFrame and calculate the percentage of seats won by each party. 
# Add this as a new column named Seats_Percentage.
try:
    df = pd.read_csv(file_name)
except Exception as e:
    print(f"Error reading the file: {e}")
    df = pd.DataFrame()

try:
    df["Seats_Percentage"] = (df["Seats_Won"] / df["Total_Seats"]) * 100
    print("Seats_Percentage is added ")
    show_dataframe_in_window(df)
except Exception as e:
    print(f"Error calculating Seats_Percentage: {e}")

# question 3> Determine the party with the highest number of seats in each state and display their names.
try:
    highest_seats = df.loc[df.groupby("State")["Seats_Won"].idxmax()]
    print("Party with the highest seats in each state:")
    print(highest_seats[["State", "Party", "Seats_Won"]])
except Exception as e:
    print(f"Error determining party with highest seats: {e}")

# question 4>Create a bar chart showing the number of seats won by each party in each state using Matplotlib or Seaborn.
try:
    plt.figure(figsize=(10, 6))
    sns.barplot(x="State", y="Seats_Won", hue="Party", data=df)
    plt.title("Seats Won by Each Party in Each State")
    plt.ylabel("Seats Won")
    plt.xlabel("State")
    plt.legend(title="Party")
    plt.tight_layout()
    plt.show()
except Exception as e:
    print(f"Error creating the bar chart: {e}")



