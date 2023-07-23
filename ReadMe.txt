1. EFS system should be in a VPC
2. Create access point for VPC to be configured in Lambda.
3. If lambda needs to write to root folder of EFS then
   a. While creating access point use "root" user POSIX ID i.e. 0 in the fields where POSIX user id is required.
   b. Root Directory path of access point  should be \
4. If lambda needs to write to other folder of EFS then
   a. While creating access point use POSIX ID  the user who is owner of the folder
   b. Root Directory path of access point should be folder name you plan to write to.
5. In Lambda configuration configure lambda to be in same VPC of EFS.  Also map all subnets that EFS is configured for access.
6. Use Same security group for EFS and Lambda function
7. Open 2049 port in security group for lambda function for incoming requests. This is needed for EFS (which  internally  NFS) access to work.
8. Create VPC endpoint for S3 service so that the lambda function can connnect to the S3 Service
9. Once everything starts working the EFS path can be configured as environment variable and be accessed in code. Example is below
    import os
    region = os.environ['EFS_PATH']


