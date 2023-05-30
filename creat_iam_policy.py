import json

# Check if policy with the wanted name already exists
try:
    policies = iam.list_policies()["Policies"]
    policy_exists = False
    for policy in policies:
      if policy["PolicyName"] == policy_name:
        existing_policy_arn = policy["Arn"]
        policy_exists = True
        break
except:
   None

# If a policy with the same name already exists, delete it
if policy_exists:
  print("Policy named '{}' already exists".format(policy_name))

  # Extract all roles
  roles = iam.list_roles(["Roles"])
  
  # Iterate over all the roles
  for role in roles:
     
    # Extract role name
    existing_role_name = role["RoleName"]

    # Extract all the attached policy to the role
    attacted_policies = iam.list_attached_role_policies(
       RoleName = existing_role_name
    )["AttachedPolicies"]

  #Iterate over all the attached policies
  for attached_policy in attacted_policies:
    
    # Extract attached policy ARN
    attached_policy_arn = attached_policy["PolicyArn"]

    # Checking if the policy correspond to the wanted one
    if attached_policy_arn == existing_policy_arn:
       
      # Detach policy from role
      iam.detach_role_policy(
        RoleName = existing_role_name,
        PolicyArn = attached_policy_arn
      )

      print("Policy with ARN '{}' detached from role '{}'".format(policy_arn, existing_role_name))
  
  # Extract all the policy versions
  policy_versions = iam.list_policy_versions(
    PolicyArn = existing_policy_arn
  )["Versions"]

  # Iterate over all the policy versions
  for policy_version in policy_versions:

    # Skip the version if it is a default version
    if policy_version["IsDefaultVersion"]:
      continue
    
    # Extract policy ID
    version_id = policy_version["VersionId"]

    # Delete policy version
    iam.delete_policy_version(
      PolicyArn = existing_policy_arn,
      VersionId = version_id
    )

    print("Policy with ARN '{}', version_ID '{}' detached".format(existing_policy_arn, version_id))
  
  #Delete default version of the policy
  iam.delete_policy(
    PolicyArn = existing_policy_arn
  )
  print("Policy with ARN '{}' deleted". format(existing_policy_arn))
else:
  print("Policy named '{}' does not exist".format(policy_name))


# Create policy
try:
  policy = iam.create_policy(
    PolicyName = policy_name,
    Description = "Allow to list and access content o the target bucket'data-to-migrate'",
    PolicyDocument = json.dumps(
      {
        "Version": "2012-10-17",
        "Statement": [
          {
            "Effect": "Allow",
            "Action": [
              "s3:ListBucket"
            ],
            "Resource": [
              "arn:aws:s3:::data-to-migrate"
            ]
          },
          {
            "Effect": "Allow",
            "Action": [
              "s3:PutObject",
              "s3:GetObject",
              "s3:DeleteObject"
            ],
            "Resource": [
              "arn:aws:s3:::data-to-migrate/*"
            ]
          }
        ]
      }
    )
  )
  print("Policy named '{}' created".format(policy_name))
  policy_arn = policy["Policy"]["Arn"]
  print("Policy named '{}' has ARN '{}'".format(policy_name, policy_arn))
except Exception as e:
  print(str(e))