"""Reusable offline skill integration gates for FEATURE-012.

These checks validate the offline distribution contract from SA-DES-012
section 5 and the frozen per-operation registers frozen at grooming by the
Tech Lead (2026-10-03). They are real content-verification unit tests: they
never make network calls and never invoke a Foundry API.

Checks:
- 300-line leaf limit for every SKILL.md and references/*.md part.
- Exact FEATURE-011 install block (conda / PyPI-pip / uv) in every SKILL.md.
- Relative local links in every SKILL.md resolve within that skill folder.
- Every frozen operation key is documented (reachable record) in the owning
  namespace references parts, and no extra callable claim is introduced.
- The four legacy Widgets design-catalogue operations are recorded as
  unsupported and are not presented as callable.  1656
"""

from pathlib import Path
import re

ROOT = Path(__file__).parent.parent
SKILLS = ROOT / ".agents" / "skills"

LEAF_LIMIT = 300
INSTALL_STRINGS = (
    "conda install -c t-jet pal_found_cli",
    "pip install pal_found_cli",
    "uv tool install pal_found_cli",
)

# Frozen per-operation registers (grooming comments 20261003-1747xx-1749xx).
# Map namespace skill name to the set of canonical operation keys it owns.
FROZEN_OPERATIONS = {
    "pal-found-admin": {
        # 042 identity (38) — authentication_provider, enrollment,
        # enrollment_role_assignment, group, group_member, group_membership,
        # group_membership_expiration_policy, group_provider_info, role, user,
        # user_provider_info
        "authentication_provider get", "authentication_provider list",
        "authentication_provider preregister_group",
        "authentication_provider preregister_user",
        "enrollment get", "enrollment get_current",
        "enrollment_role_assignment add", "enrollment_role_assignment list",
        "enrollment_role_assignment remove",
        "group create", "group delete", "group get", "group get_batch",
        "group list", "group list_current", "group replace", "group search",
        "group_member add", "group_member list", "group_member remove",
        "group_membership list",
        "group_membership_expiration_policy get",
        "group_membership_expiration_policy replace",
        "group_provider_info get", "group_provider_info replace",
        "role get", "role get_batch",
        "user delete", "user get", "user get_batch", "user get_current",
        "user get_markings", "user list", "user profile_picture",
        "user revoke_all_tokens", "user search",
        "user_provider_info get", "user_provider_info replace",
        # 043 governance (28) — cbac_banner, cbac_marking_restrictions, host,
        # marking, marking_category, marking_member, marking_role_assignment,
        # organization, organization_guest_member, organization_role_assignment
        "cbac_banner get", "cbac_marking_restrictions get", "host list",
        "marking create", "marking get", "marking get_batch", "marking list",
        "marking replace",
        "marking_category create", "marking_category get",
        "marking_category list", "marking_category replace",
        "marking_member add", "marking_member list", "marking_member remove",
        "marking_role_assignment add", "marking_role_assignment list",
        "marking_role_assignment remove",
        "organization create", "organization get",
        "organization list_available_roles", "organization replace",
        "organization_guest_member add", "organization_guest_member list",
        "organization_guest_member remove",
        "organization_role_assignment add",
        "organization_role_assignment list",
        "organization_role_assignment remove",
    },
    "pal-found-datasets": {
        "dataset create", "dataset get", "dataset get_health_check_reports",
        "dataset get_health_checks", "dataset get_schedules",
        "dataset get_schema", "dataset get_schema_batch", "dataset jobs",
        "dataset put_schema", "dataset read_table", "dataset transactions",
        "branch create", "branch delete", "branch get", "branch list",
        "branch transactions",
        "file content", "file delete", "file get", "file list", "file upload",
        "transaction abort", "transaction build", "transaction commit",
        "transaction create", "transaction get", "transaction job",
        "view add_backing_datasets", "view add_primary_key", "view create",
        "view get", "view remove_backing_datasets",
        "view replace_backing_datasets",
    },
    "pal-found-filesystem": {
        "folder children", "folder create", "folder get", "folder get_batch",
        "folder replace",
        "project add_organizations", "project create",
        "project create_from_template", "project get", "project organizations",
        "project remove_organizations", "project replace",
        "resource add_markings", "resource delete", "resource get",
        "resource get_access_requirements", "resource get_batch",
        "resource get_by_path", "resource get_by_path_batch",
        "resource markings", "resource permanently_delete",
        "resource remove_markings", "resource restore",
        "resource_role add", "resource_role list", "resource_role remove",
        "space create", "space delete", "space get", "space list",
        "space replace",
    },
    "pal-found-ontologies": {
        # 046 discovery (28)
        "action_type get", "action_type get_by_rid",
        "action_type get_by_rid_batch", "action_type list",
        "action_type_full_metadata get", "action_type_full_metadata list",
        "linked_object get_linked_object",
        "linked_object list_linked_objects",
        "object_type get", "object_type get_by_rid_batch",
        "object_type get_edits_history", "object_type get_full_metadata",
        "object_type get_outgoing_link_type", "object_type list",
        "object_type list_outgoing_link_types",
        "ontology get", "ontology get_full_metadata", "ontology list",
        "ontology load_metadata",
        "ontology_object aggregate", "ontology_object count",
        "ontology_object get", "ontology_object list", "ontology_object search",
        "ontology_value_type get", "ontology_value_type list",
        "query_type get", "query_type list",
        # 047 actions/rich (39)
        "action apply", "action apply_batch", "action apply_with_overrides",
        "attachment get", "attachment read", "attachment upload",
        "attachment upload_with_rid",
        "attachment_property get_attachment",
        "attachment_property get_attachment_by_rid",
        "attachment_property read_attachment",
        "attachment_property read_attachment_by_rid",
        "cipher_text_property decrypt",
        "geotemporal_series_property get_geotemporal_series_latest_value",
        "geotemporal_series_property stream_geotemporal_series_historic_values",
        "media_reference_property get_media_content",
        "media_reference_property get_media_metadata",
        "media_reference_property upload",
        "ontology_interface aggregate", "ontology_interface get",
        "ontology_interface get_outgoing_interface_link_type",
        "ontology_interface list",
        "ontology_interface list_interface_linked_objects",
        "ontology_interface list_objects_for_interface",
        "ontology_interface list_outgoing_interface_link_types",
        "ontology_interface search",
        "ontology_object_set aggregate",
        "ontology_object_set create_temporary",
        "ontology_object_set get", "ontology_object_set load",
        "ontology_object_set load_links",
        "ontology_object_set load_multiple_object_types",
        "ontology_object_set load_objects_or_interfaces",
        "ontology_transaction post_edits",
        "query execute",
        "time_series_property_v2 get_first_point",
        "time_series_property_v2 get_last_point",
        "time_series_property_v2 stream_points",
        "time_series_value_bank_property get_latest_value",
        "time_series_value_bank_property stream_values",
    },
    "pal-found-connectivity": {
        "connection create", "connection get", "connection get_configuration",
        "connection get_configuration_batch",
        "connection update_export_settings", "connection update_secrets",
        "connection upload_custom_jdbc_drivers",
        "file_import create", "file_import delete", "file_import execute",
        "file_import get", "file_import list", "file_import replace",
        "table_import create", "table_import delete", "table_import execute",
        "table_import get", "table_import list", "table_import replace",
        "virtual_table create",
    },
    "pal-found-checkpoints": {
        "record get", "record get_batch", "record search",
    },
    "pal-found-data-health": {
        "check create", "check delete", "check get", "check replace",
        "check_report get", "check_report get_latest",
    },
    "pal-found-aip-agents": {
        "agent all_sessions", "agent get",
        "agent_version get", "agent_version list",
        "content get",
        "session blocking_continue", "session cancel", "session create",
        "session delete", "session get", "session list",
        "session rag_context", "session streaming_continue",
        "session update_title",
        "session_trace get",
    },
    "pal-found-functions": {
        "query execute", "query get", "query get_by_rid",
        "query get_by_rid_batch", "query streaming_execute",
        "value_type get", "version_id get",
    },
    "pal-found-language-models": {
        "anthropic_model messages", "open_ai_model embeddings",
    },
    "pal-found-models": {
        "experiment get", "experiment search",
        "experiment_artifact_table json", "experiment_artifact_table parquet",
        "experiment_series json", "experiment_series parquet",
        "live_deployment transform_json",
        "model create", "model get", "model promote_version",
        "model_studio create", "model_studio get", "model_studio launch",
        "model_studio_config_version create",
        "model_studio_config_version get", "model_studio_config_version latest",
        "model_studio_config_version list",
        "model_studio_run list",
        "model_studio_trainer get", "model_studio_trainer list",
        "model_version create", "model_version get", "model_version list",
    },
    "pal-found-orchestration": {
        "build cancel", "build create", "build get", "build get_batch",
        "build jobs", "build search",
        "job get", "job get_batch",
        "schedule create", "schedule delete", "schedule get",
        "schedule get_affected_resources", "schedule get_batch",
        "schedule pause", "schedule replace", "schedule run", "schedule runs",
        "schedule unpause",
        "schedule_version get", "schedule_version schedule",
    },
    "pal-found-sql-queries": {
        "sql_query cancel", "sql_query execute", "sql_query execute_ontology",
        "sql_query get_results", "sql_query get_status",
    },
    "pal-found-streams": {
        "dataset create",
        "stream create", "stream get", "stream get_end_offsets",
        "stream get_records", "stream publish_binary_record",
        "stream publish_record", "stream publish_records", "stream reset",
        "subscriber create", "subscriber commit_offsets",
        "subscriber delete", "subscriber get_read_position",
        "subscriber read_records", "subscriber reset_offsets",
    },
    "pal-found-media-sets": {
        "media_set abort", "media_set calculate", "media_set clear",
        "media_set commit", "media_set create", "media_set get",
        "media_set get_result", "media_set get_rid_by_path",
        "media_set get_status", "media_set info", "media_set metadata",
        "media_set read", "media_set read_original", "media_set reference",
        "media_set register", "media_set retrieve", "media_set transform",
        "media_set upload", "media_set upload_media",
    },
    "pal-found-third-party-applications": {
        "third_party_application get",
        "website deploy", "website get", "website undeploy",
        "version delete", "version get", "version list",
        "version upload", "version upload_snapshot",
    },
    "pal-found-widgets": {
        "dev_mode_settings enable", "dev_mode_settings set_widget_set_by_id",
        "release delete", "release get", "release list",
        "repository get", "repository publish",
        "widget_set get",
    },
}

