from AWS_IAM_RolePolicyCheck import RolePolicyCheck

# JSON Policy file to be checked
source = "example.json"

rpc = RolePolicyCheck(source)


if __name__ == "__main__":
    print(rpc.resource_verify())
