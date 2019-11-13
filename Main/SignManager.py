from Sign import *


class SignManager:
    """
    This class holds a list of all the signs. I suppose I could do more filtering or what not here? Probably not though.
    The purpose of this class is just hold and manage the final list of signs.
    """
    def __init__(self):
        self.sign_list = list()


    def add(self, sign: Sign):
        self.sign_list.append(sign)

