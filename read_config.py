import configparser

# Read AWS credentials from the config file
cfg_data = configparser.ConfigParser()
cfg_data.read('dl.cfg')

# Save AWS credentials
access_key_id = cfg_data["AWS"]["access_key_id"]
secret_access_key = cfg_data['AWS']["secret_access_key"]

# Save IAM role and IAM policy data
role_name = cfg_data["IAM"]["role_name"]
policy_name = cfg_data["IAM"]["policy_name"]

# Save Redshift cluster
cluster_identifier = cfg_data["Redshift"]["cluster_identifier"]
cluster_type = cfg_data["Redshift"]["cluster_type"]
node_type = cfg_data["Redshift"]["node_type"]
username = cfg_data["Redshift"]["username"]
password = cfg_data["Redshift"]["password"]
database_name = cfg_data["Redshift"]["database_name"]
port = int(cfg_data["Redshift"]["port"])