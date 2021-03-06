# Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
# http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.

import boto3

# Create SES client
ses = boto3.client('ses')

response = ses.send_templated_email(
  Source='EMAIL_ADDRESS',
  Destination={
    'ToAddresses': [
      'EMAIL_ADDRESS',
    ],
    'CcAddresses': [
      'EMAIL_ADDRESS',
    ]
  },
  ReplyToAddresses=[
    'EMAIL_ADDRESS',
  ],
  Template='TEMPLATE_NAME',
  TemplateData='{ \"REPLACEMENT_TAG_NAME\":\"REPLACEMENT_VALUE\" }'
)

print(response)
