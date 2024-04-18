from .RolePolicyExceptionHandler import *
import json
import re
import numbers as nm


class RolePolicyCheck:
    file = ""
    content = ""
    pattern = re.compile("[\w+=,.@-]+")

    def __init__(self, source) -> None:
        try:
            self.document_verify(source)
        except PolicyNameException as e:
            raise RolePolicyException(e)
        except PolicyDocumentException as e:
            raise RolePolicyException(e)

        self.file = source

    def resource_verify(self) -> list:
        policy = self.content
        status = []
        for statement in policy["PolicyDocument"]["Statement"]:
            if statement["Resource"] == "*":
                status.append(False)
            else:
                status.append(True)
        return status

    def document_verify(self, file):
        with open(file) as f:
            try:
                policy = json.load(f)
                self.content = policy

                # PolicyName
                if "PolicyName" not in policy:
                    raise PolicyNameException("Document does not contain 'PolicyName'!")
                if type(policy["PolicyName"]) is not str:
                    raise PolicyNameException("'PolicyName' is not a string!")
                if self.pattern.fullmatch(policy["PolicyName"]) is None:
                    raise PolicyNameException("Document contains invalid 'PolicyName'!")
                if len(policy["PolicyName"]) not in range(1, 128):
                    raise PolicyNameException("Incorrect length of 'PolicyName'!")

                # PolicyDocument
                if "PolicyDocument" not in policy:
                    raise PolicyDocumentException(
                        "Document does not contain 'PolicyDocument'!"
                    )
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
                    raise PolicyDocumentException(
                        "'PolicyDocument' is not valid JSON structure!"
                    )

            except ValueError:
                print("Invalid JSON file!")
