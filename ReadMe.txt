1. EFS system should be in a VPC
2. Lambda function should be in same VPC
3. Same security group for EFS and Lambda function
4. Open 2049 port in security group for lambda function for incoming requests. This is needed for EFS (which  internally  NFS)access to work.
5. Create VPC endgpoint for S3 service so that the lambda function can connnect to the S3 Service

