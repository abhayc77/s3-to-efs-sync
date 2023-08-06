1.  Create lambda function using the code. In the AWS console lamba UI, add trigger with S3 service and createobject event.
    Select the bucket that is target for sync. For each bucket you need to add new trigger.
2.  EFS system should be in a VPC.
3.  Create access point for VPC to be configured in Lambda as described in either 3 or 4 below.
4.  Do note that the root specified on this access path is the folder the files will be copied to.
5.  If lambda needs to sync to root folder of EFS then
    a. While creating access point use "root" user POSIX ID i.e. 0 in the fields where POSIX user id is required.
    b. Root Directory path of access point  should be \
6.  If lambda needs to sync to other folder of EFS then
    a. While creating access point use POSIX ID  the user who is owner of the folder
    b. Root Directory path of access point should be folder name you plan to write to.
7.  In permissions tab Use existing /Create New Role for Lambda
    a. AWSLambdaExecute: Provides Put, Get access to S3 and full access to CloudWatch Logs.
    b. AmazonS3ReadOnlyAccess: Provides read only access to all buckets via the AWS Management Console.
    c. AmazonElasticFileSystemFullAccess: Provides full access to Amazon EFS via the AWS Management Console.
    d. AWSLambdaVPCAccessExecutionRole	: Provides minimum permissions for a Lambda function to execute while accessing a resource within a VPC - create, describe, delete network interfaces and write permissions to CloudWatch Logs.
    e. AmazonS3ObjectLambdaExecutionRolePolicy	: Provides AWS Lambda functions permissions to interact with Amazon S3 Object Lambda. Also grants Lambda permissions to write to CloudWatch Logs.
8.  In Lambda configuration configure lambda to be in same VPC of EFS.  Also map all subnets that EFS is configured for access.6. Use Same security group for EFS and Lambda function
9.  Open 2049 port in security group for lambda function for incoming requests. This is needed for EFS (which  internally  NFS) access to work.
10. Create VPC endpoint for S3 service so that the lambda function can connnect to the S3 Service
11. Once everything starts working the 'EFS_PATH' path can be configured as environment variable and be accessed in code. Example is below
    import os
    region = os.environ['EFS_PATH']


