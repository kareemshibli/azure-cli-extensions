# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "adp workspace create",
)
class Create(AAZCommand):
    """Create a Workspace
    """

    _aaz_info = {
        "version": "2022-09-01-preview",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.autonomousdevelopmentplatform/workspaces/{}", "2022-09-01-preview"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.workspace_name = AAZStrArg(
            options=["-n", "--name", "--workspace-name"],
            help="Workspace Name",
            required=True,
            id_part="name",
            fmt=AAZStrArgFormat(
                pattern="^[a-z0-9][-a-z0-9]{0,45}$",
                max_length=46,
            ),
        )

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.domain_label_scope = AAZStrArg(
            options=["--domain-label-scope"],
            arg_group="Properties",
            help="The scope for the FQDN label generation. If not provided, defaults to TenantReuse.",
            enum={"NoReuse": "NoReuse", "ResourceGroupReuse": "ResourceGroupReuse", "SubscriptionReuse": "SubscriptionReuse", "TenantReuse": "TenantReuse"},
        )
        _args_schema.data_location = AAZStrArg(
            options=["--data-location"],
            arg_group="Properties",
            help="The Workspace's data location. If not provided, defaults to the resource's location.",
        )
        _args_schema.encryption = AAZObjectArg(
            options=["--encryption"],
            arg_group="Properties",
            help="The encryption configuration.",
        )
        _args_schema.source_resource_id = AAZStrArg(
            options=["--source-resource-id"],
            arg_group="Properties",
            help="The ARM Id of the source resource that originated the data for this Workspace",
        )
        _args_schema.storage_account_count = AAZIntArg(
            options=["--storage-account-count"],
            arg_group="Properties",
            help="The amount of storage accounts provisioned per Workspace. If not provided, defaults to 5.",
            fmt=AAZIntArgFormat(
                minimum=1,
            ),
        )
        _args_schema.storage_sku = AAZObjectArg(
            options=["--storage-sku"],
            arg_group="Properties",
            help="The Storage SKU. If not provided, defaults to Standard_ZRS.",
        )

        encryption = cls._args_schema.encryption
        encryption.user_assigned_identity_resource_id = AAZStrArg(
            options=["user-assigned-identity-resource-id"],
            help="User assigned identity to use for accessing key encryption key Url. Example: /subscriptions/<subscription id>/resourceGroups/<resource group>/providers/Microsoft.ManagedIdentity/userAssignedIdentities/myId.",
        )
        encryption.key_encryption_key_url = AAZStrArg(
            options=["key-encryption-key-url"],
            help="The key encryption key Url, versioned or not. Example: https://contosovault.vault.azure.net/keys/contosokek/562a4bb76b524a1493a6afe8e536ee78 or https://contosovault.vault.azure.net/keys/contosokek.",
        )

        storage_sku = cls._args_schema.storage_sku
        storage_sku.name = AAZStrArg(
            options=["name"],
            help="The SKU name.",
            required=True,
            enum={"Premium_LRS": "Premium_LRS", "Premium_ZRS": "Premium_ZRS", "Standard_GRS": "Standard_GRS", "Standard_GZRS": "Standard_GZRS", "Standard_LRS": "Standard_LRS", "Standard_RAGRS": "Standard_RAGRS", "Standard_RAGZRS": "Standard_RAGZRS", "Standard_ZRS": "Standard_ZRS"},
        )

        # define Arg Group "Resource"

        _args_schema = cls._args_schema
        _args_schema.identity = AAZObjectArg(
            options=["--identity"],
            arg_group="Resource",
            help="The managed service identities assigned to this resource.",
        )
        _args_schema.location = AAZResourceLocationArg(
            arg_group="Resource",
            help="The geo-location where the resource lives",
            required=True,
            fmt=AAZResourceLocationArgFormat(
                resource_group_arg="resource_group",
            ),
        )
        _args_schema.tags = AAZDictArg(
            options=["--tags"],
            arg_group="Resource",
            help="Resource tags.",
        )

        identity = cls._args_schema.identity
        identity.identity = AAZObjectArg(
            options=["identity"],
            help="The managed service identities assigned to this resource.",
        )

        identity = cls._args_schema.identity.identity
        identity.type = AAZStrArg(
            options=["type"],
            help="The type of managed identity assigned to this resource.",
            required=True,
            enum={"None": "None", "SystemAssigned": "SystemAssigned", "SystemAssigned, UserAssigned": "SystemAssigned, UserAssigned", "UserAssigned": "UserAssigned"},
        )
        identity.user_assigned_identities = AAZDictArg(
            options=["user-assigned-identities"],
            help="The identities assigned to this resource by the user.",
        )

        user_assigned_identities = cls._args_schema.identity.identity.user_assigned_identities
        user_assigned_identities.Element = AAZObjectArg(
            blank={},
        )

        tags = cls._args_schema.tags
        tags.Element = AAZStrArg()
        return cls._args_schema

    def _execute_operations(self):
        yield self.WorkspacesCreateOrUpdate(ctx=self.ctx)()

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class WorkspacesCreateOrUpdate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200, 201]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AutonomousDevelopmentPlatform/workspaces/{workspaceName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
                **self.serialize_url_param(
                    "workspaceName", self.ctx.args.workspace_name,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2022-09-01-preview",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                typ=AAZObjectType,
                typ_kwargs={"flags": {"required": True, "client_flatten": True}}
            )
            _builder.set_prop("identity", AAZObjectType, ".identity")
            _builder.set_prop("location", AAZStrType, ".location", typ_kwargs={"flags": {"required": True}})
            _builder.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})
            _builder.set_prop("tags", AAZDictType, ".tags")

            identity = _builder.get(".identity")
            if identity is not None:
                identity.set_prop("identity", AAZObjectType, ".identity")

            identity = _builder.get(".identity.identity")
            if identity is not None:
                identity.set_prop("type", AAZStrType, ".type", typ_kwargs={"flags": {"required": True}})
                identity.set_prop("userAssignedIdentities", AAZDictType, ".user_assigned_identities")

            user_assigned_identities = _builder.get(".identity.identity.userAssignedIdentities")
            if user_assigned_identities is not None:
                user_assigned_identities.set_elements(AAZObjectType, ".")

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("autoGeneratedDomainNameLabelScope", AAZStrType, ".domain_name_label_scope")
                properties.set_prop("dataLocation", AAZStrType, ".data_location")
                properties.set_prop("encryption", AAZObjectType, ".encryption")
                properties.set_prop("sourceResourceId", AAZStrType, ".source_resource_id")
                properties.set_prop("storageAccountCount", AAZIntType, ".storage_account_count")
                properties.set_prop("storageSku", AAZObjectType, ".storage_sku")

            encryption = _builder.get(".properties.encryption")
            if encryption is not None:
                encryption.set_prop("customerManagedKeyEncryption", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})

            customer_managed_key_encryption = _builder.get(".properties.encryption.customerManagedKeyEncryption")
            if customer_managed_key_encryption is not None:
                customer_managed_key_encryption.set_prop("keyEncryptionKeyIdentity", AAZObjectType, ".", typ_kwargs={"flags": {"required": True, "client_flatten": True}})
                customer_managed_key_encryption.set_prop("keyEncryptionKeyUrl", AAZStrType, ".key_encryption_key_url", typ_kwargs={"flags": {"required": True}})

            key_encryption_key_identity = _builder.get(".properties.encryption.customerManagedKeyEncryption.keyEncryptionKeyIdentity")
            if key_encryption_key_identity is not None:
                key_encryption_key_identity.set_prop("userAssignedIdentityResourceId", AAZStrType, ".user_assigned_identity_resource_id", typ_kwargs={"flags": {"required": True}})

            storage_sku = _builder.get(".properties.storageSku")
            if storage_sku is not None:
                storage_sku.set_prop("name", AAZStrType, ".name", typ_kwargs={"flags": {"required": True}})

            tags = _builder.get(".tags")
            if tags is not None:
                tags.set_elements(AAZStrType, ".")

            return self.serialize_content(_content_value)

        def on_200_201(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200_201
            )

        _schema_on_200_201 = None

        @classmethod
        def _build_schema_on_200_201(cls):
            if cls._schema_on_200_201 is not None:
                return cls._schema_on_200_201

            cls._schema_on_200_201 = AAZObjectType()

            _schema_on_200_201 = cls._schema_on_200_201
            _schema_on_200_201.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200_201.identity = AAZObjectType()
            _schema_on_200_201.location = AAZStrType(
                flags={"required": True},
            )
            _schema_on_200_201.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200_201.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _schema_on_200_201.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _schema_on_200_201.tags = AAZDictType()
            _schema_on_200_201.type = AAZStrType(
                flags={"read_only": True},
            )

            identity = cls._schema_on_200_201.identity
            identity.identity = AAZObjectType()

            identity = cls._schema_on_200_201.identity.identity
            identity.principal_id = AAZStrType(
                serialized_name="principalId",
                flags={"read_only": True},
            )
            identity.tenant_id = AAZStrType(
                serialized_name="tenantId",
                flags={"read_only": True},
            )
            identity.type = AAZStrType(
                flags={"required": True},
            )
            identity.user_assigned_identities = AAZDictType(
                serialized_name="userAssignedIdentities",
            )

            user_assigned_identities = cls._schema_on_200_201.identity.identity.user_assigned_identities
            user_assigned_identities.Element = AAZObjectType()

            _element = cls._schema_on_200_201.identity.identity.user_assigned_identities.Element
            _element.client_id = AAZStrType(
                serialized_name="clientId",
                flags={"read_only": True},
            )
            _element.principal_id = AAZStrType(
                serialized_name="principalId",
                flags={"read_only": True},
            )

            properties = cls._schema_on_200_201.properties
            properties.auto_generated_domain_name_label_scope = AAZStrType(
                serialized_name="autoGeneratedDomainNameLabelScope",
            )
            properties.data_catalog = AAZObjectType(
                serialized_name="dataCatalog",
            )
            properties.data_location = AAZStrType(
                serialized_name="dataLocation",
            )
            properties.encryption = AAZObjectType()
            properties.endpoint = AAZStrType(
                flags={"read_only": True},
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.source_resource_id = AAZStrType(
                serialized_name="sourceResourceId",
            )
            properties.storage_account_count = AAZIntType(
                serialized_name="storageAccountCount",
            )
            properties.storage_sku = AAZObjectType(
                serialized_name="storageSku",
            )

            data_catalog = cls._schema_on_200_201.properties.data_catalog
            data_catalog.data_explorer = AAZObjectType(
                serialized_name="dataExplorer",
            )
            data_catalog.external_workspace_ids = AAZListType(
                serialized_name="externalWorkspaceIds",
            )
            data_catalog.state = AAZStrType(
                flags={"required": True},
            )

            data_explorer = cls._schema_on_200_201.properties.data_catalog.data_explorer
            data_explorer.azure_sku = AAZObjectType(
                serialized_name="azureSku",
                flags={"required": True, "client_flatten": True},
            )

            azure_sku = cls._schema_on_200_201.properties.data_catalog.data_explorer.azure_sku
            azure_sku.capacity = AAZIntType()
            azure_sku.name = AAZStrType()
            azure_sku.tier = AAZStrType()

            external_workspace_ids = cls._schema_on_200_201.properties.data_catalog.external_workspace_ids
            external_workspace_ids.Element = AAZStrType()

            encryption = cls._schema_on_200_201.properties.encryption
            encryption.customer_managed_key_encryption = AAZObjectType(
                serialized_name="customerManagedKeyEncryption",
                flags={"client_flatten": True},
            )

            customer_managed_key_encryption = cls._schema_on_200_201.properties.encryption.customer_managed_key_encryption
            customer_managed_key_encryption.key_encryption_key_identity = AAZObjectType(
                serialized_name="keyEncryptionKeyIdentity",
                flags={"required": True, "client_flatten": True},
            )
            customer_managed_key_encryption.key_encryption_key_url = AAZStrType(
                serialized_name="keyEncryptionKeyUrl",
                flags={"required": True},
            )

            key_encryption_key_identity = cls._schema_on_200_201.properties.encryption.customer_managed_key_encryption.key_encryption_key_identity
            key_encryption_key_identity.user_assigned_identity_resource_id = AAZStrType(
                serialized_name="userAssignedIdentityResourceId",
                flags={"required": True},
            )

            storage_sku = cls._schema_on_200_201.properties.storage_sku
            storage_sku.name = AAZStrType(
                flags={"required": True},
            )

            system_data = cls._schema_on_200_201.system_data
            system_data.created_at = AAZStrType(
                serialized_name="createdAt",
                flags={"read_only": True},
            )
            system_data.created_by = AAZStrType(
                serialized_name="createdBy",
                flags={"read_only": True},
            )
            system_data.created_by_type = AAZStrType(
                serialized_name="createdByType",
                flags={"read_only": True},
            )
            system_data.last_modified_at = AAZStrType(
                serialized_name="lastModifiedAt",
                flags={"read_only": True},
            )
            system_data.last_modified_by = AAZStrType(
                serialized_name="lastModifiedBy",
                flags={"read_only": True},
            )
            system_data.last_modified_by_type = AAZStrType(
                serialized_name="lastModifiedByType",
                flags={"read_only": True},
            )

            tags = cls._schema_on_200_201.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200_201


__all__ = ["Create"]
