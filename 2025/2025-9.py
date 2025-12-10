# 2025-9
### part 1
# similar to yesterday's
import math

def area(x1, y1, x2, y2):
    return ((abs(x1 - x2) + 1) * (abs(y1 - y2) + 1))

def in_rect(x1, y1, x2, y2, x, y):
    # test if x,y is within the bounds
    in_x = x1 <= x <= x2 or x2 <= x <= x1
    in_y = y1 <= y <= y2 or y2 <= y <= y1
    return in_x and in_y

def colinear(x1, y1, x2, y2, x3, y3):
   return (x1 == x2 == x3) or (y1 == y2 == y3) 

def corner(x1, y1, x2, y2, x, y):
    # check if x,y shares at least one same value as x1y1 and x2y2
    x1y1_check = x == x1 or y == y1
    x2y2_check = x == x2 or y == y2
    return x1y1_check and x2y2_check


def has_shared_axis(x1, y1, x2, y2, x, y):
    # check if xy has any shared axis
    x1y1_check = x == x1 or y == y1
    x2y2_check = x == x2 or y == y2
    return x1y1_check or x2y2_check

# thx gemini
def is_point_in_polygon_from_edges(point_to_check, polygon_edges):
    """
    Checks if a point (x, y) is inside or on the boundary of a polygon.
    The polygon is defined by an ordered list of adjacent coordinate pairs (edges).

    Args:
        point_to_check (tuple or list): The coordinates of the test point (x, y).
        polygon_edges (list of tuples of tuples): Ordered list of edges, 
                                                  e.g., [((x1, y1), (x2, y2)), ...].

    Returns:
        bool: True if the point is inside or on the boundary, False otherwise.
    """
    x, y = point_to_check
    inside = False

    # The length of polygon_edges is the number of edges (N)
    if not polygon_edges or len(polygon_edges) < 3:
        return False

    # Loop through each edge (i, j) in the list of edges
    for edge in polygon_edges:
        (xi, yi), (xj, yj) = edge  # Unpack the two vertices of the current edge

        # --- 1. BOUNDARY CHECK: Is the point exactly on the edge? ---
        
        # Check if the point is within the bounding box of the segment
        is_x_in_range = min(xi, xj) <= x <= max(xi, xj)
        is_y_in_range = min(yi, yj) <= y <= max(yi, yj)
        
        if is_x_in_range and is_y_in_range:
            # Check for colinearity (cross product == 0): (j-i) x (p-i) == 0
            cross_product = (xj - xi) * (y - yi) - (yj - yi) * (x - xi)
            
            if cross_product == 0:
                return True 

        # --- 2. RAY CASTING CHECK: Does the ray cross the edge? ---
        
        # Check if the horizontal ray starting at y intersects the edge in the y-range.
        # This implicitly ignores horizontal edges (where yi == yj).
        ray_intersects_edge_in_y = (yi <= y < yj) or (yj <= y < yi)
        
        if ray_intersects_edge_in_y:
            # Check if the intersection point (x_int) is to the right of the test point (x).
            # We use robust cross-multiplication (integer arithmetic).
            dy = yj - yi
            
            # Numerator term: (y - yi) * (xj - xi)
            numerator_term = (y - yi) * (xj - xi)
            
            # Comparison term: (x - xi) * dy
            comparison_term = (x - xi) * dy

            if dy > 0: # Upward edge
                if numerator_term > comparison_term:
                    inside = not inside
            else: # Downward edge (dy < 0)
                if numerator_term < comparison_term: # Inequality flips
                    inside = not inside
                
    return inside

from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

with open("2025-9-input.txt", 'r') as f:
    tiles = []
    taxicabs = []
    adjacent_tiles = []

    # first load into array
    lines = f.readlines()
    for line in lines:
        xy = line.strip().split(',')
        tiles.append((int(xy[0]), int(xy[1])))

    # part 2: add adjacent tiles
    for i in range(len(tiles)):
        if (i + 1) < len(tiles):
            adjacent_tiles.append((tiles[i], tiles[i + 1]))
        else:
            # wrap around case
            adjacent_tiles.append((tiles[i], tiles[0]))

    # ensure no duplicate
    for i in range(len(tiles)):
        for j in range(i + 1, len(tiles)):
            x1, y1 = tiles[i]
            x2, y2 = tiles[j]
            taxicabs.append((area(x1, y1, x2, y2), (x1, y1), (x2, y2)))
    ###  part 2
    taxicabs = sorted(taxicabs, reverse=True, key=lambda item: item[0])

    polygon = Polygon(tiles)

    # brute force
    for dist, (x1, y1), (x2, y2) in taxicabs:
        
        # rect
        rect = Polygon([(x1, y1), (x1, y2), (x2, y2), (x2, y1)])
        if polygon.contains(rect): 
            print(dist)
            break
