"""
Visualizer Module
Generates high-dimensional scatter plots (3D up to 8D) for functions 1 through 8.
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines

def plot_function_1(data: dict):
    fig = plt.figure(figsize=(20, 15))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(data["function_1"]["x"][:, 0], data["function_1"]["x"][:, 1], data["function_1"]["y"], s=80)
    ax.tick_params(labelsize=10)
    ax.set_title('3D Scatter Plot of Function 1 Initial Data Points', size=20)
    ax.set_xlabel(r"$x_1$", size=15)
    ax.set_ylabel(r"$x_2$", size=15)
    ax.set_zlabel("y", size=15)
    plt.show()

def plot_function_2(data: dict):
    fig = plt.figure(figsize=(20, 15))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(data["function_2"]["x"][:, 0], data["function_2"]["x"][:, 1], data["function_2"]["y"], s=80)
    ax.tick_params(labelsize=10)
    ax.set_title('3D Scatter Plot of Function 2 Initial Data Points', size=20)
    ax.set_xlabel(r"$x_1$", size=15)
    ax.set_ylabel(r"$x_2$", size=15)
    ax.set_zlabel("y", size=15)
    plt.show()

def plot_function_3(data: dict):
    fig = plt.figure(figsize=(20, 15))
    ax = fig.add_subplot(111, projection='3d')
    f3p = ax.scatter(
        data["function_3"]["x"][:, 0],
        data["function_3"]["x"][:, 1],
        data["function_3"]["x"][:, 2],
        c=data["function_3"]["y"], cmap='viridis', s=80
    )
    ax.tick_params(labelsize=15)
    ax.set_title('4D Scatter Plot of Function 3 Initial Data Points \n (3D Inputs + Colour Mapped Output)', size=20)
    ax.set_xlabel(r"$x_1$", size=20)
    ax.set_ylabel(r"$x_2$", size=20)
    ax.set_zlabel("x3", size=20)
    cbar = plt.colorbar(f3p, shrink=0.6)
    cbar.ax.tick_params(labelsize=14)
    cbar.set_label("4th dimension (y)", fontsize=15)
    plt.show()

def plot_function_4(data: dict):
    fig = plt.figure(figsize=(20, 15))
    function4_y = data["function_4"]["y"] * (-1)
    ax = fig.add_subplot(111, projection='3d')
    f4p = ax.scatter(
        data["function_4"]["x"][:, 0],
        data["function_4"]["x"][:, 1],
        data["function_4"]["x"][:, 2],
        c=data["function_4"]["x"][:, 3],
        s=function4_y * 80, cmap='viridis'
    )
    ax.tick_params(labelsize=15)
    vmax = np.max(np.abs(data["function_4"]["x"][:, 3]))
    f4p.set_clim(-vmax, vmax)
    ax.set_title('5D Scatter Plot of Function 4 Initial Data Points \n (3D Position + Colour + Size Encoding)', size=20)
    ax.set_xlabel(r"$x_1$", size=20)
    ax.set_ylabel(r"$x_2$", size=20)
    ax.set_zlabel("x3", size=20)
    cbar = plt.colorbar(f4p, shrink=0.6)
    cbar.ax.tick_params(labelsize=14)
    cbar.set_label("4th dimension (x4)", fontsize=15)
    
    f4_min_max_y_vals = [min(function4_y), np.median(function4_y), max(function4_y)]
    sizes = [v * 80 for v in f4_min_max_y_vals]
    handles = [mlines.Line2D([], [], color='black', alpha=0.5, marker='o', linestyle='None', markersize=np.sqrt(s), label=f"{v:.2f}") for v, s in zip(f4_min_max_y_vals, sizes)]
    legend = ax.legend(handles=handles, title="Size scale (y)", loc="upper left", fontsize=15, labelspacing=3.0, handletextpad=2.0, handlelength=0.5)
    legend.get_title().set_fontsize(15)
    legend._legend_title_box._text.set_va("top")
    plt.show()

def plot_function_5(data: dict):
    fig = plt.figure(figsize=(20, 15))
    ax = fig.add_subplot(111, projection='3d')
    f5p = ax.scatter(
        data["function_5"]["x"][:, 0],
        data["function_5"]["x"][:, 1],
        data["function_5"]["x"][:, 2],
        c=data["function_5"]["x"][:, 3],
        s=data["function_5"]["y"] * 20, cmap='viridis'
    )
    ax.tick_params(labelsize=15)
    vmax = np.max(np.abs(data["function_5"]["x"][:, 3]))
    f5p.set_clim(-vmax, vmax)
    ax.set_title('5D Scatter Plot of Function 5 Initial Data Points \n (3D Position + Colour + Size Encoding)', size=20)
    ax.set_xlabel(r"$x_1$", size=20)
    ax.set_ylabel(r"$x_2$", size=20)
    ax.set_zlabel("x3", size=20)
    cbar = plt.colorbar(f5p, shrink=0.6)
    cbar.ax.tick_params(labelsize=14)
    cbar.set_label("4th dimension (x4)", fontsize=15)
    
    f5_min_max_y_vals = sorted([min(data["function_5"]["y"]), np.median(data["function_5"]["y"]), max(data["function_5"]["y"])], reverse=True)
    sizes = [v * 20 for v in f5_min_max_y_vals]
    handles = [mlines.Line2D([], [], color='black', alpha=0.5, marker='o', linestyle='None', markersize=np.sqrt(s), label=f"{v:.2f}") for v, s in zip(f5_min_max_y_vals, sizes)]
    legend = ax.legend(handles=handles, title="Size scale (y)", loc="upper left", bbox_to_anchor=(-0.25, 1.0), fontsize=15, labelspacing=6.0, handletextpad=5.0, handlelength=5)
    legend.get_title().set_fontsize(15)
    legend._legend_title_box._text.set_va("top")
    plt.show()

def plot_function_6(data: dict):
    fig = plt.figure(figsize=(20, 15))
    X = data["function_6"]["x"]
    Y = data["function_6"]["y"]
    x5 = X[:, 4]
    alpha = 0.2 + 0.8 * (x5 - x5.min()) / (x5.max() - x5.min())
    size = 200 + ((Y - Y.min()) / (Y.max() - Y.min())) * 1800

    ax = fig.add_subplot(111, projection='3d')
    f6p = ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=X[:, 3], s=size, cmap='viridis', alpha=alpha)
    vmax = np.max(np.abs(X[:, 3]))
    f6p.set_clim(-vmax, vmax)
    ax.tick_params(labelsize=15)
    ax.set_title('6D Scatter Plot of Function 6 Initial Data Points\n(3D Position + Colour + Alpha + Size)', size=20)
    ax.set_xlabel(r"$x_1$", size=20)
    ax.set_ylabel(r"$x_2$", size=20)
    ax.set_zlabel("x3", size=20)
    
    cbar = plt.colorbar(f6p, shrink=0.6)
    cbar.ax.tick_params(labelsize=14)
    cbar.set_label("4th dimension (x4)", fontsize=15)
    plt.show()

def plot_function_7(data: dict):
    fig = plt.figure(figsize=(20, 15))
    ax = fig.add_subplot(111, projection='3d')
    X = data["function_7"]["x"]
    Y = data["function_7"]["y"]
    x5 = X[:, 4]
    alpha = 0.2 + 0.8 * (x5 - x5.min()) / (x5.max() - x5.min())
    size = 200 + ((Y - Y.min()) / (Y.max() - Y.min())) * 1800
    theta = ((X[:, 5] - X[:, 5].min()) / (X[:, 5].max() - X[:, 5].min())) * 180

    for i in range(len(X)):
        f7p = ax.scatter(X[i, 0], X[i, 1], X[i, 2], c=X[i, 3], s=size[i], cmap='viridis', alpha=alpha[i], marker=(4, 0, theta[i]), edgecolor='k', linewidth=0.3)
    
    vmax = np.max(np.abs(X[:, 3]))
    f7p.set_clim(-vmax, vmax)
    ax.tick_params(labelsize=15)
    ax.set_title('7D Scatter Plot of Function 7\n(3D Position + Colour + Size-from-y + Rotation-from-x6 + Alpha-from-x5)', size=20)
    ax.set_xlabel(r"$x_1$", size=20)
    ax.set_ylabel(r"$x_2$", size=20)
    ax.set_zlabel(r"$x_3$", size=20)
    
    cbar = plt.colorbar(f7p, shrink=0.6)
    cbar.ax.tick_params(labelsize=14)
    cbar.set_label("4th dimension (x4)", fontsize=15)
    plt.show()

def plot_function_8(data: dict):
    fig = plt.figure(figsize=(20, 15))
    ax = fig.add_subplot(111, projection='3d')
    X = data["function_8"]["x"]
    Y = data["function_8"]["y"]
    x5 = X[:, 4]
    alpha = 0.2 + 0.8 * (x5 - x5.min()) / (x5.max() - x5.min())
    size = 200 + ((Y - Y.min()) / (Y.max() - Y.min())) * 800
    theta = ((X[:, 5] - X[:, 5].min()) / (X[:, 5].max() - X[:, 5].min())) * 180
    edge_norm = (X[:, 6] - X[:, 6].min()) / (X[:, 6].max() - X[:, 6].min())
    edge_colors = plt.cm.plasma(edge_norm)

    for i in range(len(X)):
        f8p = ax.scatter(X[i, 0], X[i, 1], X[i, 2], c=X[i, 3], s=size[i], cmap='viridis', alpha=alpha[i], marker=(4, 0, theta[i]), edgecolor=edge_colors[i], linewidth=1.5)

    vmax = np.max(np.abs(X[:, 3]))
    f8p.set_clim(-vmax, vmax)
    ax.tick_params(labelsize=15)
    ax.set_title('8D Scatter Plot of Function 8\n(3D + Colour + Size-from-y + Alpha-from-x5 + Rotation-from-x6 + Edge Colour-from-x7)', size=20)
    ax.set_xlabel(r"$x_1$", size=20)
    ax.set_ylabel(r"$x_2$", size=20)
    ax.set_zlabel(r"$x_3$", size=20)
    
    cbar_main = plt.colorbar(f8p, shrink=0.6, pad=0)
    cbar_main.ax.tick_params(labelsize=14)
    cbar_main.set_label("4th dimension (x4) — main colour", fontsize=15)
    plt.show()
