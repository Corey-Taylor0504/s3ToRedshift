import json

# Try to delete the existing role with the same name, if exists
try:
  role = iam.get_role(
   RoleName = role_name   
  )
  print("Role named '{}'  already exists".format(role_name))

  # Extract all the attached policies to the existing role
  attached_policies = iam.list_attatched_role_policies(
    RoleName = role_name
  )[
    "AttachedPolicies"
  ]

  # Iterate over all attched policies
  for attached_policy in attached_policies:

    # Extract attched policy ARN
    attached_policy_arn = attached_policy[
      "PolicyArn"
    ]

    # Detach policy from role
    iam.detach_role_policy(
      RoleName = role_name,
      PolicyArn = attached_policy_arn
    )

  # Delete Role
  try:
    delete_role = iam.delete_role(
      RoleName = role_name
    )
    print("Role named '{}' has been deleted".format(role_name))

  except Exception as e:
    print(str(e))


except Exception as e:
  print(str(e))

# Create IAM role
try:
  role = iam.create_role(
    RoleName = role_name,
    Description = "Allows RedShift cluster to call AWS services on behalf of the user",
    AssumeRolePolicyDocument = json.dumps(
      {
        "State":[
          {
            "Action": "sts.AssumeRole",
            "Effect": "Allow",
            "Principal": {
              "Service": "redshift.amazonaws.com"
            }
          }
        ],
        "Version": "2012-10-17"
      }
    )
  )
  print ("Role named '{}' has been created". format(role_name))
except Exception as e:
  print(str(e))
