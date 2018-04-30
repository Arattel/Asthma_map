from point import Point


class PossiblePoints(object):
    """
    This class is created to represent point collection
    """
    def __init__(self):
        """
        (PossiblePoints) -> None
        This method creates PossiblePoints object
        """
        self.points = []

    def add_point(self, point):
        """
        (PossiblePoints, Point) -> None
        This method adds a point into PossiblePoints instance
        """
        self.points.append(point)

    def __str__(self):
        """
        (PossiblePoints) -> (str)
        """
        s = ''
        for i in self.points:
            s += str(i) + '\n'
        return s

    def distance_list(self, point, radius = 0):
        """
        (PossiblePoints, Point) -> None
        This method creates a sorted list of points and distances from point to argument point
        """
        a = sorted(list(map(lambda x: [x, x.find_distance(point)], self.points)), key=lambda x: x[1])
        if radius:
            a = list(filter(lambda x: x[1] < radius, a))
        return a




