# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RoaRequest

class DeleteRepositoryProtectedBranchRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'codeup', '2020-04-14', 'DeleteRepositoryProtectedBranch')
		self.set_uri_pattern('/api/v4/projects/[ProjectId]/repository/protect_branches/[ProtectedBranchId]')
		self.set_method('DELETE')

	def get_OrganizationId(self):
		return self.get_query_params().get('OrganizationId')

	def set_OrganizationId(self,OrganizationId):
		self.add_query_param('OrganizationId',OrganizationId)

	def get_ProtectedBranchId(self):
		return self.get_path_params().get('ProtectedBranchId')

	def set_ProtectedBranchId(self,ProtectedBranchId):
		self.add_path_param('ProtectedBranchId',ProtectedBranchId)

	def get_AccessToken(self):
		return self.get_query_params().get('AccessToken')

	def set_AccessToken(self,AccessToken):
		self.add_query_param('AccessToken',AccessToken)

	def get_ProjectId(self):
		return self.get_path_params().get('ProjectId')

	def set_ProjectId(self,ProjectId):
		self.add_path_param('ProjectId',ProjectId)