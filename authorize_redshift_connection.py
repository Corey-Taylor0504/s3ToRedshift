# Set a VPC security group rule to authorize ingress to the cluster's VPC Security Group

try:
  # Define EC2 resources
  ec2 = boto3.resources(
      "ec2",
      region_name = "us-east-1",
      aws_access_key_id = access_key_id,
      aws_secret_access_key = secret_access_key
  )

  # Extract security group for the VPC
  vpc_sg.authorize_ingress(
    GroupName = vpc_sg.group_name,
    CidrIp ="0.0.0.0/0",
    IpProtocol = "TCP",
    FromPort = 5439,
    ToPort = 5439
  )
  print("Ingress to the VPC authorized")

except Exception as e:
  # Check if the error is a duplication error
  if "InvalidPermission.Duplicate" in str(e):
    print("Rule requested already exists")
  else:
    print(e)