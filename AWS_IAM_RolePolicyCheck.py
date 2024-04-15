import json

file = ""


class RolePolicyCheck:
    def __init__(self, source) -> None:
        self.file = source

    def resource_verify(self):
        with open(self.file) as f:
            policy = json.load(f)
            if "*" in policy["PolicyDocument"]["Statement"][0]["Resource"]:
                return False
            return True
