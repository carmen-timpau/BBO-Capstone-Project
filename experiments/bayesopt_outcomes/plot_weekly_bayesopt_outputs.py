# Plotting Weekly Bayesian Optimisation Outputs Over Whole 13-Week Period For all Black-Box Functions
# To Visualise Overall Progress Achieved in the BBO Capstone Project

import pickle
import numpy as np
import matplotlib.pyplot as plt

# Loading final dataset (initial samples + 13 weeks of BO-selected queries)
with open("final_data.pkl", "rb") as f:
    final_data = pickle.load(f)

# Building 2x4 landscape grid, 1 subplot per function
fig, axes = plt.subplots(2, 4, figsize=(22, 10))
axes = axes.flatten()

query_rounds = np.arange(1, 14)  # Weeks 1 - 13

for idx in range(8):
    fn_idx = idx + 1
    fn_key = f"function_{fn_idx}"
    ax = axes[idx]

    if fn_key not in final_data:
        ax.set_visible(False)
        continue

    y = np.array(final_data[fn_key]["y"]).flatten()
    n_dims = np.array(final_data[fn_key]["x"]).shape[1]

    weekly_outputs = y[-13:]
    baseline_outputs = y[:-13]
    baseline_best = np.max(baseline_outputs)
    incumbent_best = np.maximum.accumulate(weekly_outputs)

    def fmt(v):
        return f"{v:.2g}" if fn_idx == 1 else f"{v:.2f}"

    ax.plot(query_rounds, weekly_outputs, marker="o", linewidth=1.8,
             color="steelblue", markersize=5, label="Query Output")
    ax.step(query_rounds, incumbent_best, where="post", linestyle=":", linewidth=2.0,
             color="red", label="Incumbent Best")
    ax.axhline(baseline_best, linestyle="--", linewidth=1.5, color="gray",
               label="Initial Dataset Best")

    highest_value = max(weekly_outputs.max(), incumbent_best.max(), baseline_best)
    lowest_value = min(weekly_outputs.min(), baseline_best)
    value_range = highest_value - lowest_value
    padding = value_range * 0.15 if value_range > 0 else abs(highest_value) * 0.1 + 1e-9
    bottom_padding_factor = 0.8 if fn_idx == 1 else 0.3
    ax.set_ylim(lowest_value - padding * bottom_padding_factor, highest_value + padding)
    ax.set_xlim(query_rounds[0] - 0.8, query_rounds[-1] + 0.5)

    final_incumbent = incumbent_best[-1]
    ax.annotate(fmt(final_incumbent),
                xy=(query_rounds[-1], final_incumbent),
                xytext=(0, 8), textcoords="offset points",
                ha="center", fontsize=10, color="red", fontweight="bold")

    grey_x = query_rounds[0] - 0.5
    ax.annotate(fmt(baseline_best),
                xy=(grey_x, baseline_best),
                xytext=(0, 6), textcoords="offset points",
                ha="left", va="bottom", fontsize=10, color="gray", fontweight="bold")

    first_query_value = weekly_outputs[0]
    blue_y_offset = -18 if fn_idx == 5 else -10
    ax.annotate(fmt(first_query_value),
                xy=(grey_x, first_query_value),
                xytext=(0, blue_y_offset), textcoords="offset points",
                ha="left", va="top", fontsize=10, color="steelblue", fontweight="bold")

    ax.set_title(f"Function {fn_idx} ({n_dims}D)", fontsize=14, fontweight="bold")
    ax.set_xlabel("Query Round", fontsize=12)
    ax.set_ylabel("Function Output", fontsize=12)
    ax.set_xticks(query_rounds)
    ax.grid(True, linestyle="--", alpha=0.4)
    ax.legend(loc="best", fontsize=9)

plt.suptitle("Weekly Bayesian Optimization Query Outputs Across Functions 1-8 (13 Rounds)",
             fontsize=17, fontweight="bold", y=0.98)
plt.tight_layout(rect=[0, 0, 1, 0.96])

plt.savefig("bayesopt_weekly_outputs_plot.png", dpi=300, bbox_inches="tight")
print("Saved to 'bayesopt_weekly_outputs_plot.png'")
plt.show()
