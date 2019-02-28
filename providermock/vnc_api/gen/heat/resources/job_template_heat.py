
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


class ContrailJobTemplate(contrail.ContrailResource):
    PROPERTIES = (
        NAME, FQ_NAME, JOB_TEMPLATE_CONCURRENCY_LEVEL, DISPLAY_NAME, JOB_TEMPLATE_OUTPUT_SCHEMA, JOB_TEMPLATE_PLAYBOOKS, JOB_TEMPLATE_PLAYBOOKS_PLAYBOOK_INFO, JOB_TEMPLATE_PLAYBOOKS_PLAYBOOK_INFO_PLAYBOOK_URI, JOB_TEMPLATE_PLAYBOOKS_PLAYBOOK_INFO_VENDOR, JOB_TEMPLATE_PLAYBOOKS_PLAYBOOK_INFO_DEVICE_FAMILY, JOB_TEMPLATE_PLAYBOOKS_PLAYBOOK_INFO_JOB_COMPLETION_WEIGHTAGE, JOB_TEMPLATE_OUTPUT_UI_SCHEMA, JOB_TEMPLATE_MULTI_DEVICE_JOB, PERMS2, PERMS2_OWNER, PERMS2_OWNER_ACCESS, PERMS2_GLOBAL_ACCESS, PERMS2_SHARE, PERMS2_SHARE_TENANT, PERMS2_SHARE_TENANT_ACCESS, JOB_TEMPLATE_TYPE, JOB_TEMPLATE_INPUT_UI_SCHEMA, JOB_TEMPLATE_DESCRIPTION, JOB_TEMPLATE_SYNCHRONOUS_JOB, ANNOTATIONS, ANNOTATIONS_KEY_VALUE_PAIR, ANNOTATIONS_KEY_VALUE_PAIR_KEY, ANNOTATIONS_KEY_VALUE_PAIR_VALUE, JOB_TEMPLATE_INPUT_SCHEMA, TAG_REFS, GLOBAL_SYSTEM_CONFIG
    ) = (
        'name', 'fq_name', 'job_template_concurrency_level', 'display_name', 'job_template_output_schema', 'job_template_playbooks', 'job_template_playbooks_playbook_info', 'job_template_playbooks_playbook_info_playbook_uri', 'job_template_playbooks_playbook_info_vendor', 'job_template_playbooks_playbook_info_device_family', 'job_template_playbooks_playbook_info_job_completion_weightage', 'job_template_output_ui_schema', 'job_template_multi_device_job', 'perms2', 'perms2_owner', 'perms2_owner_access', 'perms2_global_access', 'perms2_share', 'perms2_share_tenant', 'perms2_share_tenant_access', 'job_template_type', 'job_template_input_ui_schema', 'job_template_description', 'job_template_synchronous_job', 'annotations', 'annotations_key_value_pair', 'annotations_key_value_pair_key', 'annotations_key_value_pair_value', 'job_template_input_schema', 'tag_refs', 'global_system_config'
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
        JOB_TEMPLATE_CONCURRENCY_LEVEL: properties.Schema(
            properties.Schema.STRING,
            _('JOB_TEMPLATE_CONCURRENCY_LEVEL.'),
            update_allowed=True,
            required=False,
        ),
        DISPLAY_NAME: properties.Schema(
            properties.Schema.STRING,
            _('DISPLAY_NAME.'),
            update_allowed=True,
            required=False,
        ),
        JOB_TEMPLATE_OUTPUT_SCHEMA: properties.Schema(
            properties.Schema.STRING,
            _('JOB_TEMPLATE_OUTPUT_SCHEMA.'),
            update_allowed=True,
            required=False,
        ),
        JOB_TEMPLATE_PLAYBOOKS: properties.Schema(
            properties.Schema.MAP,
            _('JOB_TEMPLATE_PLAYBOOKS.'),
            update_allowed=True,
            required=False,
            schema={
                JOB_TEMPLATE_PLAYBOOKS_PLAYBOOK_INFO: properties.Schema(
                    properties.Schema.LIST,
                    _('JOB_TEMPLATE_PLAYBOOKS_PLAYBOOK_INFO.'),
                    update_allowed=True,
                    required=False,
                    schema=properties.Schema(
                        properties.Schema.MAP,
                        schema={
                            JOB_TEMPLATE_PLAYBOOKS_PLAYBOOK_INFO_PLAYBOOK_URI: properties.Schema(
                                properties.Schema.STRING,
                                _('JOB_TEMPLATE_PLAYBOOKS_PLAYBOOK_INFO_PLAYBOOK_URI.'),
                                update_allowed=True,
                                required=False,
                            ),
                            JOB_TEMPLATE_PLAYBOOKS_PLAYBOOK_INFO_VENDOR: properties.Schema(
                                properties.Schema.STRING,
                                _('JOB_TEMPLATE_PLAYBOOKS_PLAYBOOK_INFO_VENDOR.'),
                                update_allowed=True,
                                required=False,
                            ),
                            JOB_TEMPLATE_PLAYBOOKS_PLAYBOOK_INFO_DEVICE_FAMILY: properties.Schema(
                                properties.Schema.STRING,
                                _('JOB_TEMPLATE_PLAYBOOKS_PLAYBOOK_INFO_DEVICE_FAMILY.'),
                                update_allowed=True,
                                required=False,
                            ),
                            JOB_TEMPLATE_PLAYBOOKS_PLAYBOOK_INFO_JOB_COMPLETION_WEIGHTAGE: properties.Schema(
                                properties.Schema.INTEGER,
                                _('JOB_TEMPLATE_PLAYBOOKS_PLAYBOOK_INFO_JOB_COMPLETION_WEIGHTAGE.'),
                                update_allowed=True,
                                required=False,
                            ),
                        }
                    )
                ),
            }
        ),
        JOB_TEMPLATE_OUTPUT_UI_SCHEMA: properties.Schema(
            properties.Schema.STRING,
            _('JOB_TEMPLATE_OUTPUT_UI_SCHEMA.'),
            update_allowed=True,
            required=False,
        ),
        JOB_TEMPLATE_MULTI_DEVICE_JOB: properties.Schema(
            properties.Schema.BOOLEAN,
            _('JOB_TEMPLATE_MULTI_DEVICE_JOB.'),
            update_allowed=True,
            required=False,
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
        JOB_TEMPLATE_TYPE: properties.Schema(
            properties.Schema.STRING,
            _('JOB_TEMPLATE_TYPE.'),
            update_allowed=True,
            required=False,
        ),
        JOB_TEMPLATE_INPUT_UI_SCHEMA: properties.Schema(
            properties.Schema.STRING,
            _('JOB_TEMPLATE_INPUT_UI_SCHEMA.'),
            update_allowed=True,
            required=False,
        ),
        JOB_TEMPLATE_DESCRIPTION: properties.Schema(
            properties.Schema.STRING,
            _('JOB_TEMPLATE_DESCRIPTION.'),
            update_allowed=True,
            required=False,
        ),
        JOB_TEMPLATE_SYNCHRONOUS_JOB: properties.Schema(
            properties.Schema.BOOLEAN,
            _('JOB_TEMPLATE_SYNCHRONOUS_JOB.'),
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
        JOB_TEMPLATE_INPUT_SCHEMA: properties.Schema(
            properties.Schema.STRING,
            _('JOB_TEMPLATE_INPUT_SCHEMA.'),
            update_allowed=True,
            required=False,
        ),
        TAG_REFS: properties.Schema(
            properties.Schema.LIST,
            _('TAG_REFS.'),
            update_allowed=True,
            required=False,
        ),
        GLOBAL_SYSTEM_CONFIG: properties.Schema(
            properties.Schema.STRING,
            _('GLOBAL_SYSTEM_CONFIG.'),
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
        JOB_TEMPLATE_CONCURRENCY_LEVEL: attributes.Schema(
            _('JOB_TEMPLATE_CONCURRENCY_LEVEL.'),
        ),
        DISPLAY_NAME: attributes.Schema(
            _('DISPLAY_NAME.'),
        ),
        JOB_TEMPLATE_OUTPUT_SCHEMA: attributes.Schema(
            _('JOB_TEMPLATE_OUTPUT_SCHEMA.'),
        ),
        JOB_TEMPLATE_PLAYBOOKS: attributes.Schema(
            _('JOB_TEMPLATE_PLAYBOOKS.'),
        ),
        JOB_TEMPLATE_OUTPUT_UI_SCHEMA: attributes.Schema(
            _('JOB_TEMPLATE_OUTPUT_UI_SCHEMA.'),
        ),
        JOB_TEMPLATE_MULTI_DEVICE_JOB: attributes.Schema(
            _('JOB_TEMPLATE_MULTI_DEVICE_JOB.'),
        ),
        PERMS2: attributes.Schema(
            _('PERMS2.'),
        ),
        JOB_TEMPLATE_TYPE: attributes.Schema(
            _('JOB_TEMPLATE_TYPE.'),
        ),
        JOB_TEMPLATE_INPUT_UI_SCHEMA: attributes.Schema(
            _('JOB_TEMPLATE_INPUT_UI_SCHEMA.'),
        ),
        JOB_TEMPLATE_DESCRIPTION: attributes.Schema(
            _('JOB_TEMPLATE_DESCRIPTION.'),
        ),
        JOB_TEMPLATE_SYNCHRONOUS_JOB: attributes.Schema(
            _('JOB_TEMPLATE_SYNCHRONOUS_JOB.'),
        ),
        ANNOTATIONS: attributes.Schema(
            _('ANNOTATIONS.'),
        ),
        JOB_TEMPLATE_INPUT_SCHEMA: attributes.Schema(
            _('JOB_TEMPLATE_INPUT_SCHEMA.'),
        ),
        TAG_REFS: attributes.Schema(
            _('TAG_REFS.'),
        ),
        GLOBAL_SYSTEM_CONFIG: attributes.Schema(
            _('GLOBAL_SYSTEM_CONFIG.'),
        ),
    }

    update_allowed_keys = ('Properties',)

    @contrail.set_auth_token
    def handle_create(self):
        parent_obj = None
        if parent_obj is None and self.properties.get(self.GLOBAL_SYSTEM_CONFIG) and self.properties.get(self.GLOBAL_SYSTEM_CONFIG) != 'config-root':
            try:
                parent_obj = self.vnc_lib().global_system_config_read(fq_name_str=self.properties.get(self.GLOBAL_SYSTEM_CONFIG))
            except vnc_api.NoIdError:
                parent_obj = self.vnc_lib().global_system_config_read(id=str(uuid.UUID(self.properties.get(self.GLOBAL_SYSTEM_CONFIG))))
            except:
                parent_obj = None

        if parent_obj is None and self.properties.get(self.GLOBAL_SYSTEM_CONFIG) != 'config-root':
            raise Exception('Error: parent is not specified in template!')

        obj_0 = vnc_api.JobTemplate(name=self.properties[self.NAME],
            parent_obj=parent_obj)

        if self.properties.get(self.JOB_TEMPLATE_CONCURRENCY_LEVEL) is not None:
            obj_0.set_job_template_concurrency_level(self.properties.get(self.JOB_TEMPLATE_CONCURRENCY_LEVEL))
        if self.properties.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(self.properties.get(self.DISPLAY_NAME))
        if self.properties.get(self.JOB_TEMPLATE_OUTPUT_SCHEMA) is not None:
            obj_0.set_job_template_output_schema(self.properties.get(self.JOB_TEMPLATE_OUTPUT_SCHEMA))
        if self.properties.get(self.JOB_TEMPLATE_PLAYBOOKS) is not None:
            obj_1 = vnc_api.PlaybookInfoListType()
            if self.properties.get(self.JOB_TEMPLATE_PLAYBOOKS, {}).get(self.JOB_TEMPLATE_PLAYBOOKS_PLAYBOOK_INFO) is not None:
                for index_1 in range(len(self.properties.get(self.JOB_TEMPLATE_PLAYBOOKS, {}).get(self.JOB_TEMPLATE_PLAYBOOKS_PLAYBOOK_INFO))):
                    obj_2 = vnc_api.PlaybookInfoType()
                    if self.properties.get(self.JOB_TEMPLATE_PLAYBOOKS, {}).get(self.JOB_TEMPLATE_PLAYBOOKS_PLAYBOOK_INFO, {})[index_1].get(self.JOB_TEMPLATE_PLAYBOOKS_PLAYBOOK_INFO_PLAYBOOK_URI) is not None:
                        obj_2.set_playbook_uri(self.properties.get(self.JOB_TEMPLATE_PLAYBOOKS, {}).get(self.JOB_TEMPLATE_PLAYBOOKS_PLAYBOOK_INFO, {})[index_1].get(self.JOB_TEMPLATE_PLAYBOOKS_PLAYBOOK_INFO_PLAYBOOK_URI))
                    if self.properties.get(self.JOB_TEMPLATE_PLAYBOOKS, {}).get(self.JOB_TEMPLATE_PLAYBOOKS_PLAYBOOK_INFO, {})[index_1].get(self.JOB_TEMPLATE_PLAYBOOKS_PLAYBOOK_INFO_VENDOR) is not None:
                        obj_2.set_vendor(self.properties.get(self.JOB_TEMPLATE_PLAYBOOKS, {}).get(self.JOB_TEMPLATE_PLAYBOOKS_PLAYBOOK_INFO, {})[index_1].get(self.JOB_TEMPLATE_PLAYBOOKS_PLAYBOOK_INFO_VENDOR))
                    if self.properties.get(self.JOB_TEMPLATE_PLAYBOOKS, {}).get(self.JOB_TEMPLATE_PLAYBOOKS_PLAYBOOK_INFO, {})[index_1].get(self.JOB_TEMPLATE_PLAYBOOKS_PLAYBOOK_INFO_DEVICE_FAMILY) is not None:
                        obj_2.set_device_family(self.properties.get(self.JOB_TEMPLATE_PLAYBOOKS, {}).get(self.JOB_TEMPLATE_PLAYBOOKS_PLAYBOOK_INFO, {})[index_1].get(self.JOB_TEMPLATE_PLAYBOOKS_PLAYBOOK_INFO_DEVICE_FAMILY))
                    if self.properties.get(self.JOB_TEMPLATE_PLAYBOOKS, {}).get(self.JOB_TEMPLATE_PLAYBOOKS_PLAYBOOK_INFO, {})[index_1].get(self.JOB_TEMPLATE_PLAYBOOKS_PLAYBOOK_INFO_JOB_COMPLETION_WEIGHTAGE) is not None:
                        obj_2.set_job_completion_weightage(self.properties.get(self.JOB_TEMPLATE_PLAYBOOKS, {}).get(self.JOB_TEMPLATE_PLAYBOOKS_PLAYBOOK_INFO, {})[index_1].get(self.JOB_TEMPLATE_PLAYBOOKS_PLAYBOOK_INFO_JOB_COMPLETION_WEIGHTAGE))
                    obj_1.add_playbook_info(obj_2)
            obj_0.set_job_template_playbooks(obj_1)
        if self.properties.get(self.JOB_TEMPLATE_OUTPUT_UI_SCHEMA) is not None:
            obj_0.set_job_template_output_ui_schema(self.properties.get(self.JOB_TEMPLATE_OUTPUT_UI_SCHEMA))
        if self.properties.get(self.JOB_TEMPLATE_MULTI_DEVICE_JOB) is not None:
            obj_0.set_job_template_multi_device_job(self.properties.get(self.JOB_TEMPLATE_MULTI_DEVICE_JOB))
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
        if self.properties.get(self.JOB_TEMPLATE_TYPE) is not None:
            obj_0.set_job_template_type(self.properties.get(self.JOB_TEMPLATE_TYPE))
        if self.properties.get(self.JOB_TEMPLATE_INPUT_UI_SCHEMA) is not None:
            obj_0.set_job_template_input_ui_schema(self.properties.get(self.JOB_TEMPLATE_INPUT_UI_SCHEMA))
        if self.properties.get(self.JOB_TEMPLATE_DESCRIPTION) is not None:
            obj_0.set_job_template_description(self.properties.get(self.JOB_TEMPLATE_DESCRIPTION))
        if self.properties.get(self.JOB_TEMPLATE_SYNCHRONOUS_JOB) is not None:
            obj_0.set_job_template_synchronous_job(self.properties.get(self.JOB_TEMPLATE_SYNCHRONOUS_JOB))
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
        if self.properties.get(self.JOB_TEMPLATE_INPUT_SCHEMA) is not None:
            obj_0.set_job_template_input_schema(self.properties.get(self.JOB_TEMPLATE_INPUT_SCHEMA))

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
            obj_uuid = super(ContrailJobTemplate, self).resource_create(obj_0)
        except Exception as e:
            raise Exception(_('%s') % str(e))

        self.resource_id_set(obj_uuid)

    @contrail.set_auth_token
    def handle_update(self, json_snippet, tmpl_diff, prop_diff):
        try:
            obj_0 = self.vnc_lib().job_template_read(
                id=self.resource_id
            )
        except Exception as e:
            raise Exception(_('%s') % str(e))

        if prop_diff.get(self.JOB_TEMPLATE_CONCURRENCY_LEVEL) is not None:
            obj_0.set_job_template_concurrency_level(prop_diff.get(self.JOB_TEMPLATE_CONCURRENCY_LEVEL))
        if prop_diff.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(prop_diff.get(self.DISPLAY_NAME))
        if prop_diff.get(self.JOB_TEMPLATE_OUTPUT_SCHEMA) is not None:
            obj_0.set_job_template_output_schema(prop_diff.get(self.JOB_TEMPLATE_OUTPUT_SCHEMA))
        if prop_diff.get(self.JOB_TEMPLATE_PLAYBOOKS) is not None:
            obj_1 = vnc_api.PlaybookInfoListType()
            if prop_diff.get(self.JOB_TEMPLATE_PLAYBOOKS, {}).get(self.JOB_TEMPLATE_PLAYBOOKS_PLAYBOOK_INFO) is not None:
                for index_1 in range(len(prop_diff.get(self.JOB_TEMPLATE_PLAYBOOKS, {}).get(self.JOB_TEMPLATE_PLAYBOOKS_PLAYBOOK_INFO))):
                    obj_2 = vnc_api.PlaybookInfoType()
                    if prop_diff.get(self.JOB_TEMPLATE_PLAYBOOKS, {}).get(self.JOB_TEMPLATE_PLAYBOOKS_PLAYBOOK_INFO, {})[index_1].get(self.JOB_TEMPLATE_PLAYBOOKS_PLAYBOOK_INFO_PLAYBOOK_URI) is not None:
                        obj_2.set_playbook_uri(prop_diff.get(self.JOB_TEMPLATE_PLAYBOOKS, {}).get(self.JOB_TEMPLATE_PLAYBOOKS_PLAYBOOK_INFO, {})[index_1].get(self.JOB_TEMPLATE_PLAYBOOKS_PLAYBOOK_INFO_PLAYBOOK_URI))
                    if prop_diff.get(self.JOB_TEMPLATE_PLAYBOOKS, {}).get(self.JOB_TEMPLATE_PLAYBOOKS_PLAYBOOK_INFO, {})[index_1].get(self.JOB_TEMPLATE_PLAYBOOKS_PLAYBOOK_INFO_VENDOR) is not None:
                        obj_2.set_vendor(prop_diff.get(self.JOB_TEMPLATE_PLAYBOOKS, {}).get(self.JOB_TEMPLATE_PLAYBOOKS_PLAYBOOK_INFO, {})[index_1].get(self.JOB_TEMPLATE_PLAYBOOKS_PLAYBOOK_INFO_VENDOR))
                    if prop_diff.get(self.JOB_TEMPLATE_PLAYBOOKS, {}).get(self.JOB_TEMPLATE_PLAYBOOKS_PLAYBOOK_INFO, {})[index_1].get(self.JOB_TEMPLATE_PLAYBOOKS_PLAYBOOK_INFO_DEVICE_FAMILY) is not None:
                        obj_2.set_device_family(prop_diff.get(self.JOB_TEMPLATE_PLAYBOOKS, {}).get(self.JOB_TEMPLATE_PLAYBOOKS_PLAYBOOK_INFO, {})[index_1].get(self.JOB_TEMPLATE_PLAYBOOKS_PLAYBOOK_INFO_DEVICE_FAMILY))
                    if prop_diff.get(self.JOB_TEMPLATE_PLAYBOOKS, {}).get(self.JOB_TEMPLATE_PLAYBOOKS_PLAYBOOK_INFO, {})[index_1].get(self.JOB_TEMPLATE_PLAYBOOKS_PLAYBOOK_INFO_JOB_COMPLETION_WEIGHTAGE) is not None:
                        obj_2.set_job_completion_weightage(prop_diff.get(self.JOB_TEMPLATE_PLAYBOOKS, {}).get(self.JOB_TEMPLATE_PLAYBOOKS_PLAYBOOK_INFO, {})[index_1].get(self.JOB_TEMPLATE_PLAYBOOKS_PLAYBOOK_INFO_JOB_COMPLETION_WEIGHTAGE))
                    obj_1.add_playbook_info(obj_2)
            obj_0.set_job_template_playbooks(obj_1)
        if prop_diff.get(self.JOB_TEMPLATE_OUTPUT_UI_SCHEMA) is not None:
            obj_0.set_job_template_output_ui_schema(prop_diff.get(self.JOB_TEMPLATE_OUTPUT_UI_SCHEMA))
        if prop_diff.get(self.JOB_TEMPLATE_MULTI_DEVICE_JOB) is not None:
            obj_0.set_job_template_multi_device_job(prop_diff.get(self.JOB_TEMPLATE_MULTI_DEVICE_JOB))
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
        if prop_diff.get(self.JOB_TEMPLATE_TYPE) is not None:
            obj_0.set_job_template_type(prop_diff.get(self.JOB_TEMPLATE_TYPE))
        if prop_diff.get(self.JOB_TEMPLATE_INPUT_UI_SCHEMA) is not None:
            obj_0.set_job_template_input_ui_schema(prop_diff.get(self.JOB_TEMPLATE_INPUT_UI_SCHEMA))
        if prop_diff.get(self.JOB_TEMPLATE_DESCRIPTION) is not None:
            obj_0.set_job_template_description(prop_diff.get(self.JOB_TEMPLATE_DESCRIPTION))
        if prop_diff.get(self.JOB_TEMPLATE_SYNCHRONOUS_JOB) is not None:
            obj_0.set_job_template_synchronous_job(prop_diff.get(self.JOB_TEMPLATE_SYNCHRONOUS_JOB))
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
        if prop_diff.get(self.JOB_TEMPLATE_INPUT_SCHEMA) is not None:
            obj_0.set_job_template_input_schema(prop_diff.get(self.JOB_TEMPLATE_INPUT_SCHEMA))

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
            self.vnc_lib().job_template_update(obj_0)
        except Exception as e:
            raise Exception(_('%s') % str(e))

    @contrail.set_auth_token
    def handle_delete(self):
        if self.resource_id is None:
            return

        try:
            self.vnc_lib().job_template_delete(id=self.resource_id)
        except Exception as ex:
            self._ignore_not_found(ex)
            LOG.warn(_('job_template %s already deleted.') % self.name)

    @contrail.set_auth_token
    def _show_resource(self):
        obj = self.vnc_lib().job_template_read(id=self.resource_id)
        obj_dict = obj.serialize_to_json()
        return obj_dict


def resource_mapping():
    return {
        'OS::ContrailV2::JobTemplate': ContrailJobTemplate,
    }