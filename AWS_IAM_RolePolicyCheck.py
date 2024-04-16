import json
import re
import numbers as nm


class RolePolicyCheck:
    file = ""
    pattern = re.compile("[\w+=,.@-]+")

    def __init__(self, source) -> None:
        self.document_verify(source)
        self.file = source

    def resource_verify(self) -> bool:
        with open(self.file) as f:
            policy = json.load(f)
            for statement in policy["PolicyDocument"]["Statement"]:
                if statement["Resource"] == "*":
                    return False
            return True

    def document_verify(self, file):
        with open(file) as f:
            try:
                policy = json.load(f)

                # PolicyName
                if "PolicyName" not in policy:
                    print("Document does not contain 'PolicyName'!")
                if type(policy["PolicyName"]) is not str:
                    print("'PolicyName' is not a string!")
                if self.pattern.fullmatch(policy["PolicyName"]) is None:
                    print("Document contains invalid 'PolicyName'!")
                if len(policy["PolicyName"]) not in range(1, 128):
                    print("Incorrect length of 'PolicyName'!")

                # PolicyDocument
                if "PolicyDocument" not in policy:
                    print("Document does not contain 'PolicyDocument'!")
                if (
                    type(policy["PolicyDocument"]) is not dict
                    or [
                        key
                        for key in policy["PolicyDocument"].keys()
                        if type(key) is not str
                    ]
                    or [
                        value
                        for value in policy["PolicyDocument"].values()
                        if not isinstance(
                            value, (str, nm.Number, bool, type(None), object, list)
                        )
                    ]
                ):
                    print("'PolicyDocument' is not valid JSON structure!")

            except ValueError:
                print("Invalid JSON file!")
