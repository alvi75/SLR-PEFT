import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def prepare_benchmark_data():
    data = {
        "SE Task": [
            "Automated Program Repair",
            "Cloze Test",
            "Code Change",
            "Code Clone Detection",
            "Code Completion",
            "Code Generation",
            "Code Refinement", 
            "Code Review",
            "Code Search",
            "Code Summarization", 
            "Code Translation",
            "Commit Message Generation",
            "Defect Detection",
            "Defect Prediction",
            "Unit Test Generation"
        ],
        "Total_Studies": [
            5, 2, 2, 6, 3, 11, 2, 1, 3, 11, 6, 1, 2, 3, 1
        ],
        "Established_Practices": [
            4, 2, 2, 5, 3, 7, 2, 1, 3, 8, 5, 1, 2, 3, 1
        ],
        "Uses_Standard_Dataset": [
            4, 2, 1, 4, 1, 6, 2, 0, 3, 7, 4, 0, 2, 3, 0
        ]
    }
    
    df = pd.DataFrame(data)
    
    df["Both"] = df.apply(lambda row: max(0, row["Established_Practices"] + row["Uses_Standard_Dataset"] - row["Total_Studies"]), axis=1)
    df["Neither"] = df["Total_Studies"] - df["Established_Practices"] - df["Uses_Standard_Dataset"] + df["Both"]
    
    return df

benchmark_summary = prepare_benchmark_data()

# Print summary for review
print("Summary of benchmarking practices (alphabetically ordered):")
print(benchmark_summary[["SE Task", "Total_Studies", "Established_Practices", "Uses_Standard_Dataset", "Both", "Neither"]])
print("\n")

plt.figure(figsize=(16, 10))
sns.set_style("whitegrid")
ax = plt.gca()

x = np.arange(len(benchmark_summary["SE Task"]))
width = 0.6

established_only = benchmark_summary["Established_Practices"] - benchmark_summary["Both"]
dataset_only = benchmark_summary["Uses_Standard_Dataset"] - benchmark_summary["Both"]
both = benchmark_summary["Both"]
neither = benchmark_summary["Neither"]

established = ax.bar(x, established_only, width, 
                    label="Follows Established Practices", color="#1f77b4")

std_dataset = ax.bar(x, dataset_only, width, 
                    bottom=established_only, 
                    label="Uses Standard Dataset", color="#ff7f0e")

both_bar = ax.bar(x, both, width, 
                  bottom=established_only + dataset_only,
                  label="Both", color="#2ca02c")

neither_bar = ax.bar(x, neither, width, 
                     bottom=established_only + dataset_only + both,
                     label="Neither", color="#d62728")

for i, row in enumerate(benchmark_summary.itertuples()):
    if established_only[i] > 0:
        ax.text(i, established_only[i] / 2, 
                f"{int(established_only[i])}", 
                ha="center", va="center", fontsize=16, color="white")
    
    if dataset_only[i] > 0:
        ax.text(i, established_only[i] + dataset_only[i] / 2, 
                f"{int(dataset_only[i])}", 
                ha="center", va="center", fontsize=16, color="white")
    
    if both[i] > 0:
        ax.text(i, established_only[i] + dataset_only[i] + both[i] / 2, 
                f"{int(both[i])}", 
                ha="center", va="center", fontsize=16, color="white")
    
    if neither[i] > 0:
        ax.text(i, established_only[i] + dataset_only[i] + both[i] + neither[i] / 2, 
                f"{int(neither[i])}", 
                ha="center", va="center", fontsize=16, color="white")
      
plt.xlabel("SE Task", fontsize=16, fontweight="bold")
plt.ylabel("Number of Studies", fontsize=14, fontweight="bold")
plt.xticks(x, benchmark_summary["SE Task"], rotation=45, ha="right", fontsize=16)
plt.yticks(fontsize=16)
plt.legend(title="Criteria", title_fontsize=16, bbox_to_anchor=(1.05, 1), loc="upper left", fontsize=16)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig("benchmarking_practices_stacked_bar.png", dpi=300, bbox_inches="tight")
plt.show()

print("Saved visualization as 'benchmarking_practices_stacked_bar.png'.")
