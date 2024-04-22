from .RolePolicyExceptionHandler import *
from .RolePolicy import *


class RolePolicyCheck:
    policy = ""

    def __init__(self, source) -> None:
        try:
            self.policy = RolePolicy(source)
        except PolicyNameException as e:
            raise RolePolicyException(e)
        except PolicyDocumentException as e:
            raise RolePolicyException(e)

    def resource_verify(self) -> list:
        status = []
        for statement in self.policy.content["PolicyDocument"]["Statement"]:
            if statement["Resource"] == "*":
                status.append(False)
            else:
                status.append(True)
        return status
