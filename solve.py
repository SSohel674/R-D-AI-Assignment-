import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import differential_evolution
from scipy.spatial import cKDTree
from pathlib import Path


# ==========================================
# 1. LOAD CSV DATA
# ==========================================

# Get the folder where solve.py is located
BASE_DIR = Path(__file__).resolve().parent

# Build the CSV path
csv_path = BASE_DIR / "xy_data.csv"

data = pd.read_csv(csv_path)

x_data = data["x"].values
y_data = data["y"].values

given_points = np.column_stack((x_data, y_data))

print("Number of data points:", len(given_points))


# ==========================================
# 2. PARAMETRIC CURVE
# ==========================================

def generate_curve(params, n_points=5000):

    theta, M, X = params

    # Convert theta from degrees to radians
    theta = np.radians(theta)

    # Assignment specifies 6 < t < 60
    t = np.linspace(6, 60, n_points)

    exp_term = np.exp(M * np.abs(t))
    sin_term = np.sin(0.3 * t)

    x = (
        t * np.cos(theta)
        - exp_term * sin_term * np.sin(theta)
        + X
    )

    y = (
        42
        + t * np.sin(theta)
        + exp_term * sin_term * np.cos(theta)
    )

    return np.column_stack((x, y))


# ==========================================
# 3. L1 DISTANCE
# ==========================================

def objective(params):

    predicted_points = generate_curve(params)

    # Create KDTree for predicted curve
    tree = cKDTree(predicted_points)

    # Find nearest predicted point
    distances, _ = tree.query(
        given_points,
        k=1,
        p=1
    )

    # Mean L1 distance
    return np.mean(distances)


# ==========================================
# 4. UNKNOWN PARAMETER RANGES
# ==========================================

bounds = [
    (0, 50),        # theta
    (-0.05, 0.05),  # M
    (0, 100)        # X
]


# ==========================================
# 5. OPTIMIZATION
# ==========================================

print("\nStarting optimization...")
print("Please wait...\n")

result = differential_evolution(
    objective,
    bounds,
    seed=42,
    maxiter=100,
    popsize=15,
    tol=1e-8,
    polish=True
)


# ==========================================
# 6. RESULTS
# ==========================================

theta, M, X = result.x

print("===================================")
print("       FINAL RESULTS")
print("===================================")

print(f"Theta = {theta:.8f} degrees")
print(f"M     = {M:.8f}")
print(f"X     = {X:.8f}")

print("-----------------------------------")
print(f"L1 Error = {result.fun:.10f}")
print("===================================")


# ==========================================
# 7. GENERATE FINAL CURVE
# ==========================================

final_curve = generate_curve(
    [theta, M, X],
    n_points=10000
)


# ==========================================
# 8. PLOT
# ==========================================

plt.figure(figsize=(10, 6))

plt.scatter(
    x_data,
    y_data,
    s=8,
    label="Given CSV Data"
)

plt.plot(
    final_curve[:, 0],
    final_curve[:, 1],
    linewidth=2,
    color="red",
    label="Fitted Parametric Curve"
)

plt.xlabel("X")
plt.ylabel("Y")

plt.title("Parametric Curve Fitting")

plt.legend()
plt.grid(True)

plt.tight_layout()


# Save image in the same folder as solve.py
output_path = BASE_DIR / "fitted_curve.png"

plt.savefig(
    output_path,
    dpi=300
)

plt.show()