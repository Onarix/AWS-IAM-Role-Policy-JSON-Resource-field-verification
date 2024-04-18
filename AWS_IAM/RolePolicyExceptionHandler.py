class RolePolicyException(Exception):
    def __init__(self, value):
        self.parameter = value


class PolicyNameException(RolePolicyException):
    def __init__(self, value):
        self.parameter = value


class PolicyDocumentException(RolePolicyException):
    def __init__(self, value):
        self.parameter = value
