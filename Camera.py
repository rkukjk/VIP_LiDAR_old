class Camera:
    """
    The idea behind this class is to contain the pictures and to have a method to return a picture that is closest to
    a given coordinate. So if I think have a sign somewhere, then I can assign that picture to that sign. That way, I can
    check to see if that sign is a valid sign.


    """
    def __init__(self, path):
        self.path_to_pics = path

