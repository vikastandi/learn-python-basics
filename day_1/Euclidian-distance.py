# Implement function to calculate Euclidian distance between two points (x1, y1) and (x2, y2)
# write a function get_euclidian_distance(x1, y1, x2, y2) that returns the Euclidian distance between two points (x1, y1) and (x2, y2)

def get_euclidian_distance(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

#call get_euclidian_distance inside main function
if __name__ == '__main__':
    print(get_euclidian_distance(0, 0, 1, 1)) # 1.4142135623730951