# Change directory to the one containing the project
PROJECT_DIRECTORY=PROJECT_DIRECTORY:/<path to local project>/
cd PROJECT_DIRECTORY

# Compile the project with sbt assembly
sbt assembly

# Move the .jar file to S3 bucket
aws s3 cp PROJECT_DIRECTORY/RedMug/target/scala-2.11/KafkaProducerConsumerSbt-assembly-1.0.jar s3://red-mug/

# Spin up the EMR
# EMR variables
emr_version='emr-5.28.0'
cluster_name='redMugEMR'
aws_subnet='subnet-ae69cad6'
ec2_key=PROJECT_DIRECTORY/redMugKey.pem
s3_log_bucket='red-mug'$cluster_name
# spin up cluster
aws emr create-cluster \
--name=$cluster_name \
--release-label $emr_version \
--instance-groups InstanceGroupType=MASTER,InstanceCount=1,InstanceType=m5.xlarge InstanceGroupType=CORE,InstanceCount=2,InstanceType=m5.xlarge \
--applications Name=Spark\
--use-default-roles \
--ec2-attributes SubnetIds=$aws_subnet,KeyName=$ec2_key \
--log-uri $s3_log_bucket

# SSH into the EMR machine
ssh -i PROJECT_DIRECTORY/redMugKey.pem hadoop@ec2-34-222-197-232.us-west-2.compute.amazonaws.com

# Copy jar file from S3 RedMug bucket to the current directory in the EMR
aws s3 cp s3://red-mug/KafkaProducerConsumerSbt-assembly-1.0.jar ./

# Run .jar file from EMR
spark-submit --class red.mug.KafkaProducerConsumerSbt KafkaProducerConsumerSbt-assembly-1.0.jar