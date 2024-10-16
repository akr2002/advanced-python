import matplotlib.pyplot as plt


def visualize_data():
    # Scatter Plot Example
    def scatter_plot():
        # Data for scatter plot
        x = [10, 20, 30, 40, 50, 60, 70]
        y = [15, 25, 35, 45, 55, 65, 75]
        sizes = [20, 50, 80, 200, 300, 400, 500]  # Size of points

        plt.figure(figsize=(6, 4))
        plt.scatter(x, y, s=sizes, color="blue", alpha=0.5)
        plt.title("Scatter Plot Example")
        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")
        plt.grid(True)
        plt.show()

    # Pie Chart Example
    def pie_chart():
        # Data for pie chart
        labels = ["Category A", "Category B", "Category C", "Category D"]
        sizes = [40, 30, 20, 10]
        colors = ["gold", "yellowgreen", "lightcoral", "lightskyblue"]
        explode = (0.1, 0, 0, 0)  # Explode the 1st slice (Category A)

        plt.figure(figsize=(6, 6))
        plt.pie(
            sizes,
            explode=explode,
            labels=labels,
            colors=colors,
            autopct="%1.1f%%",
            shadow=True,
            startangle=140,
        )
        plt.title("Pie Chart Example")
        plt.axis(
            "equal"
        )  # Equal aspect ratio ensures that the pie is drawn as a circle.
        plt.show()

    # Bar Graph Example
    def bar_graph():
        # Data for bar graph
        categories = ["Category A", "Category B", "Category C", "Category D"]
        values = [30, 70, 50, 85]

        plt.figure(figsize=(8, 5))
        plt.bar(categories, values, color=["blue", "green", "red", "orange"])
        plt.title("Bar Graph Example")
        plt.xlabel("Categories")
        plt.ylabel("Values")
        plt.show()

    # Call the functions
    scatter_plot()
    pie_chart()
    bar_graph()


# Execute the program
visualize_data()
