try:
  # Delete Cluster
  redshift.delete_cluster(
    ClusterIdentifier = cluster_identifier,
    SkipFinalClusterSnapshot = True,
  )

  print("A cluster named {} exists".format(cluster_identifier))
  print("Deleting existing cluster named {}...".format(cluster_identifier))


  # Wait for the cluster status change to deleted
  delete_waiter = redshift.get_waiter("cluster_deleted")
  delete_waiter.wait(
    ClusterIdentifier = cluster_identifier,
    WaiterConfig = {
      "Delay": 30,
      "MaxAttempts": 20
  }
  )

  print("Cluster named {} deleted".format(cluster_identifier))

except:
  print("A cluster named {} does not exist".format(cluster_identifier))  