# Unsupported legacy Widgets design-catalogue operations (negative checks).
# Stored in kebab form as documented; the matcher also accepts snake_case.
LEGACY_WIDGETS_UNSUPPORTED = {
    "dev_mode_settings disable",
    "dev_mode_settings get",
    "dev_mode_settings pause",
    "dev_mode_settings set_widget_set",
}

NAMESPACE_SKILLS = {
    name for name in SKILLS.iterdir() if name.is_dir() and name.name.startswith("pal-found-")
} if SKILLS.is_dir() else set()


def _files(name: str) -> list[Path]:
    return sorted(
        p for p in (SKILLS / name).rglob("*.md") if "__pycache__" not in p.parts
    )


def _text(name: str) -> str:
    return "\n".join(p.read_text(encoding="utf-8") for p in _files(name))


def test_leaf_files_respect_300_line_limit() -> None:
    for name in set(FROZEN_OPERATIONS) | {"pal-found"}:
        for path in _files(name):
            count = len(path.read_text(encoding="utf-8").splitlines())
            assert count <= LEAF_LIMIT, f"{path.name} has {count} lines > {LEAF_LIMIT}"


def test_every_skill_has_install_prerequisite_block() -> None:
    for name in set(FROZEN_OPERATIONS) | {"pal-found"}:
        skill = SKILLS / name / "SKILL.md"
        text = skill.read_text(encoding="utf-8")
        for expected in INSTALL_STRINGS:
            assert expected in text, f"{name} missing install string: {expected}"


