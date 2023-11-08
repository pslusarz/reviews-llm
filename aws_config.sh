#!/usr/bin/env bash

#If you have the AWS toolkit plugin installed in intellij, this will
#take the result of the yak command and add it to the aws credentials file
#then select the default profile in the lower right corner (AWS:No credentials selected)

echo "bedrock credentials"

$(yak arn:aws:iam::540686305771:role/role-admins)

if [[ -n $AWS_ACCESS_KEY_ID ]]
  then
    aws configure --profile default set aws_access_key_id $AWS_ACCESS_KEY_ID
    aws configure --profile default set aws_secret_access_key $AWS_SECRET_ACCESS_KEY
    aws configure --profile default set aws_session_token $AWS_SESSION_TOKEN
    aws configure set default.region "us-west-2"
  else
    echo "You need to do a yaks command before the tests will work correctly"
fi
