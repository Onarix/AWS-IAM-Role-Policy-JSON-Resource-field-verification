from AWS_IAM.RolePolicy import *
from AWS_IAM.RolePolicyCheck import *
from AWS_IAM.RolePolicyExceptionHandler import *
import pytest

example = "example.json"
sample_1 = "./tests/sample_1.json"
sample_2 = "./tests/sample_2.json"
sample_3 = "./tests/sample_3.json"


# Valid Role Policy Files with resource check
def test_valid_resource_check():
    rpc = RolePolicyCheck(example)
    assert rpc.resource_verify() == [False]


def test_sample_1():
    rpc = RolePolicyCheck(sample_1)
    assert rpc.resource_verify() == [False, True, True, False]


# Invalid Role Policy files
def test_sample_2():
    with pytest.raises(PolicyNameException) as e:
        try:
            rpc = RolePolicyCheck(sample_2)
        except RolePolicyException as err:
            raise PolicyNameException(str(err.parameter))
    assert str(e.value) == "Document contains invalid 'PolicyName'!"


def test_sample_3():
    with pytest.raises(PolicyDocumentException) as e:
        try:
            rpc = RolePolicyCheck(sample_3)
        except RolePolicyException as err:
            raise PolicyDocumentException(str(err.parameter))
    assert str(e.value) == "'PolicyDocument' is not valid JSON structure!"