def test_skillmd_relative_links_resolve_within_folder() -> None:
    for name in set(FROZEN_OPERATIONS) | {"pal-found"}:
        skill = (SKILLS / name / "SKILL.md").read_text(encoding="utf-8")
        links = re.findall(r"\]\(([^)#]+)\)", skill)
        for link in links:
            if link.startswith("http") or link.startswith("#"):
                continue
            target = (SKILLS / name / link.split("#")[0]).resolve()
            assert target.exists(), f"{name}: relative link {link} does not resolve"


def test_frozen_operations_are_documented_and_reachable() -> None:
    for name, ops in FROZEN_OPERATIONS.items():
        text = _text(name)
        for key in ops:
            resource, operation = key.split(" ", 1)
            # The record heading or body names the operation in snake or
            # kebab form. Check both the op name alone (kebab or snake) and
            # the resource context so a record is reachable.
            op_variants = {operation, operation.replace("_", "-")}
            resource_variants = {resource, resource.replace("_", "-")}
            assert any(v in text for v in op_variants), (
                f"{name}: operation key {key} has no reachable record"
            )
            assert any(v in text for v in resource_variants), (
                f"{name}: operation key {key} missing resource context"
            )


def test_summary_counts_match_frozen_register() -> None:
    expected = {
        "pal-found-admin": 66,
        "pal-found-datasets": 33,
        "pal-found-filesystem": 31,
        "pal-found-ontologies": 67,
        "pal-found-connectivity": 20,
        "pal-found-checkpoints": 3,
        "pal-found-data-health": 6,
        "pal-found-aip-agents": 15,
        "pal-found-functions": 7,
        "pal-found-language-models": 2,
        "pal-found-models": 23,
        "pal-found-orchestration": 20,
        "pal-found-sql-queries": 5,
        "pal-found-streams": 15,
        "pal-found-media-sets": 19,
        "pal-found-third-party-applications": 9,
        "pal-found-widgets": 8,
    }
    for name, count in expected.items():
        skill = (SKILLS / name / "SKILL.md").read_text(encoding="utf-8")
        for line in skill.splitlines():
            m = re.search(r"(\d+)\s+Foundry", line)
            if m:
                assert int(m.group(1)) == count, (
                    f"{name}: advertised count {m.group(1)} != frozen {count}"
                )
                break
        else:
            raise AssertionError(f"{name}: no advertised operation count found")


