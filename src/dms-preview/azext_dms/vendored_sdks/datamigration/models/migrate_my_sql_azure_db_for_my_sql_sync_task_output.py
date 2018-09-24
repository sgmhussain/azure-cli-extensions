# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MigrateMySqlAzureDbForMySqlSyncTaskOutput(Model):
    """Output for the task that migrates MySQL databases to Azure Database for
    MySQL for online migrations.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: MigrateMySqlAzureDbForMySqlSyncTaskOutputDatabaseError,
    MigrateMySqlAzureDbForMySqlSyncTaskOutputError,
    MigrateMySqlAzureDbForMySqlSyncTaskOutputTableLevel,
    MigrateMySqlAzureDbForMySqlSyncTaskOutputDatabaseLevel,
    MigrateMySqlAzureDbForMySqlSyncTaskOutputMigrationLevel

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Result identifier
    :vartype id: str
    :param result_type: Required. Constant filled by server.
    :type result_type: str
    """

    _validation = {
        'id': {'readonly': True},
        'result_type': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'result_type': {'key': 'resultType', 'type': 'str'},
    }

    _subtype_map = {
        'result_type': {'DatabaseLevelErrorOutput': 'MigrateMySqlAzureDbForMySqlSyncTaskOutputDatabaseError', 'ErrorOutput': 'MigrateMySqlAzureDbForMySqlSyncTaskOutputError', 'TableLevelOutput': 'MigrateMySqlAzureDbForMySqlSyncTaskOutputTableLevel', 'DatabaseLevelOutput': 'MigrateMySqlAzureDbForMySqlSyncTaskOutputDatabaseLevel', 'MigrationLevelOutput': 'MigrateMySqlAzureDbForMySqlSyncTaskOutputMigrationLevel'}
    }

    def __init__(self, **kwargs):
        super(MigrateMySqlAzureDbForMySqlSyncTaskOutput, self).__init__(**kwargs)
        self.id = None
        self.result_type = None