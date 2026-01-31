import math

def circle_area_coverage(radius_of_circle_1, radius_of_circle_2):
    """
    Calculates the percentage of the larger circle's area that can be
    covered by the smaller circle.

    """

    # Validate that both radii are positive
    if radius_of_circle_1 <= 0 or radius_of_circle_2 <= 0:
        return "Error: Both radii must be positive integers."

    # Calculate the area of both circles
    area_of_circle_1 = math.pi * radius_of_circle_1 ** 2
    area_of_circle_2 = math.pi * radius_of_circle_2 ** 2

    # Determine smaller and larger areas
    smaller_area = min(area_of_circle_1, area_of_circle_2)
    larger_area = max(area_of_circle_1, area_of_circle_2)

    # Calculate percentage coverage
    coverage_percentage = (smaller_area / larger_area) * 100

    return coverage_percentage

radius_of_circle1 = 3
radius_of_circle2 = 5
print(circle_area_coverage(radius_of_circle1, radius_of_circle2))