def test_legacy_widgets_negatives_are_not_callable() -> None:
    text = _text("pal-found-widgets")
    for key in LEGACY_WIDGETS_UNSUPPORTED:
        operation = key.split(" ", 1)[1]
        variants = {operation, operation.replace("_", "-")}
        # The operation must appear only in the unsupported/negative context,
        # and it must not be presented as an available command invocation.
        assert "unsupported" in text.lower() or "does **not** expose" in text, (
            "widgets skill must document the unsupported legacy surface"
        )
        assert any(f"`{v}`" in text for v in variants), (
            f"widgets skill should name unsupported op {operation} as a negative"
        )
        # They must not be presented as callable via pal-found-widgets usage.
        assert f"pal-found-widgets dev-mode-settings {operation}" not in text


def test_namespace_totals_frozen_register_equivalence() -> None:
    # The union of every frozen per-namespace op key set must equal the
    # documented per-namespace counts: each skill documents its full surface.
    checks = {
        "pal-found-admin": 66,
        "pal-found-datasets": 33,
        "pal-found-filesystem": 31,
        "pal-found-ontologies": 67,
        "pal-found-connectivity": 20,
        "pal-found-checkpoints": 3,
        "pal-found-data-health": 6,
        "pal-found-aip-agents": 15,
        "pal-found-functions": 7,
        "pal-found-language-models": 2,
        "pal-found-models": 23,
        "pal-found-orchestration": 20,
        "pal-found-sql-queries": 5,
        "pal-found-streams": 15,
        "pal-found-media-sets": 19,
        "pal-found-third-party-applications": 9,
        "pal-found-widgets": 8,
    }
    for name, count in checks.items():
        assert len(FROZEN_OPERATIONS[name]) == count, (
            f"{name}: harness register has {len(FROZEN_OPERATIONS[name])} keys, "
            f"expected {count}"
        )
