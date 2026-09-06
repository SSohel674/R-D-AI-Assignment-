# R&D / AI Parametric Curve Assignment

## 1. Problem Statement

The objective is to find the unknown parameters **theta (θ), M, and X** from a given set of points belonging to a parametric curve.

The parametric equations are:

```text
x = t*cos(theta) - exp(M*|t|)*sin(0.3t)*sin(theta) + X

y = 42 + t*sin(theta) + exp(M*|t|)*sin(0.3t)*cos(theta)
```

Parameter ranges:

- 0 < theta < 50 degrees
- -0.05 < M < 0.05
- 0 < X < 100
- 6 < t < 60

## 2. Dataset

The provided `xy_data.csv` file contains the points that lie on the required curve.

The CSV file contains two columns:

- `x` - X-coordinate of the data point
- `y` - Y-coordinate of the data point

The dataset is loaded using Pandas.

## 3. Approach

The following steps are used:

1. Load the CSV data using Pandas.
2. Extract the `x` and `y` coordinates.
3. Combine the coordinates into `(x, y)` points.
4. Generate points from the given parametric equations.
5. Compare the generated curve with the given data points.
6. Calculate the nearest-point L1 distance.
7. Use numerical optimization to find the values of theta, M, and X that minimize the L1 distance.
8. Generate the final fitted curve using the optimized parameters.
9. Plot the original data points and the fitted curve.
10. Save the fitted curve as `fitted_curve.png`.

## 4. Optimization

The `differential_evolution` optimization method from SciPy is used.

The search is performed within the specified parameter ranges:

| Parameter | Range |
|---|---|
| Theta | 0 to 50 degrees |
| M | -0.05 to 0.05 |
| X | 0 to 100 |

The objective function minimizes the mean **L1 distance** between the supplied data points and the generated parametric curve.

`cKDTree` from SciPy is used to efficiently find the nearest point on the generated curve.

Optimization settings:

- Maximum iterations: 100
- Population size: 15
- Tolerance: 1e-8
- Seed: 42
- Polish: True

## 5. Results

The estimated parameters are:

- **Theta = 30°**
- **M = 0.03**
- **X = 55**

The optimization produced an L1 error of approximately:

**0.0040733**

The low L1 error indicates that the fitted curve closely matches the given data points.

## 6. Final Parametric Equation

Using the estimated parameters:

**Theta = 30°**

**M = 0.03**

**X = 55**

The final equations are:

```text
x = t*cos(30°) - exp(0.03*|t|)*sin(0.3t)*sin(30°) + 55

y = 42 + t*sin(30°) + exp(0.03*|t|)*sin(0.3t)*cos(30°)
```

where:

```text
6 < t < 60
```

## 7. Result Visualization

The generated plot compares the original points from `xy_data.csv` with the fitted parametric curve.

![Fitted Curve](fitted_curve.png)

## 8. Project Files

- `xy_data.csv` - Input dataset
- `solve.py` - Python implementation
- `fitted_curve.png` - Generated fitted curve
- `README.md` - Project documentation
- `requirements.txt` - Required dependencies

## 9. Technologies Used

- Python
- NumPy
- Pandas
- SciPy
- Matplotlib

## 10. How to Run

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Run the program:

```bash
python solve.py
```

The program will load the dataset, optimize the parameters, calculate the L1 error, generate the fitted curve, and save the visualization as `fitted_curve.png`.

## 11. Conclusion

The unknown parameters of the given parametric curve were estimated using numerical optimization.

The final estimated values are:

- **Theta = 30°**
- **M = 0.03**
- **X = 55**

The fitted curve closely matches the points provided in the dataset, with an approximate **L1 error of 0.0040733**.
