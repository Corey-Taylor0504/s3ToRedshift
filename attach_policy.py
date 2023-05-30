# Attach policy to IAM role
try:
  attachment = iam.attach_role_policy(
    RoleName = role_name,
    PolicyArn = policy_arn
  )
  print("Policy named {} attached to role {}".format(policy_name, role_name))
except Exception as e:
  print(str(e))