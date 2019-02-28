
# AUTO-GENERATED file from IFMapApiGenerator. Do Not Edit!

from contrail_heat.resources import contrail
try:
    from heat.common.i18n import _
except ImportError:
    pass
from heat.engine import attributes
from heat.engine import constraints
from heat.engine import properties
try:
    from heat.openstack.common import log as logging
except ImportError:
    from oslo_log import log as logging
import uuid

from vnc_api import vnc_api

LOG = logging.getLogger(__name__)


class ContrailVirtualIp(contrail.ContrailResource):
    PROPERTIES = (
        NAME, FQ_NAME, DISPLAY_NAME, VIRTUAL_IP_PROPERTIES, VIRTUAL_IP_PROPERTIES_ADDRESS, VIRTUAL_IP_PROPERTIES_STATUS, VIRTUAL_IP_PROPERTIES_STATUS_DESCRIPTION, VIRTUAL_IP_PROPERTIES_ADMIN_STATE, VIRTUAL_IP_PROPERTIES_PROTOCOL, VIRTUAL_IP_PROPERTIES_PROTOCOL_PORT, VIRTUAL_IP_PROPERTIES_CONNECTION_LIMIT, VIRTUAL_IP_PROPERTIES_SUBNET_ID, VIRTUAL_IP_PROPERTIES_PERSISTENCE_COOKIE_NAME, VIRTUAL_IP_PROPERTIES_PERSISTENCE_TYPE, ANNOTATIONS, ANNOTATIONS_KEY_VALUE_PAIR, ANNOTATIONS_KEY_VALUE_PAIR_KEY, ANNOTATIONS_KEY_VALUE_PAIR_VALUE, PERMS2, PERMS2_OWNER, PERMS2_OWNER_ACCESS, PERMS2_GLOBAL_ACCESS, PERMS2_SHARE, PERMS2_SHARE_TENANT, PERMS2_SHARE_TENANT_ACCESS, TAG_REFS, VIRTUAL_MACHINE_INTERFACE_REFS, LOADBALANCER_POOL_REFS, PROJECT
    ) = (
        'name', 'fq_name', 'display_name', 'virtual_ip_properties', 'virtual_ip_properties_address', 'virtual_ip_properties_status', 'virtual_ip_properties_status_description', 'virtual_ip_properties_admin_state', 'virtual_ip_properties_protocol', 'virtual_ip_properties_protocol_port', 'virtual_ip_properties_connection_limit', 'virtual_ip_properties_subnet_id', 'virtual_ip_properties_persistence_cookie_name', 'virtual_ip_properties_persistence_type', 'annotations', 'annotations_key_value_pair', 'annotations_key_value_pair_key', 'annotations_key_value_pair_value', 'perms2', 'perms2_owner', 'perms2_owner_access', 'perms2_global_access', 'perms2_share', 'perms2_share_tenant', 'perms2_share_tenant_access', 'tag_refs', 'virtual_machine_interface_refs', 'loadbalancer_pool_refs', 'project'
    )

    properties_schema = {
        NAME: properties.Schema(
            properties.Schema.STRING,
            _('NAME.'),
            update_allowed=True,
            required=False,
        ),
        FQ_NAME: properties.Schema(
            properties.Schema.STRING,
            _('FQ_NAME.'),
            update_allowed=True,
            required=False,
        ),
        DISPLAY_NAME: properties.Schema(
            properties.Schema.STRING,
            _('DISPLAY_NAME.'),
            update_allowed=True,
            required=False,
        ),
        VIRTUAL_IP_PROPERTIES: properties.Schema(
            properties.Schema.MAP,
            _('VIRTUAL_IP_PROPERTIES.'),
            update_allowed=True,
            required=False,
            schema={
                VIRTUAL_IP_PROPERTIES_ADDRESS: properties.Schema(
                    properties.Schema.STRING,
                    _('VIRTUAL_IP_PROPERTIES_ADDRESS.'),
                    update_allowed=True,
                    required=False,
                ),
                VIRTUAL_IP_PROPERTIES_STATUS: properties.Schema(
                    properties.Schema.STRING,
                    _('VIRTUAL_IP_PROPERTIES_STATUS.'),
                    update_allowed=True,
                    required=False,
                ),
                VIRTUAL_IP_PROPERTIES_STATUS_DESCRIPTION: properties.Schema(
                    properties.Schema.STRING,
                    _('VIRTUAL_IP_PROPERTIES_STATUS_DESCRIPTION.'),
                    update_allowed=True,
                    required=False,
                ),
                VIRTUAL_IP_PROPERTIES_ADMIN_STATE: properties.Schema(
                    properties.Schema.BOOLEAN,
                    _('VIRTUAL_IP_PROPERTIES_ADMIN_STATE.'),
                    update_allowed=True,
                    required=False,
                ),
                VIRTUAL_IP_PROPERTIES_PROTOCOL: properties.Schema(
                    properties.Schema.STRING,
                    _('VIRTUAL_IP_PROPERTIES_PROTOCOL.'),
                    update_allowed=True,
                    required=False,
                    constraints=[
                        constraints.AllowedValues([u'HTTP', u'HTTPS', u'TCP', u'UDP', u'TERMINATED_HTTPS']),
                    ],
                ),
                VIRTUAL_IP_PROPERTIES_PROTOCOL_PORT: properties.Schema(
                    properties.Schema.INTEGER,
                    _('VIRTUAL_IP_PROPERTIES_PROTOCOL_PORT.'),
                    update_allowed=True,
                    required=False,
                ),
                VIRTUAL_IP_PROPERTIES_CONNECTION_LIMIT: properties.Schema(
                    properties.Schema.INTEGER,
                    _('VIRTUAL_IP_PROPERTIES_CONNECTION_LIMIT.'),
                    update_allowed=True,
                    required=False,
                ),
                VIRTUAL_IP_PROPERTIES_SUBNET_ID: properties.Schema(
                    properties.Schema.STRING,
                    _('VIRTUAL_IP_PROPERTIES_SUBNET_ID.'),
                    update_allowed=True,
                    required=False,
                ),
                VIRTUAL_IP_PROPERTIES_PERSISTENCE_COOKIE_NAME: properties.Schema(
                    properties.Schema.STRING,
                    _('VIRTUAL_IP_PROPERTIES_PERSISTENCE_COOKIE_NAME.'),
                    update_allowed=True,
                    required=False,
                ),
                VIRTUAL_IP_PROPERTIES_PERSISTENCE_TYPE: properties.Schema(
                    properties.Schema.STRING,
                    _('VIRTUAL_IP_PROPERTIES_PERSISTENCE_TYPE.'),
                    update_allowed=True,
                    required=False,
                    constraints=[
                        constraints.AllowedValues([u'SOURCE_IP', u'HTTP_COOKIE', u'APP_COOKIE']),
                    ],
                ),
            }
        ),
        ANNOTATIONS: properties.Schema(
            properties.Schema.MAP,
            _('ANNOTATIONS.'),
            update_allowed=True,
            required=False,
            schema={
                ANNOTATIONS_KEY_VALUE_PAIR: properties.Schema(
                    properties.Schema.LIST,
                    _('ANNOTATIONS_KEY_VALUE_PAIR.'),
                    update_allowed=True,
                    required=False,
                    schema=properties.Schema(
                        properties.Schema.MAP,
                        schema={
                            ANNOTATIONS_KEY_VALUE_PAIR_KEY: properties.Schema(
                                properties.Schema.STRING,
                                _('ANNOTATIONS_KEY_VALUE_PAIR_KEY.'),
                                update_allowed=True,
                                required=False,
                            ),
                            ANNOTATIONS_KEY_VALUE_PAIR_VALUE: properties.Schema(
                                properties.Schema.STRING,
                                _('ANNOTATIONS_KEY_VALUE_PAIR_VALUE.'),
                                update_allowed=True,
                                required=False,
                            ),
                        }
                    )
                ),
            }
        ),
        PERMS2: properties.Schema(
            properties.Schema.MAP,
            _('PERMS2.'),
            update_allowed=True,
            required=False,
            schema={
                PERMS2_OWNER: properties.Schema(
                    properties.Schema.STRING,
                    _('PERMS2_OWNER.'),
                    update_allowed=True,
                    required=False,
                ),
                PERMS2_OWNER_ACCESS: properties.Schema(
                    properties.Schema.INTEGER,
                    _('PERMS2_OWNER_ACCESS.'),
                    update_allowed=True,
                    required=False,
                    constraints=[
                        constraints.Range(0, 7),
                    ],
                ),
                PERMS2_GLOBAL_ACCESS: properties.Schema(
                    properties.Schema.INTEGER,
                    _('PERMS2_GLOBAL_ACCESS.'),
                    update_allowed=True,
                    required=False,
                    constraints=[
                        constraints.Range(0, 7),
                    ],
                ),
                PERMS2_SHARE: properties.Schema(
                    properties.Schema.LIST,
                    _('PERMS2_SHARE.'),
                    update_allowed=True,
                    required=False,
                    schema=properties.Schema(
                        properties.Schema.MAP,
                        schema={
                            PERMS2_SHARE_TENANT: properties.Schema(
                                properties.Schema.STRING,
                                _('PERMS2_SHARE_TENANT.'),
                                update_allowed=True,
                                required=False,
                            ),
                            PERMS2_SHARE_TENANT_ACCESS: properties.Schema(
                                properties.Schema.INTEGER,
                                _('PERMS2_SHARE_TENANT_ACCESS.'),
                                update_allowed=True,
                                required=False,
                                constraints=[
                                    constraints.Range(0, 7),
                                ],
                            ),
                        }
                    )
                ),
            }
        ),
        TAG_REFS: properties.Schema(
            properties.Schema.LIST,
            _('TAG_REFS.'),
            update_allowed=True,
            required=False,
        ),
        VIRTUAL_MACHINE_INTERFACE_REFS: properties.Schema(
            properties.Schema.LIST,
            _('VIRTUAL_MACHINE_INTERFACE_REFS.'),
            update_allowed=True,
            required=False,
        ),
        LOADBALANCER_POOL_REFS: properties.Schema(
            properties.Schema.LIST,
            _('LOADBALANCER_POOL_REFS.'),
            update_allowed=True,
            required=False,
        ),
        PROJECT: properties.Schema(
            properties.Schema.STRING,
            _('PROJECT.'),
            update_allowed=True,
            required=False,
        ),
    }

    attributes_schema = {
        NAME: attributes.Schema(
            _('NAME.'),
        ),
        FQ_NAME: attributes.Schema(
            _('FQ_NAME.'),
        ),
        DISPLAY_NAME: attributes.Schema(
            _('DISPLAY_NAME.'),
        ),
        VIRTUAL_IP_PROPERTIES: attributes.Schema(
            _('VIRTUAL_IP_PROPERTIES.'),
        ),
        ANNOTATIONS: attributes.Schema(
            _('ANNOTATIONS.'),
        ),
        PERMS2: attributes.Schema(
            _('PERMS2.'),
        ),
        TAG_REFS: attributes.Schema(
            _('TAG_REFS.'),
        ),
        VIRTUAL_MACHINE_INTERFACE_REFS: attributes.Schema(
            _('VIRTUAL_MACHINE_INTERFACE_REFS.'),
        ),
        LOADBALANCER_POOL_REFS: attributes.Schema(
            _('LOADBALANCER_POOL_REFS.'),
        ),
        PROJECT: attributes.Schema(
            _('PROJECT.'),
        ),
    }

    update_allowed_keys = ('Properties',)

    @contrail.set_auth_token
    def handle_create(self):
        parent_obj = None
        if parent_obj is None and self.properties.get(self.PROJECT) and self.properties.get(self.PROJECT) != 'config-root':
            try:
                parent_obj = self.vnc_lib().project_read(fq_name_str=self.properties.get(self.PROJECT))
            except vnc_api.NoIdError:
                parent_obj = self.vnc_lib().project_read(id=str(uuid.UUID(self.properties.get(self.PROJECT))))
            except:
                parent_obj = None

        if parent_obj is None and self.properties.get(self.PROJECT) != 'config-root':
            tenant_id = self.stack.context.tenant_id
            parent_obj = self.vnc_lib().project_read(id=str(uuid.UUID(tenant_id)))

        if parent_obj is None and self.properties.get(self.PROJECT) != 'config-root':
            raise Exception('Error: parent is not specified in template!')

        obj_0 = vnc_api.VirtualIp(name=self.properties[self.NAME],
            parent_obj=parent_obj)

        if self.properties.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(self.properties.get(self.DISPLAY_NAME))
        if self.properties.get(self.VIRTUAL_IP_PROPERTIES) is not None:
            obj_1 = vnc_api.VirtualIpType()
            if self.properties.get(self.VIRTUAL_IP_PROPERTIES, {}).get(self.VIRTUAL_IP_PROPERTIES_ADDRESS) is not None:
                obj_1.set_address(self.properties.get(self.VIRTUAL_IP_PROPERTIES, {}).get(self.VIRTUAL_IP_PROPERTIES_ADDRESS))
            if self.properties.get(self.VIRTUAL_IP_PROPERTIES, {}).get(self.VIRTUAL_IP_PROPERTIES_STATUS) is not None:
                obj_1.set_status(self.properties.get(self.VIRTUAL_IP_PROPERTIES, {}).get(self.VIRTUAL_IP_PROPERTIES_STATUS))
            if self.properties.get(self.VIRTUAL_IP_PROPERTIES, {}).get(self.VIRTUAL_IP_PROPERTIES_STATUS_DESCRIPTION) is not None:
                obj_1.set_status_description(self.properties.get(self.VIRTUAL_IP_PROPERTIES, {}).get(self.VIRTUAL_IP_PROPERTIES_STATUS_DESCRIPTION))
            if self.properties.get(self.VIRTUAL_IP_PROPERTIES, {}).get(self.VIRTUAL_IP_PROPERTIES_ADMIN_STATE) is not None:
                obj_1.set_admin_state(self.properties.get(self.VIRTUAL_IP_PROPERTIES, {}).get(self.VIRTUAL_IP_PROPERTIES_ADMIN_STATE))
            if self.properties.get(self.VIRTUAL_IP_PROPERTIES, {}).get(self.VIRTUAL_IP_PROPERTIES_PROTOCOL) is not None:
                obj_1.set_protocol(self.properties.get(self.VIRTUAL_IP_PROPERTIES, {}).get(self.VIRTUAL_IP_PROPERTIES_PROTOCOL))
            if self.properties.get(self.VIRTUAL_IP_PROPERTIES, {}).get(self.VIRTUAL_IP_PROPERTIES_PROTOCOL_PORT) is not None:
                obj_1.set_protocol_port(self.properties.get(self.VIRTUAL_IP_PROPERTIES, {}).get(self.VIRTUAL_IP_PROPERTIES_PROTOCOL_PORT))
            if self.properties.get(self.VIRTUAL_IP_PROPERTIES, {}).get(self.VIRTUAL_IP_PROPERTIES_CONNECTION_LIMIT) is not None:
                obj_1.set_connection_limit(self.properties.get(self.VIRTUAL_IP_PROPERTIES, {}).get(self.VIRTUAL_IP_PROPERTIES_CONNECTION_LIMIT))
            if self.properties.get(self.VIRTUAL_IP_PROPERTIES, {}).get(self.VIRTUAL_IP_PROPERTIES_SUBNET_ID) is not None:
                obj_1.set_subnet_id(self.properties.get(self.VIRTUAL_IP_PROPERTIES, {}).get(self.VIRTUAL_IP_PROPERTIES_SUBNET_ID))
            if self.properties.get(self.VIRTUAL_IP_PROPERTIES, {}).get(self.VIRTUAL_IP_PROPERTIES_PERSISTENCE_COOKIE_NAME) is not None:
                obj_1.set_persistence_cookie_name(self.properties.get(self.VIRTUAL_IP_PROPERTIES, {}).get(self.VIRTUAL_IP_PROPERTIES_PERSISTENCE_COOKIE_NAME))
            if self.properties.get(self.VIRTUAL_IP_PROPERTIES, {}).get(self.VIRTUAL_IP_PROPERTIES_PERSISTENCE_TYPE) is not None:
                obj_1.set_persistence_type(self.properties.get(self.VIRTUAL_IP_PROPERTIES, {}).get(self.VIRTUAL_IP_PROPERTIES_PERSISTENCE_TYPE))
            obj_0.set_virtual_ip_properties(obj_1)
        if self.properties.get(self.ANNOTATIONS) is not None:
            obj_1 = vnc_api.KeyValuePairs()
            if self.properties.get(self.ANNOTATIONS, {}).get(self.ANNOTATIONS_KEY_VALUE_PAIR) is not None:
                for index_1 in range(len(self.properties.get(self.ANNOTATIONS, {}).get(self.ANNOTATIONS_KEY_VALUE_PAIR))):
                    obj_2 = vnc_api.KeyValuePair()
                    if self.properties.get(self.ANNOTATIONS, {}).get(self.ANNOTATIONS_KEY_VALUE_PAIR, {})[index_1].get(self.ANNOTATIONS_KEY_VALUE_PAIR_KEY) is not None:
                        obj_2.set_key(self.properties.get(self.ANNOTATIONS, {}).get(self.ANNOTATIONS_KEY_VALUE_PAIR, {})[index_1].get(self.ANNOTATIONS_KEY_VALUE_PAIR_KEY))
                    if self.properties.get(self.ANNOTATIONS, {}).get(self.ANNOTATIONS_KEY_VALUE_PAIR, {})[index_1].get(self.ANNOTATIONS_KEY_VALUE_PAIR_VALUE) is not None:
                        obj_2.set_value(self.properties.get(self.ANNOTATIONS, {}).get(self.ANNOTATIONS_KEY_VALUE_PAIR, {})[index_1].get(self.ANNOTATIONS_KEY_VALUE_PAIR_VALUE))
                    obj_1.add_key_value_pair(obj_2)
            obj_0.set_annotations(obj_1)
        if self.properties.get(self.PERMS2) is not None:
            obj_1 = vnc_api.PermType2()
            if self.properties.get(self.PERMS2, {}).get(self.PERMS2_OWNER) is not None:
                obj_1.set_owner(self.properties.get(self.PERMS2, {}).get(self.PERMS2_OWNER))
            if self.properties.get(self.PERMS2, {}).get(self.PERMS2_OWNER_ACCESS) is not None:
                obj_1.set_owner_access(self.properties.get(self.PERMS2, {}).get(self.PERMS2_OWNER_ACCESS))
            if self.properties.get(self.PERMS2, {}).get(self.PERMS2_GLOBAL_ACCESS) is not None:
                obj_1.set_global_access(self.properties.get(self.PERMS2, {}).get(self.PERMS2_GLOBAL_ACCESS))
            if self.properties.get(self.PERMS2, {}).get(self.PERMS2_SHARE) is not None:
                for index_1 in range(len(self.properties.get(self.PERMS2, {}).get(self.PERMS2_SHARE))):
                    obj_2 = vnc_api.ShareType()
                    if self.properties.get(self.PERMS2, {}).get(self.PERMS2_SHARE, {})[index_1].get(self.PERMS2_SHARE_TENANT) is not None:
                        obj_2.set_tenant(self.properties.get(self.PERMS2, {}).get(self.PERMS2_SHARE, {})[index_1].get(self.PERMS2_SHARE_TENANT))
                    if self.properties.get(self.PERMS2, {}).get(self.PERMS2_SHARE, {})[index_1].get(self.PERMS2_SHARE_TENANT_ACCESS) is not None:
                        obj_2.set_tenant_access(self.properties.get(self.PERMS2, {}).get(self.PERMS2_SHARE, {})[index_1].get(self.PERMS2_SHARE_TENANT_ACCESS))
                    obj_1.add_share(obj_2)
            obj_0.set_perms2(obj_1)

        # reference to tag_refs
        if self.properties.get(self.TAG_REFS):
            for index_0 in range(len(self.properties.get(self.TAG_REFS))):
                try:
                    ref_obj = self.vnc_lib().tag_read(
                        id=self.properties.get(self.TAG_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().tag_read(
                        fq_name_str=self.properties.get(self.TAG_REFS)[index_0]
                    )
                except Exception as e:
                    raise Exception(_('%s') % str(e))
                obj_0.add_tag(ref_obj)

        # reference to virtual_machine_interface_refs
        if self.properties.get(self.VIRTUAL_MACHINE_INTERFACE_REFS):
            for index_0 in range(len(self.properties.get(self.VIRTUAL_MACHINE_INTERFACE_REFS))):
                try:
                    ref_obj = self.vnc_lib().virtual_machine_interface_read(
                        id=self.properties.get(self.VIRTUAL_MACHINE_INTERFACE_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().virtual_machine_interface_read(
                        fq_name_str=self.properties.get(self.VIRTUAL_MACHINE_INTERFACE_REFS)[index_0]
                    )
                except Exception as e:
                    raise Exception(_('%s') % str(e))
                obj_0.add_virtual_machine_interface(ref_obj)

        # reference to loadbalancer_pool_refs
        if self.properties.get(self.LOADBALANCER_POOL_REFS):
            for index_0 in range(len(self.properties.get(self.LOADBALANCER_POOL_REFS))):
                try:
                    ref_obj = self.vnc_lib().loadbalancer_pool_read(
                        id=self.properties.get(self.LOADBALANCER_POOL_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().loadbalancer_pool_read(
                        fq_name_str=self.properties.get(self.LOADBALANCER_POOL_REFS)[index_0]
                    )
                except Exception as e:
                    raise Exception(_('%s') % str(e))
                obj_0.add_loadbalancer_pool(ref_obj)

        try:
            obj_uuid = super(ContrailVirtualIp, self).resource_create(obj_0)
        except Exception as e:
            raise Exception(_('%s') % str(e))

        self.resource_id_set(obj_uuid)

    @contrail.set_auth_token
    def handle_update(self, json_snippet, tmpl_diff, prop_diff):
        try:
            obj_0 = self.vnc_lib().virtual_ip_read(
                id=self.resource_id
            )
        except Exception as e:
            raise Exception(_('%s') % str(e))

        if prop_diff.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(prop_diff.get(self.DISPLAY_NAME))
        if prop_diff.get(self.VIRTUAL_IP_PROPERTIES) is not None:
            obj_1 = vnc_api.VirtualIpType()
            if prop_diff.get(self.VIRTUAL_IP_PROPERTIES, {}).get(self.VIRTUAL_IP_PROPERTIES_ADDRESS) is not None:
                obj_1.set_address(prop_diff.get(self.VIRTUAL_IP_PROPERTIES, {}).get(self.VIRTUAL_IP_PROPERTIES_ADDRESS))
            if prop_diff.get(self.VIRTUAL_IP_PROPERTIES, {}).get(self.VIRTUAL_IP_PROPERTIES_STATUS) is not None:
                obj_1.set_status(prop_diff.get(self.VIRTUAL_IP_PROPERTIES, {}).get(self.VIRTUAL_IP_PROPERTIES_STATUS))
            if prop_diff.get(self.VIRTUAL_IP_PROPERTIES, {}).get(self.VIRTUAL_IP_PROPERTIES_STATUS_DESCRIPTION) is not None:
                obj_1.set_status_description(prop_diff.get(self.VIRTUAL_IP_PROPERTIES, {}).get(self.VIRTUAL_IP_PROPERTIES_STATUS_DESCRIPTION))
            if prop_diff.get(self.VIRTUAL_IP_PROPERTIES, {}).get(self.VIRTUAL_IP_PROPERTIES_ADMIN_STATE) is not None:
                obj_1.set_admin_state(prop_diff.get(self.VIRTUAL_IP_PROPERTIES, {}).get(self.VIRTUAL_IP_PROPERTIES_ADMIN_STATE))
            if prop_diff.get(self.VIRTUAL_IP_PROPERTIES, {}).get(self.VIRTUAL_IP_PROPERTIES_PROTOCOL) is not None:
                obj_1.set_protocol(prop_diff.get(self.VIRTUAL_IP_PROPERTIES, {}).get(self.VIRTUAL_IP_PROPERTIES_PROTOCOL))
            if prop_diff.get(self.VIRTUAL_IP_PROPERTIES, {}).get(self.VIRTUAL_IP_PROPERTIES_PROTOCOL_PORT) is not None:
                obj_1.set_protocol_port(prop_diff.get(self.VIRTUAL_IP_PROPERTIES, {}).get(self.VIRTUAL_IP_PROPERTIES_PROTOCOL_PORT))
            if prop_diff.get(self.VIRTUAL_IP_PROPERTIES, {}).get(self.VIRTUAL_IP_PROPERTIES_CONNECTION_LIMIT) is not None:
                obj_1.set_connection_limit(prop_diff.get(self.VIRTUAL_IP_PROPERTIES, {}).get(self.VIRTUAL_IP_PROPERTIES_CONNECTION_LIMIT))
            if prop_diff.get(self.VIRTUAL_IP_PROPERTIES, {}).get(self.VIRTUAL_IP_PROPERTIES_SUBNET_ID) is not None:
                obj_1.set_subnet_id(prop_diff.get(self.VIRTUAL_IP_PROPERTIES, {}).get(self.VIRTUAL_IP_PROPERTIES_SUBNET_ID))
            if prop_diff.get(self.VIRTUAL_IP_PROPERTIES, {}).get(self.VIRTUAL_IP_PROPERTIES_PERSISTENCE_COOKIE_NAME) is not None:
                obj_1.set_persistence_cookie_name(prop_diff.get(self.VIRTUAL_IP_PROPERTIES, {}).get(self.VIRTUAL_IP_PROPERTIES_PERSISTENCE_COOKIE_NAME))
            if prop_diff.get(self.VIRTUAL_IP_PROPERTIES, {}).get(self.VIRTUAL_IP_PROPERTIES_PERSISTENCE_TYPE) is not None:
                obj_1.set_persistence_type(prop_diff.get(self.VIRTUAL_IP_PROPERTIES, {}).get(self.VIRTUAL_IP_PROPERTIES_PERSISTENCE_TYPE))
            obj_0.set_virtual_ip_properties(obj_1)
        if prop_diff.get(self.ANNOTATIONS) is not None:
            obj_1 = vnc_api.KeyValuePairs()
            if prop_diff.get(self.ANNOTATIONS, {}).get(self.ANNOTATIONS_KEY_VALUE_PAIR) is not None:
                for index_1 in range(len(prop_diff.get(self.ANNOTATIONS, {}).get(self.ANNOTATIONS_KEY_VALUE_PAIR))):
                    obj_2 = vnc_api.KeyValuePair()
                    if prop_diff.get(self.ANNOTATIONS, {}).get(self.ANNOTATIONS_KEY_VALUE_PAIR, {})[index_1].get(self.ANNOTATIONS_KEY_VALUE_PAIR_KEY) is not None:
                        obj_2.set_key(prop_diff.get(self.ANNOTATIONS, {}).get(self.ANNOTATIONS_KEY_VALUE_PAIR, {})[index_1].get(self.ANNOTATIONS_KEY_VALUE_PAIR_KEY))
                    if prop_diff.get(self.ANNOTATIONS, {}).get(self.ANNOTATIONS_KEY_VALUE_PAIR, {})[index_1].get(self.ANNOTATIONS_KEY_VALUE_PAIR_VALUE) is not None:
                        obj_2.set_value(prop_diff.get(self.ANNOTATIONS, {}).get(self.ANNOTATIONS_KEY_VALUE_PAIR, {})[index_1].get(self.ANNOTATIONS_KEY_VALUE_PAIR_VALUE))
                    obj_1.add_key_value_pair(obj_2)
            obj_0.set_annotations(obj_1)
        if prop_diff.get(self.PERMS2) is not None:
            obj_1 = vnc_api.PermType2()
            if prop_diff.get(self.PERMS2, {}).get(self.PERMS2_OWNER) is not None:
                obj_1.set_owner(prop_diff.get(self.PERMS2, {}).get(self.PERMS2_OWNER))
            if prop_diff.get(self.PERMS2, {}).get(self.PERMS2_OWNER_ACCESS) is not None:
                obj_1.set_owner_access(prop_diff.get(self.PERMS2, {}).get(self.PERMS2_OWNER_ACCESS))
            if prop_diff.get(self.PERMS2, {}).get(self.PERMS2_GLOBAL_ACCESS) is not None:
                obj_1.set_global_access(prop_diff.get(self.PERMS2, {}).get(self.PERMS2_GLOBAL_ACCESS))
            if prop_diff.get(self.PERMS2, {}).get(self.PERMS2_SHARE) is not None:
                for index_1 in range(len(prop_diff.get(self.PERMS2, {}).get(self.PERMS2_SHARE))):
                    obj_2 = vnc_api.ShareType()
                    if prop_diff.get(self.PERMS2, {}).get(self.PERMS2_SHARE, {})[index_1].get(self.PERMS2_SHARE_TENANT) is not None:
                        obj_2.set_tenant(prop_diff.get(self.PERMS2, {}).get(self.PERMS2_SHARE, {})[index_1].get(self.PERMS2_SHARE_TENANT))
                    if prop_diff.get(self.PERMS2, {}).get(self.PERMS2_SHARE, {})[index_1].get(self.PERMS2_SHARE_TENANT_ACCESS) is not None:
                        obj_2.set_tenant_access(prop_diff.get(self.PERMS2, {}).get(self.PERMS2_SHARE, {})[index_1].get(self.PERMS2_SHARE_TENANT_ACCESS))
                    obj_1.add_share(obj_2)
            obj_0.set_perms2(obj_1)

        # reference to tag_refs
        ref_obj_list = []
        if self.TAG_REFS in prop_diff:
            for index_0 in range(len(prop_diff.get(self.TAG_REFS) or [])):
                try:
                    ref_obj = self.vnc_lib().tag_read(
                        id=prop_diff.get(self.TAG_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().tag_read(
                        fq_name_str=prop_diff.get(self.TAG_REFS)[index_0]
                    )
                except Exception as e:
                    raise Exception(_('%s') % str(e))
                ref_obj_list.append({'to':ref_obj.fq_name})

            obj_0.set_tag_list(ref_obj_list)
            # End: reference to tag_refs

        # reference to virtual_machine_interface_refs
        ref_obj_list = []
        if self.VIRTUAL_MACHINE_INTERFACE_REFS in prop_diff:
            for index_0 in range(len(prop_diff.get(self.VIRTUAL_MACHINE_INTERFACE_REFS) or [])):
                try:
                    ref_obj = self.vnc_lib().virtual_machine_interface_read(
                        id=prop_diff.get(self.VIRTUAL_MACHINE_INTERFACE_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().virtual_machine_interface_read(
                        fq_name_str=prop_diff.get(self.VIRTUAL_MACHINE_INTERFACE_REFS)[index_0]
                    )
                except Exception as e:
                    raise Exception(_('%s') % str(e))
                ref_obj_list.append({'to':ref_obj.fq_name})

            obj_0.set_virtual_machine_interface_list(ref_obj_list)
            # End: reference to virtual_machine_interface_refs

        # reference to loadbalancer_pool_refs
        ref_obj_list = []
        if self.LOADBALANCER_POOL_REFS in prop_diff:
            for index_0 in range(len(prop_diff.get(self.LOADBALANCER_POOL_REFS) or [])):
                try:
                    ref_obj = self.vnc_lib().loadbalancer_pool_read(
                        id=prop_diff.get(self.LOADBALANCER_POOL_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().loadbalancer_pool_read(
                        fq_name_str=prop_diff.get(self.LOADBALANCER_POOL_REFS)[index_0]
                    )
                except Exception as e:
                    raise Exception(_('%s') % str(e))
                ref_obj_list.append({'to':ref_obj.fq_name})

            obj_0.set_loadbalancer_pool_list(ref_obj_list)
            # End: reference to loadbalancer_pool_refs

        try:
            self.vnc_lib().virtual_ip_update(obj_0)
        except Exception as e:
            raise Exception(_('%s') % str(e))

    @contrail.set_auth_token
    def handle_delete(self):
        if self.resource_id is None:
            return

        try:
            self.vnc_lib().virtual_ip_delete(id=self.resource_id)
        except Exception as ex:
            self._ignore_not_found(ex)
            LOG.warn(_('virtual_ip %s already deleted.') % self.name)

    @contrail.set_auth_token
    def _show_resource(self):
        obj = self.vnc_lib().virtual_ip_read(id=self.resource_id)
        obj_dict = obj.serialize_to_json()
        return obj_dict


def resource_mapping():
    return {
        'OS::ContrailV2::VirtualIp': ContrailVirtualIp,
    }