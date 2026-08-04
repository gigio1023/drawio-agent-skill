"""Two reference charts in the editorial language. Doubles as the smoke test.

Run from this skill's scripts/ directory (or anywhere, paths are cwd-relative):

    uv run --with matplotlib python example_chart.py

Outputs example_line.{svg,png} and example_bars.{svg,png} in the cwd.
"""

import math

import matplotlib.pyplot as plt
import editorial_mpl as ed

ed.use()

# --- Line chart: log x, one solid + one dashed series, endpoint labels ---
fig, ax = plt.subplots(figsize=(8.3, 6.2))
fig.subplots_adjust(left=0.11, right=0.88, top=0.80, bottom=0.12)

steps = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 400]
main = [42 / (1 + math.exp(-(math.log(s) - 3.1) / 0.75)) for s in steps]
ref = [24 / (1 + math.exp(-(math.log(s) - 3.4) / 0.8)) for s in steps]

ax.plot(steps, main, color=ed.BLUE["mid"], solid_capstyle="round")
ax.plot(steps, ref, color=ed.CORAL["mid"], dashes=(4, 4))

ax.set_xscale("log")
ax.set_xlim(1, 400)
ax.set_ylim(0, 45)
ax.set_xticks([1, 10, 100, 400])
ax.set_xticklabels(["1", "10", "100", "400"])

ed.direct_label(ax, steps[-1], main[-1], f"{main[-1]:.1f}%", ed.BLUE["mid"], dx=8)
ed.direct_label(ax, steps[-1], ref[-1], f"{ref[-1]:.1f}%", ed.CORAL["text"], dx=8)

ed.mono_ticks(ax)
ed.axis_label(ax, "Max steps allowed", "Success rate (%)")
ed.header(fig, "Success rate scales with agent budget",
          [("Tuned harness", ed.BLUE["chip"], ed.BLUE["deep"]),
           ("Baseline", ed.CORAL["chip"], ed.CORAL["deep"])])
ed.save(fig, "example_line")
plt.close(fig)

# --- Grouped bars: light fill + ink stroke, mono value labels ---
fig, ax = plt.subplots(figsize=(8.3, 6.2))
fig.subplots_adjust(left=0.11, right=0.95, top=0.80, bottom=0.12)

benchmarks = ["SUITE A", "SUITE B", "SUITE C"]
model_a = [74.9, 88.1, 94.6]
model_b = [69.1, 83.3, 88.9]
x = range(len(benchmarks))
w = 0.34

bars_a = ax.bar([i - w / 2 - 0.015 for i in x], model_a, w,
                facecolor=ed.BLUE["chip"], edgecolor=ed.INK, linewidth=1.2)
bars_b = ax.bar([i + w / 2 + 0.015 for i in x], model_b, w,
                facecolor=ed.BLUE["light"], edgecolor=ed.INK, linewidth=1.2)

for bars in (bars_a, bars_b):
    for b in bars:
        ax.annotate(f"{b.get_height():.1f}",
                    (b.get_x() + b.get_width() / 2, b.get_height()),
                    xytext=(0, 6), textcoords="offset points", ha="center",
                    fontfamily=ed.MONO, fontsize=11.5, color=ed.INK)

ax.set_xticks(list(x))
ax.set_xticklabels(benchmarks)
ax.set_ylim(0, 100)
ax.set_yticks([0, 25, 50, 75, 100])
ax.spines["left"].set_visible(False)
ax.tick_params(axis="both", length=0)
ed.mono_ticks(ax)
ed.axis_label(ax, None, "Accuracy (%)")
ed.header(fig, "Benchmark accuracy by model",
          [("Model A", ed.BLUE["chip"], ed.BLUE["deep"]),
           ("Model B", ed.BLUE["light"], ed.INK)])
ed.save(fig, "example_bars")
plt.close(fig)

print("wrote example_line.{svg,png}, example_bars.{svg,png}")
