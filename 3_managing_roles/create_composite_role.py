# Copyright 2020 StrongDM Inc
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import os
import strongdm

#	Load the SDM API keys from the environment.
#	If these values are not set in your environment,
#	please follow the documentation here:
#	https://www.strongdm.com/docs/admin-guide/api-credentials/
api_access_key = os.getenv("SDM_API_ACCESS_KEY")
api_secret_key = os.getenv("SDM_API_SECRET_KEY")
client = strongdm.Client(api_access_key, api_secret_key)

# Create a composite role
composite = strongdm.Role(
    name="example composite role",
    composite=True,
)

composite_response = client.roles.create(composite, timeout=30)

print("Successfully created composite role.")
print("\tID: ", composite_response.role.id)

# Create a role
role = strongdm.Role(
    name="example role",
)

role_response = client.roles.create(role, timeout=30)

print("Successfully created role.")
print("\tID: ", role_response.role.id)

# Attach the user to the role
grant = strongdm.RoleAttachment(
    composite_role_id=composite_response.role.id,
    attached_role_id=role_response.role.id,

)

attachment_response = client.role_attachments.create(grant, timeout=30)

print("Successfully created account attachment.")
print("\tID: ", attachment_response.role_attachment.id)
