# Extract role ARN
role_arn = iam.get_role(
    RoleName = role_name
)["Role"]["Arn"]
print("Role {}'s ARN is: {}".format(role_name, role_arn))