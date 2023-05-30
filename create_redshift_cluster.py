# Delete Redshift cluster with the same name if it exists

try:
  # Delete Cluster
  redshift.delete_cluster(
    ClusterIdentifier = cluster_identifier,
    SkipFinalClusterSnapshot = True,
  )

  print("A cluster named '{}' already exists".format(cluster_identifier))
  print("Deleting existing cluster named '{}'...".format(cluster_identifier))

  # Wait for the cluster status change to deleted
  delete_waiter = redshift.get_waiter("cluster_deleted")
  delete_waiter.wait(
    ClusterIdentifier = cluster_identifier,
    WaiterConfig = {
      "Delay": 30,
      "MaxAttempts": 20
    }
  )

  print("Existing cluster named '{}' deleted".format(cluster_identifier))
except:
  print("A cluter named '{}' does not exists".format(cluster_identifier))

# Create Redshift cluster
try:
  cluster = reshift.create_cluster(
    DBName = database_name,
    ClusterIdentifier = cluster_identifier,
    ClusterType = cluster_type,
    NodeType = node_type,
    MaterUsername = username,
    MastrUSerPassword = password,
    Port = port,
    IamRoles = [role_arn]
  )
except Exception as e:
  print(e)

print("New cluster named '{}' created and available".format(cluster_identifier))

#Extract cluster info
clusters = redshift.describe_clusters(
  ClusterIdentifier = cluster_identifier
)["Clusters"]

for cluster in clusters:
  if cluster["ClusterIdentifier"] == cluster_identifier:
    break

cluster_endpoint = cluster["Endpoint"]["Address"]
vpc_secrity_group_id = cluster["VpcSecurityGroup"][0]["VpcSecurityGroupId"]

print("Cluster '{}' endpoint is '{}'".format(cluster_identifier, cluster_endpoint))
print("Cluster '{}''s VPC security group ID is '{}'".format(cluster_identifier, vpc_security_group_id))