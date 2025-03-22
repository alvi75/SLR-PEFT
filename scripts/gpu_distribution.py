import pandas as pd
import matplotlib.pyplot as plt
import os

input_csv = "../data/peft_se_benchmark_metadata.csv"
df = pd.read_csv(input_csv, encoding="iso-8859-1")

columns_needed = ["SE Task", "Hardware Details"]
df = df[columns_needed].dropna()

gpu_models = ["A100", "RTX 3090", "V100", "RTX 3090Ti", "GTX 3090", "L40S"]

gpu_usage = {task: {gpu: 0 for gpu in gpu_models} for task in df["SE Task"].unique()}

for _, row in df.iterrows():
    task = row["SE Task"]
    hardware_info = str(row["Hardware Details"])
    for gpu in gpu_models:
        if gpu in hardware_info:
            gpu_usage[task][gpu] += 1

gpu_df = pd.DataFrame.from_dict(gpu_usage, orient="index")

gpu_df = gpu_df.sort_index()
gpu_df = gpu_df[gpu_models] 

output_folder = "peft_analysis_outputs_rq3a"
os.makedirs(output_folder, exist_ok=True)

plt.style.use("seaborn-v0_8")
plt.figure(figsize=(12, 8))

ax = gpu_df.plot(kind="bar", stacked=True, colormap="viridis", edgecolor="black", linewidth=0.7)

plt.xlabel("SE Task", fontsize=12, fontweight="bold")
plt.ylabel("Count of Studies Using Each GPU", fontsize=12, fontweight="bold")

plt.xticks(rotation=45, ha="right", fontsize=12)
plt.yticks(fontsize=12)

plt.legend(title="GPU Model", fontsize=12, title_fontsize=14, bbox_to_anchor=(1.05, 1), loc="upper left")

for p in ax.patches:
    width, height = p.get_width(), p.get_height()
    if height > 0:
        x, y = p.get_xy()
        ax.annotate(f"{int(height)}", (x + width / 2, y + height / 2), ha="center", va="center", fontsize=10, color="white")

plt.tight_layout()

output_file = os.path.join(output_folder, "gpu_hardware_distribution.png")
plt.savefig(output_file, dpi=300, bbox_inches="tight")

print(f"Visualization saved as {output_file}")
