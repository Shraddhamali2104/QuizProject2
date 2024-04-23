import matplotlib

matplotlib.use("Agg")  # Use the Agg backend

import matplotlib.pyplot as plt
import io
import base64
import numpy as np
import random


def plot_data_1(data):
    # Separate lists for first and second elements
    x = [t[1] for t in data]
    y = [int(t[3]) for t in data]

    # Define threshold values
    green_threshold = 7
    blue_threshold = 4

    # Create a scatter plot with colored points
    for i in range(len(x)):
        color = "red"  # Default color is red

        # Determine color based on the y value
        if y[i] > green_threshold:
            color = "green"
        elif blue_threshold <= y[i] <= green_threshold:
            color = "blue"

        # plt.scatter(x[i], y[i], color=color)
        plt.scatter(
            x[i],
            y[i],
            color=color,
            s=150,
            marker="o",
            alpha=0.9,
            edgecolors="black",
            linewidths=0.7,
        )

    plt.xlabel("Subject")
    plt.ylabel("Score")
    plt.title("Subject Vs Score")

    # Save the plot to a BytesIO object
    buffer = io.BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)

    # Encode the plot as base64 string
    plot_data = base64.b64encode(buffer.getvalue()).decode()

    # Close the plot to free up memory
    plt.close()
    return plot_data


def plot_data_2(data):
    # Separate lists for subject and test number
    subjects = [entry[1] for entry in data]
    test_numbers = [int(entry[2]) for entry in data]

    # Define threshold values
    green_threshold = 7
    blue_threshold = 4

    # Create a vertical bar graph with colored bars
    plt.bar(
        range(len(subjects)),
        test_numbers,
        color=[
            (
                "red"
                if val < blue_threshold
                else "blue" if blue_threshold <= val <= green_threshold else "green"
            )
            for val in test_numbers
        ],
        edgecolor="black",
    )

    plt.xlabel("Subject")
    plt.ylabel("Test Number")
    plt.title("Subject Vs Test Number")

    # Set the x-axis tick labels to the subjects
    plt.xticks(range(len(subjects)), subjects)

    # Set y-axis limits to 0 and 60
    plt.ylim(0, 60)

    # Save the plot to a BytesIO object
    buffer = io.BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)

    # Encode the plot as a base64 string
    plot_data = base64.b64encode(buffer.getvalue()).decode()

    # Close the plot to free up memory
    plt.close()

    return plot_data


def plot_data_result(data):
    # Separate lists for first and second elements
    x = [int(t[0]) for t in data]  # Convert to integer
    y = [int(t[1]) for t in data]  # Convert to integer

    # Define threshold values
    green_threshold = 7
    blue_threshold = 4

    # Create a vertical bar graph with colored bars
    plt.bar(
        x,
        y,
        color=[
            (
                "red"
                if val < blue_threshold
                else "blue" if blue_threshold <= val <= green_threshold else "green"
            )
            for val in y
        ],
        edgecolor="black",
    )

    plt.xlabel("Test Number")
    plt.ylabel("Score")
    plt.title("Score Plot")

    # Save the plot to a BytesIO object
    buffer = io.BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)

    # Encode the plot as a base64 string
    plot_data = base64.b64encode(buffer.getvalue()).decode()

    # Close the plot to free up memory
    plt.close()

    return plot_data


def plot_data_result2(data):
    # Separate lists for first and second elements
    x = [int(t[0]) for t in data]  # Convert to integer
    y = [int(t[2]) for t in data]  # Convert to integer

    # Define threshold values
    green_threshold = 7
    blue_threshold = 4

    # Create a line plot with colored curve
    plt.plot(
        x,
        y,
        marker="o",  # add markers at data points
        linestyle="-",  # solid line
        markersize=8,  # adjust marker size
        markerfacecolor="black",  # marker color
        markeredgewidth=1,  # marker edge width
        markeredgecolor="black",  # marker edge color
    )

    plt.xlabel("Test Number")
    plt.ylabel("Time Required")
    plt.title("Time")

    # Save the plot to a BytesIO object
    buffer = io.BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)

    # Encode the plot as a base64 string
    plot_data = base64.b64encode(buffer.getvalue()).decode()

    # Close the plot to free up memory
    plt.close()

    return plot_data


# admin side plots
def plot_data_admin(data):
    # Separate lists for first and second elements
    x = [t[1] for t in data]
    y = [int(t[6]) for t in data]  # Convert to integer

    # Define threshold values
    green_threshold = 7
    blue_threshold = 4

    # Create a scatter plot with colored points
    for i in range(len(x)):
        color = "red"  # Default color is red

        # Determine color based on the y value
        if y[i] > green_threshold:
            color = "green"
        elif blue_threshold <= y[i] <= green_threshold:
            color = "blue"

        # plt.scatter(x[i], y[i], color=color)
        plt.scatter(
            x[i],
            y[i],
            color=color,
            s=150,
            marker="o",
            alpha=0.9,
            edgecolors="black",
            linewidths=0.7,
        )

    plt.xlabel("Students Username")
    plt.ylabel("Scores")
    plt.title("Scatter plot of Students score")

    # Save the plot to a BytesIO object
    buffer = io.BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)

    # Encode the plot as base64 string
    plot_data = base64.b64encode(buffer.getvalue()).decode()

    # Close the plot to free up memory
    plt.close()
    return plot_data


def plot_data_admin2(data):
    # Separate lists for usernames and time
    usernames = [entry[1] for entry in data]
    time = [entry[8] for entry in data]

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(
        time,
        usernames,
        color="blue",
        s=150,
        alpha=0.9,
        edgecolors="black",
        linewidths=0.7,
    )

    # Set labels and title
    plt.xlabel("Time")
    plt.ylabel("Usernames")
    plt.title("Scatter plot of Usernames over Time")

    # Save the plot to a BytesIO object
    buffer = io.BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)

    # Encode the plot as base64 string
    plot_data = base64.b64encode(buffer.getvalue()).decode()

    # Close the plot to free up memory
    plt.close()

    return plot_data
