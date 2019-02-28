
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


class ContrailStructuredSyslogHostnameRecord(contrail.ContrailResource):
    PROPERTIES = (
        NAME, FQ_NAME, DISPLAY_NAME, STRUCTURED_SYSLOG_HOSTADDR, STRUCTURED_SYSLOG_DEVICE, STRUCTURED_SYSLOG_LINKMAP, STRUCTURED_SYSLOG_LINKMAP_LINKS, STRUCTURED_SYSLOG_LINKMAP_LINKS_OVERLAY, STRUCTURED_SYSLOG_LINKMAP_LINKS_UNDERLAY, PERMS2, PERMS2_OWNER, PERMS2_OWNER_ACCESS, PERMS2_GLOBAL_ACCESS, PERMS2_SHARE, PERMS2_SHARE_TENANT, PERMS2_SHARE_TENANT_ACCESS, STRUCTURED_SYSLOG_LOCATION, STRUCTURED_SYSLOG_HOSTNAME_TAGS, ANNOTATIONS, ANNOTATIONS_KEY_VALUE_PAIR, ANNOTATIONS_KEY_VALUE_PAIR_KEY, ANNOTATIONS_KEY_VALUE_PAIR_VALUE, STRUCTURED_SYSLOG_TENANT, TAG_REFS, STRUCTURED_SYSLOG_CONFIG
    ) = (
        'name', 'fq_name', 'display_name', 'structured_syslog_hostaddr', 'structured_syslog_device', 'structured_syslog_linkmap', 'structured_syslog_linkmap_links', 'structured_syslog_linkmap_links_overlay', 'structured_syslog_linkmap_links_underlay', 'perms2', 'perms2_owner', 'perms2_owner_access', 'perms2_global_access', 'perms2_share', 'perms2_share_tenant', 'perms2_share_tenant_access', 'structured_syslog_location', 'structured_syslog_hostname_tags', 'annotations', 'annotations_key_value_pair', 'annotations_key_value_pair_key', 'annotations_key_value_pair_value', 'structured_syslog_tenant', 'tag_refs', 'structured_syslog_config'
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
        STRUCTURED_SYSLOG_HOSTADDR: properties.Schema(
            properties.Schema.STRING,
            _('STRUCTURED_SYSLOG_HOSTADDR.'),
            update_allowed=True,
            required=False,
        ),
        STRUCTURED_SYSLOG_DEVICE: properties.Schema(
            properties.Schema.STRING,
            _('STRUCTURED_SYSLOG_DEVICE.'),
            update_allowed=True,
            required=False,
        ),
        STRUCTURED_SYSLOG_LINKMAP: properties.Schema(
            properties.Schema.MAP,
            _('STRUCTURED_SYSLOG_LINKMAP.'),
            update_allowed=True,
            required=False,
            schema={
                STRUCTURED_SYSLOG_LINKMAP_LINKS: properties.Schema(
                    properties.Schema.LIST,
                    _('STRUCTURED_SYSLOG_LINKMAP_LINKS.'),
                    update_allowed=True,
                    required=False,
                    schema=properties.Schema(
                        properties.Schema.MAP,
                        schema={
                            STRUCTURED_SYSLOG_LINKMAP_LINKS_OVERLAY: properties.Schema(
                                properties.Schema.STRING,
                                _('STRUCTURED_SYSLOG_LINKMAP_LINKS_OVERLAY.'),
                                update_allowed=True,
                                required=False,
                            ),
                            STRUCTURED_SYSLOG_LINKMAP_LINKS_UNDERLAY: properties.Schema(
                                properties.Schema.STRING,
                                _('STRUCTURED_SYSLOG_LINKMAP_LINKS_UNDERLAY.'),
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
        STRUCTURED_SYSLOG_LOCATION: properties.Schema(
            properties.Schema.STRING,
            _('STRUCTURED_SYSLOG_LOCATION.'),
            update_allowed=True,
            required=False,
        ),
        STRUCTURED_SYSLOG_HOSTNAME_TAGS: properties.Schema(
            properties.Schema.STRING,
            _('STRUCTURED_SYSLOG_HOSTNAME_TAGS.'),
            update_allowed=True,
            required=False,
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
        STRUCTURED_SYSLOG_TENANT: properties.Schema(
            properties.Schema.STRING,
            _('STRUCTURED_SYSLOG_TENANT.'),
            update_allowed=True,
            required=False,
        ),
        TAG_REFS: properties.Schema(
            properties.Schema.LIST,
            _('TAG_REFS.'),
            update_allowed=True,
            required=False,
        ),
        STRUCTURED_SYSLOG_CONFIG: properties.Schema(
            properties.Schema.STRING,
            _('STRUCTURED_SYSLOG_CONFIG.'),
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
        STRUCTURED_SYSLOG_HOSTADDR: attributes.Schema(
            _('STRUCTURED_SYSLOG_HOSTADDR.'),
        ),
        STRUCTURED_SYSLOG_DEVICE: attributes.Schema(
            _('STRUCTURED_SYSLOG_DEVICE.'),
        ),
        STRUCTURED_SYSLOG_LINKMAP: attributes.Schema(
            _('STRUCTURED_SYSLOG_LINKMAP.'),
        ),
        PERMS2: attributes.Schema(
            _('PERMS2.'),
        ),
        STRUCTURED_SYSLOG_LOCATION: attributes.Schema(
            _('STRUCTURED_SYSLOG_LOCATION.'),
        ),
        STRUCTURED_SYSLOG_HOSTNAME_TAGS: attributes.Schema(
            _('STRUCTURED_SYSLOG_HOSTNAME_TAGS.'),
        ),
        ANNOTATIONS: attributes.Schema(
            _('ANNOTATIONS.'),
        ),
        STRUCTURED_SYSLOG_TENANT: attributes.Schema(
            _('STRUCTURED_SYSLOG_TENANT.'),
        ),
        TAG_REFS: attributes.Schema(
            _('TAG_REFS.'),
        ),
        STRUCTURED_SYSLOG_CONFIG: attributes.Schema(
            _('STRUCTURED_SYSLOG_CONFIG.'),
        ),
    }

    update_allowed_keys = ('Properties',)

    @contrail.set_auth_token
    def handle_create(self):
        parent_obj = None
        if parent_obj is None and self.properties.get(self.STRUCTURED_SYSLOG_CONFIG) and self.properties.get(self.STRUCTURED_SYSLOG_CONFIG) != 'config-root':
            try:
                parent_obj = self.vnc_lib().structured_syslog_config_read(fq_name_str=self.properties.get(self.STRUCTURED_SYSLOG_CONFIG))
            except vnc_api.NoIdError:
                parent_obj = self.vnc_lib().structured_syslog_config_read(id=str(uuid.UUID(self.properties.get(self.STRUCTURED_SYSLOG_CONFIG))))
            except:
                parent_obj = None

        if parent_obj is None and self.properties.get(self.STRUCTURED_SYSLOG_CONFIG) != 'config-root':
            raise Exception('Error: parent is not specified in template!')

        obj_0 = vnc_api.StructuredSyslogHostnameRecord(name=self.properties[self.NAME],
            parent_obj=parent_obj)

        if self.properties.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(self.properties.get(self.DISPLAY_NAME))
        if self.properties.get(self.STRUCTURED_SYSLOG_HOSTADDR) is not None:
            obj_0.set_structured_syslog_hostaddr(self.properties.get(self.STRUCTURED_SYSLOG_HOSTADDR))
        if self.properties.get(self.STRUCTURED_SYSLOG_DEVICE) is not None:
            obj_0.set_structured_syslog_device(self.properties.get(self.STRUCTURED_SYSLOG_DEVICE))
        if self.properties.get(self.STRUCTURED_SYSLOG_LINKMAP) is not None:
            obj_1 = vnc_api.StructuredSyslogLinkmap()
            if self.properties.get(self.STRUCTURED_SYSLOG_LINKMAP, {}).get(self.STRUCTURED_SYSLOG_LINKMAP_LINKS) is not None:
                for index_1 in range(len(self.properties.get(self.STRUCTURED_SYSLOG_LINKMAP, {}).get(self.STRUCTURED_SYSLOG_LINKMAP_LINKS))):
                    obj_2 = vnc_api.StructuredSyslogLinkType()
                    if self.properties.get(self.STRUCTURED_SYSLOG_LINKMAP, {}).get(self.STRUCTURED_SYSLOG_LINKMAP_LINKS, {})[index_1].get(self.STRUCTURED_SYSLOG_LINKMAP_LINKS_OVERLAY) is not None:
                        obj_2.set_overlay(self.properties.get(self.STRUCTURED_SYSLOG_LINKMAP, {}).get(self.STRUCTURED_SYSLOG_LINKMAP_LINKS, {})[index_1].get(self.STRUCTURED_SYSLOG_LINKMAP_LINKS_OVERLAY))
                    if self.properties.get(self.STRUCTURED_SYSLOG_LINKMAP, {}).get(self.STRUCTURED_SYSLOG_LINKMAP_LINKS, {})[index_1].get(self.STRUCTURED_SYSLOG_LINKMAP_LINKS_UNDERLAY) is not None:
                        obj_2.set_underlay(self.properties.get(self.STRUCTURED_SYSLOG_LINKMAP, {}).get(self.STRUCTURED_SYSLOG_LINKMAP_LINKS, {})[index_1].get(self.STRUCTURED_SYSLOG_LINKMAP_LINKS_UNDERLAY))
                    obj_1.add_links(obj_2)
            obj_0.set_structured_syslog_linkmap(obj_1)
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
        if self.properties.get(self.STRUCTURED_SYSLOG_LOCATION) is not None:
            obj_0.set_structured_syslog_location(self.properties.get(self.STRUCTURED_SYSLOG_LOCATION))
        if self.properties.get(self.STRUCTURED_SYSLOG_HOSTNAME_TAGS) is not None:
            obj_0.set_structured_syslog_hostname_tags(self.properties.get(self.STRUCTURED_SYSLOG_HOSTNAME_TAGS))
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
        if self.properties.get(self.STRUCTURED_SYSLOG_TENANT) is not None:
            obj_0.set_structured_syslog_tenant(self.properties.get(self.STRUCTURED_SYSLOG_TENANT))

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

        try:
            obj_uuid = super(ContrailStructuredSyslogHostnameRecord, self).resource_create(obj_0)
        except Exception as e:
            raise Exception(_('%s') % str(e))

        self.resource_id_set(obj_uuid)

    @contrail.set_auth_token
    def handle_update(self, json_snippet, tmpl_diff, prop_diff):
        try:
            obj_0 = self.vnc_lib().structured_syslog_hostname_record_read(
                id=self.resource_id
            )
        except Exception as e:
            raise Exception(_('%s') % str(e))

        if prop_diff.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(prop_diff.get(self.DISPLAY_NAME))
        if prop_diff.get(self.STRUCTURED_SYSLOG_HOSTADDR) is not None:
            obj_0.set_structured_syslog_hostaddr(prop_diff.get(self.STRUCTURED_SYSLOG_HOSTADDR))
        if prop_diff.get(self.STRUCTURED_SYSLOG_DEVICE) is not None:
            obj_0.set_structured_syslog_device(prop_diff.get(self.STRUCTURED_SYSLOG_DEVICE))
        if prop_diff.get(self.STRUCTURED_SYSLOG_LINKMAP) is not None:
            obj_1 = vnc_api.StructuredSyslogLinkmap()
            if prop_diff.get(self.STRUCTURED_SYSLOG_LINKMAP, {}).get(self.STRUCTURED_SYSLOG_LINKMAP_LINKS) is not None:
                for index_1 in range(len(prop_diff.get(self.STRUCTURED_SYSLOG_LINKMAP, {}).get(self.STRUCTURED_SYSLOG_LINKMAP_LINKS))):
                    obj_2 = vnc_api.StructuredSyslogLinkType()
                    if prop_diff.get(self.STRUCTURED_SYSLOG_LINKMAP, {}).get(self.STRUCTURED_SYSLOG_LINKMAP_LINKS, {})[index_1].get(self.STRUCTURED_SYSLOG_LINKMAP_LINKS_OVERLAY) is not None:
                        obj_2.set_overlay(prop_diff.get(self.STRUCTURED_SYSLOG_LINKMAP, {}).get(self.STRUCTURED_SYSLOG_LINKMAP_LINKS, {})[index_1].get(self.STRUCTURED_SYSLOG_LINKMAP_LINKS_OVERLAY))
                    if prop_diff.get(self.STRUCTURED_SYSLOG_LINKMAP, {}).get(self.STRUCTURED_SYSLOG_LINKMAP_LINKS, {})[index_1].get(self.STRUCTURED_SYSLOG_LINKMAP_LINKS_UNDERLAY) is not None:
                        obj_2.set_underlay(prop_diff.get(self.STRUCTURED_SYSLOG_LINKMAP, {}).get(self.STRUCTURED_SYSLOG_LINKMAP_LINKS, {})[index_1].get(self.STRUCTURED_SYSLOG_LINKMAP_LINKS_UNDERLAY))
                    obj_1.add_links(obj_2)
            obj_0.set_structured_syslog_linkmap(obj_1)
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
        if prop_diff.get(self.STRUCTURED_SYSLOG_LOCATION) is not None:
            obj_0.set_structured_syslog_location(prop_diff.get(self.STRUCTURED_SYSLOG_LOCATION))
        if prop_diff.get(self.STRUCTURED_SYSLOG_HOSTNAME_TAGS) is not None:
            obj_0.set_structured_syslog_hostname_tags(prop_diff.get(self.STRUCTURED_SYSLOG_HOSTNAME_TAGS))
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
        if prop_diff.get(self.STRUCTURED_SYSLOG_TENANT) is not None:
            obj_0.set_structured_syslog_tenant(prop_diff.get(self.STRUCTURED_SYSLOG_TENANT))

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

        try:
            self.vnc_lib().structured_syslog_hostname_record_update(obj_0)
        except Exception as e:
            raise Exception(_('%s') % str(e))

    @contrail.set_auth_token
    def handle_delete(self):
        if self.resource_id is None:
            return

        try:
            self.vnc_lib().structured_syslog_hostname_record_delete(id=self.resource_id)
        except Exception as ex:
            self._ignore_not_found(ex)
            LOG.warn(_('structured_syslog_hostname_record %s already deleted.') % self.name)

    @contrail.set_auth_token
    def _show_resource(self):
        obj = self.vnc_lib().structured_syslog_hostname_record_read(id=self.resource_id)
        obj_dict = obj.serialize_to_json()
        return obj_dict


def resource_mapping():
    return {
        'OS::ContrailV2::StructuredSyslogHostnameRecord': ContrailStructuredSyslogHostnameRecord,
    }