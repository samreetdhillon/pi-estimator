# Monte Carlo π Estimation

This project demonstrates a real-time Monte Carlo simulation to estimate the value of π (pi) using Python and Matplotlib.

## Overview

The simulation randomly generates points inside a unit square and determines how many fall inside a quarter circle. The ratio of points inside the circle to the total number of points is used to estimate π. The process is visualized in real-time with two plots:
- A scatter plot showing points inside and outside the quarter circle.
- A convergence plot showing how the π estimate evolves as more points are added.

## Requirements

- Python 3.x
- matplotlib

## Installation

1. Clone this repository or download the files.
2. (Optional) Create and activate a virtual environment:
    ```sh
    python -m venv simul
    source simul/Scripts/activate  # On Windows: simul\Scripts\activate
    ```
3. Install required packages:
    ```sh
    pip install matplotlib
    ```

## Usage

Run the simulation with:

```sh
python pi.py
```

You can adjust the number of points and update interval by modifying the last line in [`pi.py`](pi.py):

```python
monte_carlo_pi_realtime(50000, update_interval=50)
```

## File Structure

- [`pi.py`](pi.py): Main script running the Monte Carlo simulation and visualization.
- `simul/`: (Optional) Virtual environment directory.

## Example Output

The script will open a window showing the simulation in real-time, updating the scatter plot and convergence plot as points are generated.

---

*Created for educational purposes. Visualizes the power of Monte Carlo methods for estimating mathematical constants.*
