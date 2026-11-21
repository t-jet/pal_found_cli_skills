Feature: REST079 source-bound Ontology schema and interface cases
  # Recovered 2026-11-18; independent review and separate executor required.

  Scenario: F079-ActionType-get
    Given SDK1.101.0, frozen published reader, fake identity, independently declared Device079/Inspectable079 schema and denied public network
    When Invoke v2.ontologies.ActionType.get in six native forms with exact kwargs below
    Then Match exact wire and typed nested result; generic403/timeout each send once; zero timeout sends nothing; unread/interrupted/canceled responses close
    And API v2 release stage is Stable
    And exact SDK inputs are
      """
      {"action_type": "rename-device079", "branch": "qa-branch079", "ontology": "qa-ontology079", "sdk_package_rid": "ri.qa.main.sdk.package079", "sdk_version": "0.7.9"}
      """
    And exact HTTP expectation is
      """
      {"body": null, "headers": {"Accept": "application/json"}, "method": "GET", "path": "/v2/ontologies/qa-ontology079/actionTypes/rename-device079", "query": {"branch": "qa-branch079", "sdkPackageRid": "ri.qa.main.sdk.package079", "sdkVersion": "0.7.9"}}
      """
    And exact decoded response is
      """
      {"apiName": "rename-device079", "operations": [{"interfaceTypeApiName": "Inspectable079", "type": "modifyInterfaceObject"}], "parameters": {"device": {"dataType": {"interfaceTypeApiName": "Inspectable079", "type": "interfaceObject"}, "displayName": "Device", "required": true}, "labelText": {"dataType": {"type": "string"}, "displayName": "Label", "required": true}}, "rid": "ri.qa.main.action-type.rename-device079", "status": "EXPERIMENTAL"}
      """
    And runtime response type is foundry_sdk.v2.ontologies.models.ActionTypeV2
    And nested schema category is action_summary
    And source named SDK error union is empty
    And exact adverse outcomes are
      """
      {"generic_403": {"class": "PermissionDeniedError", "errorName": "IndependentDenied079", "requests": 1}, "invalid_timeout": {"exception": "pydantic.ValidationError", "request_timeout": 0, "requests": 0}, "paging": {"budget": "three-distinct-cursors-partial-retain", "empty": "complete", "empty_with_continuation": "continue-until-next-data", "enabled": false, "item_budget": 1, "page_budget": 3, "repeated_cursor": "stop-retain"}, "stream": {"async_cancel": true, "caller_consumed_byte_limit": 4, "closed": true, "interrupted": true, "transport_chunk_may_be_larger": true, "unread": true}, "timeout": {"cause": "httpx.ReadTimeout", "class": "ReadTimeout", "replay": false, "requests": 1}}
      """
    And caller consumes at most four stream bytes, retains partial bytes and closes response even when transport chunk is larger

  Scenario: F079-ActionType-get_by_rid
    Given SDK1.101.0, frozen published reader, fake identity, independently declared Device079/Inspectable079 schema and denied public network
    When Invoke v2.ontologies.ActionType.get_by_rid in six native forms with exact kwargs below
    Then Match exact wire and typed nested result; generic403/timeout each send once; zero timeout sends nothing; unread/interrupted/canceled responses close
    And API v2 release stage is Stable
    And exact SDK inputs are
      """
      {"action_type_rid": "ri.qa.main.action-type.rename-device079", "branch": "qa-branch079", "ontology": "qa-ontology079"}
      """
    And exact HTTP expectation is
      """
      {"body": null, "headers": {"Accept": "application/json"}, "method": "GET", "path": "/v2/ontologies/qa-ontology079/actionTypes/byRid/ri.qa.main.action-type.rename-device079", "query": {"branch": "qa-branch079"}}
      """
    And exact decoded response is
      """
      {"apiName": "rename-device079", "operations": [{"interfaceTypeApiName": "Inspectable079", "type": "modifyInterfaceObject"}], "parameters": {"device": {"dataType": {"interfaceTypeApiName": "Inspectable079", "type": "interfaceObject"}, "displayName": "Device", "required": true}, "labelText": {"dataType": {"type": "string"}, "displayName": "Label", "required": true}}, "rid": "ri.qa.main.action-type.rename-device079", "status": "EXPERIMENTAL"}
      """
    And runtime response type is foundry_sdk.v2.ontologies.models.ActionTypeV2
    And nested schema category is action_summary
    And source named SDK error union is empty
    And exact adverse outcomes are
      """
      {"generic_403": {"class": "PermissionDeniedError", "errorName": "IndependentDenied079", "requests": 1}, "invalid_timeout": {"exception": "pydantic.ValidationError", "request_timeout": 0, "requests": 0}, "paging": {"budget": "three-distinct-cursors-partial-retain", "empty": "complete", "empty_with_continuation": "continue-until-next-data", "enabled": false, "item_budget": 1, "page_budget": 3, "repeated_cursor": "stop-retain"}, "stream": {"async_cancel": true, "caller_consumed_byte_limit": 4, "closed": true, "interrupted": true, "transport_chunk_may_be_larger": true, "unread": true}, "timeout": {"cause": "httpx.ReadTimeout", "class": "ReadTimeout", "replay": false, "requests": 1}}
      """
    And caller consumes at most four stream bytes, retains partial bytes and closes response even when transport chunk is larger

  Scenario: F079-ActionType-get_by_rid_batch
    Given SDK1.101.0, frozen published reader, fake identity, independently declared Device079/Inspectable079 schema and denied public network
    When Invoke v2.ontologies.ActionType.get_by_rid_batch in six native forms with exact kwargs below
    Then Match exact wire and typed nested result; generic403/timeout each send once; zero timeout sends nothing; unread/interrupted/canceled responses close
    And API v2 release stage is Public Beta
    And exact SDK inputs are
      """
      {"branch": "qa-branch079", "ontology": "qa-ontology079", "preview": true, "requests": [{"actionTypeRid": "ri.qa.main.action-type.rename-device079"}]}
      """
    And exact HTTP expectation is
      """
      {"body": {"requests": [{"actionTypeRid": "ri.qa.main.action-type.rename-device079"}]}, "headers": {"Accept": "application/json", "Content-Type": "application/json"}, "method": "POST", "path": "/v2/ontologies/qa-ontology079/actionTypes/getByRidBatch", "query": {"branch": "qa-branch079", "preview": true}}
      """
    And exact decoded response is
      """
      {"data": [{"apiName": "rename-device079", "operations": [{"interfaceTypeApiName": "Inspectable079", "type": "modifyInterfaceObject"}], "parameters": {"device": {"dataType": {"interfaceTypeApiName": "Inspectable079", "type": "interfaceObject"}, "displayName": "Device", "required": true}, "labelText": {"dataType": {"type": "string"}, "displayName": "Label", "required": true}}, "rid": "ri.qa.main.action-type.rename-device079", "status": "EXPERIMENTAL"}]}
      """
    And runtime response type is foundry_sdk.v2.ontologies.models.GetActionTypeByRidBatchResponse
    And nested schema category is action_summary
    And source named SDK error union is empty
    And exact adverse outcomes are
      """
      {"generic_403": {"class": "PermissionDeniedError", "errorName": "IndependentDenied079", "requests": 1}, "invalid_timeout": {"exception": "pydantic.ValidationError", "request_timeout": 0, "requests": 0}, "paging": {"budget": "three-distinct-cursors-partial-retain", "empty": "complete", "empty_with_continuation": "continue-until-next-data", "enabled": false, "item_budget": 1, "page_budget": 3, "repeated_cursor": "stop-retain"}, "stream": {"async_cancel": true, "caller_consumed_byte_limit": 4, "closed": true, "interrupted": true, "transport_chunk_may_be_larger": true, "unread": true}, "timeout": {"cause": "httpx.ReadTimeout", "class": "ReadTimeout", "replay": false, "requests": 1}}
      """
    And caller consumes at most four stream bytes, retains partial bytes and closes response even when transport chunk is larger

  Scenario: F079-ActionType-list
    Given SDK1.101.0, frozen published reader, fake identity, independently declared Device079/Inspectable079 schema and denied public network
    When Invoke v2.ontologies.ActionType.list in six native forms with exact kwargs below
    Then Match exact wire and typed nested result; generic403/timeout each send once; zero timeout sends nothing; unread/interrupted/canceled responses close
    And API v2 release stage is Stable
    And exact SDK inputs are
      """
      {"branch": "qa-branch079", "ontology": "qa-ontology079", "page_size": 2}
      """
    And exact HTTP expectation is
      """
      {"body": null, "headers": {"Accept": "application/json"}, "method": "GET", "path": "/v2/ontologies/qa-ontology079/actionTypes", "query": {"branch": "qa-branch079", "pageSize": 2}}
      """
    And exact decoded response is
      """
      {"data": [{"apiName": "rename-device079", "operations": [{"interfaceTypeApiName": "Inspectable079", "type": "modifyInterfaceObject"}], "parameters": {"device": {"dataType": {"interfaceTypeApiName": "Inspectable079", "type": "interfaceObject"}, "displayName": "Device", "required": true}, "labelText": {"dataType": {"type": "string"}, "displayName": "Label", "required": true}}, "rid": "ri.qa.main.action-type.rename-device079", "status": "EXPERIMENTAL"}]}
      """
    And runtime response type is foundry_sdk.v2.ontologies.models.ListActionTypesResponseV2
    And nested schema category is action_summary
    And source named SDK error union is empty
    And exact adverse outcomes are
      """
      {"generic_403": {"class": "PermissionDeniedError", "errorName": "IndependentDenied079", "requests": 1}, "invalid_timeout": {"exception": "pydantic.ValidationError", "request_timeout": 0, "requests": 0}, "paging": {"budget": "three-distinct-cursors-partial-retain", "empty": "complete", "empty_with_continuation": "continue-until-next-data", "enabled": true, "item_budget": 1, "page_budget": 3, "repeated_cursor": "stop-retain"}, "stream": {"async_cancel": true, "caller_consumed_byte_limit": 4, "closed": true, "interrupted": true, "transport_chunk_may_be_larger": true, "unread": true}, "timeout": {"cause": "httpx.ReadTimeout", "class": "ReadTimeout", "replay": false, "requests": 1}}
      """
    And terminal empty page completes; intermediate empty page follows continuation to next data
    And repeated cursor stops; three distinct cursor pages or one-item budget retains partial items and continuation
    And caller consumes at most four stream bytes, retains partial bytes and closes response even when transport chunk is larger

  Scenario: F079-ActionType-search
    Given SDK1.101.0, frozen published reader, fake identity, independently declared Device079/Inspectable079 schema and denied public network
    When Invoke v2.ontologies.ActionType.search in six native forms with exact kwargs below
    Then Match exact wire and typed nested result; generic403/timeout each send once; zero timeout sends nothing; unread/interrupted/canceled responses close
    And API v2 release stage is Private Beta
    And exact SDK inputs are
      """
      {"branch": "qa-branch079", "ontology": "qa-ontology079", "page_size": 2, "preview": true, "where": {"type": "actionTypeApiName", "value": {"type": "exact", "value": "rename-device079"}}}
      """
    And exact HTTP expectation is
      """
      {"body": {"pageSize": 2, "where": {"type": "actionTypeApiName", "value": {"type": "exact", "value": "rename-device079"}}}, "headers": {"Accept": "application/json", "Content-Type": "application/json"}, "method": "POST", "path": "/v2/ontologies/qa-ontology079/actionTypes/search", "query": {"branch": "qa-branch079", "preview": true}}
      """
    And exact decoded response is
      """
      {"data": [{"apiName": "rename-device079", "operations": [{"interfaceTypeApiName": "Inspectable079", "type": "modifyInterfaceObject"}], "parameters": {"device": {"dataType": {"interfaceTypeApiName": "Inspectable079", "type": "interfaceObject"}, "displayName": "Device", "required": true}, "labelText": {"dataType": {"type": "string"}, "displayName": "Label", "required": true}}, "rid": "ri.qa.main.action-type.rename-device079", "status": "EXPERIMENTAL"}], "totalCount": "1"}
      """
    And runtime response type is foundry_sdk.v2.ontologies.models.SearchActionTypesResponseV2
    And nested schema category is action_summary
    And source named SDK error union is empty
    And exact adverse outcomes are
      """
      {"generic_403": {"class": "PermissionDeniedError", "errorName": "IndependentDenied079", "requests": 1}, "invalid_timeout": {"exception": "pydantic.ValidationError", "request_timeout": 0, "requests": 0}, "paging": {"budget": "three-distinct-cursors-partial-retain", "empty": "complete", "empty_with_continuation": "continue-until-next-data", "enabled": true, "item_budget": 1, "page_budget": 3, "repeated_cursor": "stop-retain"}, "stream": {"async_cancel": true, "caller_consumed_byte_limit": 4, "closed": true, "interrupted": true, "transport_chunk_may_be_larger": true, "unread": true}, "timeout": {"cause": "httpx.ReadTimeout", "class": "ReadTimeout", "replay": false, "requests": 1}}
      """
    And terminal empty page completes; intermediate empty page follows continuation to next data
    And repeated cursor stops; three distinct cursor pages or one-item budget retains partial items and continuation
    And caller consumes at most four stream bytes, retains partial bytes and closes response even when transport chunk is larger

  Scenario: F079-ActionTypeFullMetadata-get
    Given SDK1.101.0, frozen published reader, fake identity, independently declared Device079/Inspectable079 schema and denied public network
    When Invoke v2.ontologies.ActionTypeFullMetadata.get in six native forms with exact kwargs below
    Then Match exact wire and typed nested result; generic403/timeout each send once; zero timeout sends nothing; unread/interrupted/canceled responses close
    And API v2 release stage is Private Beta
    And exact SDK inputs are
      """
      {"action_type": "rename-device079", "branch": "qa-branch079", "ontology": "qa-ontology079", "preview": true}
      """
    And exact HTTP expectation is
      """
      {"body": null, "headers": {"Accept": "application/json"}, "method": "GET", "path": "/v2/ontologies/qa-ontology079/actionTypes/rename-device079/fullMetadata", "query": {"branch": "qa-branch079", "preview": true}}
      """
    And exact decoded response is
      """
      {"actionType": {"apiName": "rename-device079", "operations": [{"interfaceTypeApiName": "Inspectable079", "type": "modifyInterfaceObject"}], "parameters": {"device": {"dataType": {"interfaceTypeApiName": "Inspectable079", "type": "interfaceObject"}, "displayName": "Device", "required": true}, "labelText": {"dataType": {"type": "string"}, "displayName": "Label", "required": true}}, "rid": "ri.qa.main.action-type.rename-device079", "status": "EXPERIMENTAL"}, "fullLogicRules": [{"interfaceObjectToModify": "device", "sharedPropertyArguments": {"label": {"parameterId": "labelText", "type": "parameterId"}}, "structPropertyArguments": {}, "type": "modifyInterface"}]}
      """
    And runtime response type is foundry_sdk.v2.ontologies.models.ActionTypeFullMetadata
    And nested schema category is action_rule
    And source named SDK error union is empty
    And exact adverse outcomes are
      """
      {"generic_403": {"class": "PermissionDeniedError", "errorName": "IndependentDenied079", "requests": 1}, "invalid_timeout": {"exception": "pydantic.ValidationError", "request_timeout": 0, "requests": 0}, "paging": {"budget": "three-distinct-cursors-partial-retain", "empty": "complete", "empty_with_continuation": "continue-until-next-data", "enabled": false, "item_budget": 1, "page_budget": 3, "repeated_cursor": "stop-retain"}, "stream": {"async_cancel": true, "caller_consumed_byte_limit": 4, "closed": true, "interrupted": true, "transport_chunk_may_be_larger": true, "unread": true}, "timeout": {"cause": "httpx.ReadTimeout", "class": "ReadTimeout", "replay": false, "requests": 1}}
      """
    And caller consumes at most four stream bytes, retains partial bytes and closes response even when transport chunk is larger

  Scenario: F079-ActionTypeFullMetadata-list
    Given SDK1.101.0, frozen published reader, fake identity, independently declared Device079/Inspectable079 schema and denied public network
    When Invoke v2.ontologies.ActionTypeFullMetadata.list in six native forms with exact kwargs below
    Then Match exact wire and typed nested result; generic403/timeout each send once; zero timeout sends nothing; unread/interrupted/canceled responses close
    And API v2 release stage is Private Beta
    And exact SDK inputs are
      """
      {"branch": "qa-branch079", "ontology": "qa-ontology079", "page_size": 2, "preview": true}
      """
    And exact HTTP expectation is
      """
      {"body": null, "headers": {"Accept": "application/json"}, "method": "GET", "path": "/v2/ontologies/qa-ontology079/actionTypesFullMetadata", "query": {"branch": "qa-branch079", "pageSize": 2, "preview": true}}
      """
    And exact decoded response is
      """
      {"data": [{"actionType": {"apiName": "rename-device079", "operations": [{"interfaceTypeApiName": "Inspectable079", "type": "modifyInterfaceObject"}], "parameters": {"device": {"dataType": {"interfaceTypeApiName": "Inspectable079", "type": "interfaceObject"}, "displayName": "Device", "required": true}, "labelText": {"dataType": {"type": "string"}, "displayName": "Label", "required": true}}, "rid": "ri.qa.main.action-type.rename-device079", "status": "EXPERIMENTAL"}, "fullLogicRules": [{"interfaceObjectToModify": "device", "sharedPropertyArguments": {"label": {"parameterId": "labelText", "type": "parameterId"}}, "structPropertyArguments": {}, "type": "modifyInterface"}]}]}
      """
    And runtime response type is foundry_sdk.v2.ontologies.models.ListActionTypesFullMetadataResponse
    And nested schema category is action_rule
    And source named SDK error union is empty
    And exact adverse outcomes are
      """
      {"generic_403": {"class": "PermissionDeniedError", "errorName": "IndependentDenied079", "requests": 1}, "invalid_timeout": {"exception": "pydantic.ValidationError", "request_timeout": 0, "requests": 0}, "paging": {"budget": "three-distinct-cursors-partial-retain", "empty": "complete", "empty_with_continuation": "continue-until-next-data", "enabled": true, "item_budget": 1, "page_budget": 3, "repeated_cursor": "stop-retain"}, "stream": {"async_cancel": true, "caller_consumed_byte_limit": 4, "closed": true, "interrupted": true, "transport_chunk_may_be_larger": true, "unread": true}, "timeout": {"cause": "httpx.ReadTimeout", "class": "ReadTimeout", "replay": false, "requests": 1}}
      """
    And terminal empty page completes; intermediate empty page follows continuation to next data
    And repeated cursor stops; three distinct cursor pages or one-item budget retains partial items and continuation
    And caller consumes at most four stream bytes, retains partial bytes and closes response even when transport chunk is larger

  Scenario: F079-ObjectType-get
    Given SDK1.101.0, frozen published reader, fake identity, independently declared Device079/Inspectable079 schema and denied public network
    When Invoke v2.ontologies.ObjectType.get in six native forms with exact kwargs below
    Then Match exact wire and typed nested result; generic403/timeout each send once; zero timeout sends nothing; unread/interrupted/canceled responses close
    And API v2 release stage is Stable
    And exact SDK inputs are
      """
      {"branch": "qa-branch079", "include_datasources": false, "object_type": "Device079", "ontology": "qa-ontology079"}
      """
    And exact HTTP expectation is
      """
      {"body": null, "headers": {"Accept": "application/json"}, "method": "GET", "path": "/v2/ontologies/qa-ontology079/objectTypes/Device079", "query": {"branch": "qa-branch079", "includeDatasources": false}}
      """
    And exact decoded response is
      """
      {"apiName": "Device079", "displayName": "Inspection device", "icon": {"color": "#126734", "name": "wrench", "type": "blueprint"}, "pluralDisplayName": "Inspection devices", "primaryKey": "deviceId", "properties": {"deviceId": {"dataType": {"type": "string"}, "rid": "ri.qa.main.property.deviceId"}, "label": {"dataType": {"type": "string"}, "rid": "ri.qa.main.property.label"}, "recordedAt": {"dataType": {"type": "timestamp"}, "rid": "ri.qa.main.property.recordedAt"}}, "rid": "ri.qa.main.object-type.device079", "status": "EXPERIMENTAL", "titleProperty": "label"}
      """
    And runtime response type is foundry_sdk.v2.ontologies.models.ObjectTypeV2
    And nested schema category is device_schema
    And source named SDK error union is empty
    And exact adverse outcomes are
      """
      {"generic_403": {"class": "PermissionDeniedError", "errorName": "IndependentDenied079", "requests": 1}, "invalid_timeout": {"exception": "pydantic.ValidationError", "request_timeout": 0, "requests": 0}, "paging": {"budget": "three-distinct-cursors-partial-retain", "empty": "complete", "empty_with_continuation": "continue-until-next-data", "enabled": false, "item_budget": 1, "page_budget": 3, "repeated_cursor": "stop-retain"}, "stream": {"async_cancel": true, "caller_consumed_byte_limit": 4, "closed": true, "interrupted": true, "transport_chunk_may_be_larger": true, "unread": true}, "timeout": {"cause": "httpx.ReadTimeout", "class": "ReadTimeout", "replay": false, "requests": 1}}
      """
    And caller consumes at most four stream bytes, retains partial bytes and closes response even when transport chunk is larger

  Scenario: F079-ObjectType-get_by_rid_batch
    Given SDK1.101.0, frozen published reader, fake identity, independently declared Device079/Inspectable079 schema and denied public network
    When Invoke v2.ontologies.ObjectType.get_by_rid_batch in six native forms with exact kwargs below
    Then Match exact wire and typed nested result; generic403/timeout each send once; zero timeout sends nothing; unread/interrupted/canceled responses close
    And API v2 release stage is Public Beta
    And exact SDK inputs are
      """
      {"branch": "qa-branch079", "ontology": "qa-ontology079", "preview": true, "requests": [{"objectTypeRid": "ri.qa.main.object-type.device079"}]}
      """
    And exact HTTP expectation is
      """
      {"body": {"requests": [{"objectTypeRid": "ri.qa.main.object-type.device079"}]}, "headers": {"Accept": "application/json", "Content-Type": "application/json"}, "method": "POST", "path": "/v2/ontologies/qa-ontology079/objectTypes/getByRidBatch", "query": {"branch": "qa-branch079", "preview": true}}
      """
    And exact decoded response is
      """
      {"data": [{"apiName": "Device079", "displayName": "Inspection device", "icon": {"color": "#126734", "name": "wrench", "type": "blueprint"}, "pluralDisplayName": "Inspection devices", "primaryKey": "deviceId", "properties": {"deviceId": {"dataType": {"type": "string"}, "rid": "ri.qa.main.property.deviceId"}, "label": {"dataType": {"type": "string"}, "rid": "ri.qa.main.property.label"}, "recordedAt": {"dataType": {"type": "timestamp"}, "rid": "ri.qa.main.property.recordedAt"}}, "rid": "ri.qa.main.object-type.device079", "status": "EXPERIMENTAL", "titleProperty": "label"}]}
      """
    And runtime response type is foundry_sdk.v2.ontologies.models.GetObjectTypeByRidBatchResponse
    And nested schema category is device_schema
    And source named SDK error union is empty
    And exact adverse outcomes are
      """
      {"generic_403": {"class": "PermissionDeniedError", "errorName": "IndependentDenied079", "requests": 1}, "invalid_timeout": {"exception": "pydantic.ValidationError", "request_timeout": 0, "requests": 0}, "paging": {"budget": "three-distinct-cursors-partial-retain", "empty": "complete", "empty_with_continuation": "continue-until-next-data", "enabled": false, "item_budget": 1, "page_budget": 3, "repeated_cursor": "stop-retain"}, "stream": {"async_cancel": true, "caller_consumed_byte_limit": 4, "closed": true, "interrupted": true, "transport_chunk_may_be_larger": true, "unread": true}, "timeout": {"cause": "httpx.ReadTimeout", "class": "ReadTimeout", "replay": false, "requests": 1}}
      """
    And caller consumes at most four stream bytes, retains partial bytes and closes response even when transport chunk is larger

  Scenario: F079-ObjectType-get_edits_history
    Given SDK1.101.0, frozen published reader, fake identity, independently declared Device079/Inspectable079 schema and denied public network
    When Invoke v2.ontologies.ObjectType.get_edits_history in six native forms with exact kwargs below
    Then Match exact wire and typed nested result; generic403/timeout each send once; zero timeout sends nothing; unread/interrupted/canceled responses close
    And API v2 release stage is Public Beta
    And exact SDK inputs are
      """
      {"branch": "qa-branch079", "include_all_previous_properties": true, "object_primary_key": {"deviceId": {"type": "stringValue", "value": "D-079"}}, "object_type": "Device079", "ontology": "qa-ontology079", "page_size": 2, "preview": true, "sort_order": "oldest_first"}
      """
    And exact HTTP expectation is
      """
      {"body": {"includeAllPreviousProperties": true, "objectPrimaryKey": {"deviceId": {"type": "stringValue", "value": "D-079"}}, "pageSize": 2, "sortOrder": "oldest_first"}, "headers": {"Accept": "application/json", "Content-Type": "application/json"}, "method": "POST", "path": "/v2/ontologies/qa-ontology079/objectTypes/Device079/editsHistory", "query": {"branch": "qa-branch079", "preview": true}}
      """
    And exact decoded response is
      """
      {"data": [{"actionTypeRid": "ri.qa.main.action-type.rename-device079", "edit": {"objectType": "Device079", "properties": {"deviceId": "D-079", "label": "Valve 079", "recordedAt": "2026-11-16T08:00:00Z"}, "type": "createEdit"}, "objectPrimaryKey": {"deviceId": {"type": "stringValue", "value": "D-079"}}, "operationId": "ri.qa.main.operation.history079", "timestamp": "2026-11-16T08:00:00+00:00", "userId": "qa-user079"}]}
      """
    And runtime response type is foundry_sdk.v2.ontologies.models.ObjectTypeEditsHistoryResponse
    And nested schema category is history
    And source named SDK error union is empty
    And exact adverse outcomes are
      """
      {"generic_403": {"class": "PermissionDeniedError", "errorName": "IndependentDenied079", "requests": 1}, "invalid_timeout": {"exception": "pydantic.ValidationError", "request_timeout": 0, "requests": 0}, "paging": {"budget": "three-distinct-cursors-partial-retain", "empty": "complete", "empty_with_continuation": "continue-until-next-data", "enabled": true, "item_budget": 1, "page_budget": 3, "repeated_cursor": "stop-retain"}, "stream": {"async_cancel": true, "caller_consumed_byte_limit": 4, "closed": true, "interrupted": true, "transport_chunk_may_be_larger": true, "unread": true}, "timeout": {"cause": "httpx.ReadTimeout", "class": "ReadTimeout", "replay": false, "requests": 1}}
      """
    And terminal empty page completes; intermediate empty page follows continuation to next data
    And repeated cursor stops; three distinct cursor pages or one-item budget retains partial items and continuation
    And caller consumes at most four stream bytes, retains partial bytes and closes response even when transport chunk is larger

  Scenario: F079-ObjectType-get_full_metadata
    Given SDK1.101.0, frozen published reader, fake identity, independently declared Device079/Inspectable079 schema and denied public network
    When Invoke v2.ontologies.ObjectType.get_full_metadata in six native forms with exact kwargs below
    Then Match exact wire and typed nested result; generic403/timeout each send once; zero timeout sends nothing; unread/interrupted/canceled responses close
    And API v2 release stage is Public Beta
    And exact SDK inputs are
      """
      {"branch": "qa-branch079", "include_datasources": false, "object_type": "Device079", "ontology": "qa-ontology079", "preview": true, "sdk_package_rid": "ri.qa.main.sdk.package079", "sdk_version": "0.7.9"}
      """
    And exact HTTP expectation is
      """
      {"body": null, "headers": {"Accept": "application/json"}, "method": "GET", "path": "/v2/ontologies/qa-ontology079/objectTypes/Device079/fullMetadata", "query": {"branch": "qa-branch079", "includeDatasources": false, "preview": true, "sdkPackageRid": "ri.qa.main.sdk.package079", "sdkVersion": "0.7.9"}}
      """
    And exact decoded response is
      """
      {"implementsInterfaces": ["Inspectable079"], "implementsInterfaces2": {"Inspectable079": {"apiName": "Inspectable079", "links": {"inspectedPeers079": ["relatedDevices079"]}, "properties": {"deviceId": "deviceId", "label": "label", "recordedAt": "recordedAt"}, "propertiesV2": {"deviceId": {"propertyApiName": "deviceId", "type": "localPropertyImplementation"}, "label": {"propertyApiName": "label", "type": "localPropertyImplementation"}, "recordedAt": {"propertyApiName": "recordedAt", "type": "localPropertyImplementation"}}, "rid": "ri.qa.main.interface-type.inspectable079"}}, "linkTypes": [{"apiName": "relatedDevices079", "cardinality": "MANY", "displayName": "Related devices", "linkTypeRid": "ri.qa.main.link-type.related-devices079", "objectTypeApiName": "Device079", "status": "EXPERIMENTAL"}], "objectType": {"apiName": "Device079", "displayName": "Inspection device", "icon": {"color": "#126734", "name": "wrench", "type": "blueprint"}, "pluralDisplayName": "Inspection devices", "primaryKey": "deviceId", "properties": {"deviceId": {"dataType": {"type": "string"}, "rid": "ri.qa.main.property.deviceId"}, "label": {"dataType": {"type": "string"}, "rid": "ri.qa.main.property.label"}, "recordedAt": {"dataType": {"type": "timestamp"}, "rid": "ri.qa.main.property.recordedAt"}}, "rid": "ri.qa.main.object-type.device079", "status": "EXPERIMENTAL", "titleProperty": "label"}, "sharedPropertyTypeMapping": {"deviceId": "deviceId", "label": "label", "recordedAt": "recordedAt"}}
      """
    And runtime response type is foundry_sdk.v2.ontologies.models.ObjectTypeFullMetadata
    And nested schema category is device_full
    And source named SDK error union is empty
    And exact adverse outcomes are
      """
      {"generic_403": {"class": "PermissionDeniedError", "errorName": "IndependentDenied079", "requests": 1}, "invalid_timeout": {"exception": "pydantic.ValidationError", "request_timeout": 0, "requests": 0}, "paging": {"budget": "three-distinct-cursors-partial-retain", "empty": "complete", "empty_with_continuation": "continue-until-next-data", "enabled": false, "item_budget": 1, "page_budget": 3, "repeated_cursor": "stop-retain"}, "stream": {"async_cancel": true, "caller_consumed_byte_limit": 4, "closed": true, "interrupted": true, "transport_chunk_may_be_larger": true, "unread": true}, "timeout": {"cause": "httpx.ReadTimeout", "class": "ReadTimeout", "replay": false, "requests": 1}}
      """
    And caller consumes at most four stream bytes, retains partial bytes and closes response even when transport chunk is larger

  Scenario: F079-ObjectType-get_outgoing_link_type
    Given SDK1.101.0, frozen published reader, fake identity, independently declared Device079/Inspectable079 schema and denied public network
    When Invoke v2.ontologies.ObjectType.get_outgoing_link_type in six native forms with exact kwargs below
    Then Match exact wire and typed nested result; generic403/timeout each send once; zero timeout sends nothing; unread/interrupted/canceled responses close
    And API v2 release stage is Stable
    And exact SDK inputs are
      """
      {"branch": "qa-branch079", "link_type": "relatedDevices079", "object_type": "Device079", "ontology": "qa-ontology079"}
      """
    And exact HTTP expectation is
      """
      {"body": null, "headers": {"Accept": "application/json"}, "method": "GET", "path": "/v2/ontologies/qa-ontology079/objectTypes/Device079/outgoingLinkTypes/relatedDevices079", "query": {"branch": "qa-branch079"}}
      """
    And exact decoded response is
      """
      {"apiName": "relatedDevices079", "cardinality": "MANY", "displayName": "Related devices", "linkTypeRid": "ri.qa.main.link-type.related-devices079", "objectTypeApiName": "Device079", "status": "EXPERIMENTAL"}
      """
    And runtime response type is foundry_sdk.v2.ontologies.models.LinkTypeSideV2
    And nested schema category is object_link
    And source named SDK error union is empty
    And exact adverse outcomes are
      """
      {"generic_403": {"class": "PermissionDeniedError", "errorName": "IndependentDenied079", "requests": 1}, "invalid_timeout": {"exception": "pydantic.ValidationError", "request_timeout": 0, "requests": 0}, "paging": {"budget": "three-distinct-cursors-partial-retain", "empty": "complete", "empty_with_continuation": "continue-until-next-data", "enabled": false, "item_budget": 1, "page_budget": 3, "repeated_cursor": "stop-retain"}, "stream": {"async_cancel": true, "caller_consumed_byte_limit": 4, "closed": true, "interrupted": true, "transport_chunk_may_be_larger": true, "unread": true}, "timeout": {"cause": "httpx.ReadTimeout", "class": "ReadTimeout", "replay": false, "requests": 1}}
      """
    And caller consumes at most four stream bytes, retains partial bytes and closes response even when transport chunk is larger

  Scenario: F079-ObjectType-get_outgoing_link_types_by_object_type_rid_batch
    Given SDK1.101.0, frozen published reader, fake identity, independently declared Device079/Inspectable079 schema and denied public network
    When Invoke v2.ontologies.ObjectType.get_outgoing_link_types_by_object_type_rid_batch in six native forms with exact kwargs below
    Then Match exact wire and typed nested result; generic403/timeout each send once; zero timeout sends nothing; unread/interrupted/canceled responses close
    And API v2 release stage is Public Beta
    And exact SDK inputs are
      """
      {"branch": "qa-branch079", "filter_link_type_rids": ["ri.qa.main.link-type.related-devices079"], "ontology": "qa-ontology079", "preview": true, "requests": [{"objectTypeRid": "ri.qa.main.object-type.device079"}]}
      """
    And exact HTTP expectation is
      """
      {"body": {"filterLinkTypeRids": ["ri.qa.main.link-type.related-devices079"], "requests": [{"objectTypeRid": "ri.qa.main.object-type.device079"}]}, "headers": {"Accept": "application/json", "Content-Type": "application/json"}, "method": "POST", "path": "/v2/ontologies/qa-ontology079/outgoingLinkTypes/getByRidBatch", "query": {"branch": "qa-branch079", "preview": true}}
      """
    And exact decoded response is
      """
      {"data": {"ri.qa.main.object-type.device079": [{"apiName": "relatedDevices079", "cardinality": "MANY", "displayName": "Related devices", "linkTypeRid": "ri.qa.main.link-type.related-devices079", "objectTypeApiName": "Device079", "status": "EXPERIMENTAL"}]}}
      """
    And runtime response type is foundry_sdk.v2.ontologies.models.GetOutgoingLinkTypesByObjectTypeRidBatchResponse
    And nested schema category is object_link
    And source named SDK error union is empty
    And exact adverse outcomes are
      """
      {"generic_403": {"class": "PermissionDeniedError", "errorName": "IndependentDenied079", "requests": 1}, "invalid_timeout": {"exception": "pydantic.ValidationError", "request_timeout": 0, "requests": 0}, "paging": {"budget": "three-distinct-cursors-partial-retain", "empty": "complete", "empty_with_continuation": "continue-until-next-data", "enabled": false, "item_budget": 1, "page_budget": 3, "repeated_cursor": "stop-retain"}, "stream": {"async_cancel": true, "caller_consumed_byte_limit": 4, "closed": true, "interrupted": true, "transport_chunk_may_be_larger": true, "unread": true}, "timeout": {"cause": "httpx.ReadTimeout", "class": "ReadTimeout", "replay": false, "requests": 1}}
      """
    And caller consumes at most four stream bytes, retains partial bytes and closes response even when transport chunk is larger

  Scenario: F079-ObjectType-list
    Given SDK1.101.0, frozen published reader, fake identity, independently declared Device079/Inspectable079 schema and denied public network
    When Invoke v2.ontologies.ObjectType.list in six native forms with exact kwargs below
    Then Match exact wire and typed nested result; generic403/timeout each send once; zero timeout sends nothing; unread/interrupted/canceled responses close
    And API v2 release stage is Stable
    And exact SDK inputs are
      """
      {"branch": "qa-branch079", "include_datasources": false, "ontology": "qa-ontology079", "page_size": 2}
      """
    And exact HTTP expectation is
      """
      {"body": null, "headers": {"Accept": "application/json"}, "method": "GET", "path": "/v2/ontologies/qa-ontology079/objectTypes", "query": {"branch": "qa-branch079", "includeDatasources": false, "pageSize": 2}}
      """
    And exact decoded response is
      """
      {"data": [{"apiName": "Device079", "displayName": "Inspection device", "icon": {"color": "#126734", "name": "wrench", "type": "blueprint"}, "pluralDisplayName": "Inspection devices", "primaryKey": "deviceId", "properties": {"deviceId": {"dataType": {"type": "string"}, "rid": "ri.qa.main.property.deviceId"}, "label": {"dataType": {"type": "string"}, "rid": "ri.qa.main.property.label"}, "recordedAt": {"dataType": {"type": "timestamp"}, "rid": "ri.qa.main.property.recordedAt"}}, "rid": "ri.qa.main.object-type.device079", "status": "EXPERIMENTAL", "titleProperty": "label"}]}
      """
    And runtime response type is foundry_sdk.v2.ontologies.models.ListObjectTypesV2Response
    And nested schema category is device_schema
    And source named SDK error union is empty
    And exact adverse outcomes are
      """
      {"generic_403": {"class": "PermissionDeniedError", "errorName": "IndependentDenied079", "requests": 1}, "invalid_timeout": {"exception": "pydantic.ValidationError", "request_timeout": 0, "requests": 0}, "paging": {"budget": "three-distinct-cursors-partial-retain", "empty": "complete", "empty_with_continuation": "continue-until-next-data", "enabled": true, "item_budget": 1, "page_budget": 3, "repeated_cursor": "stop-retain"}, "stream": {"async_cancel": true, "caller_consumed_byte_limit": 4, "closed": true, "interrupted": true, "transport_chunk_may_be_larger": true, "unread": true}, "timeout": {"cause": "httpx.ReadTimeout", "class": "ReadTimeout", "replay": false, "requests": 1}}
      """
    And terminal empty page completes; intermediate empty page follows continuation to next data
    And repeated cursor stops; three distinct cursor pages or one-item budget retains partial items and continuation
    And caller consumes at most four stream bytes, retains partial bytes and closes response even when transport chunk is larger

  Scenario: F079-ObjectType-list_outgoing_link_types
    Given SDK1.101.0, frozen published reader, fake identity, independently declared Device079/Inspectable079 schema and denied public network
    When Invoke v2.ontologies.ObjectType.list_outgoing_link_types in six native forms with exact kwargs below
    Then Match exact wire and typed nested result; generic403/timeout each send once; zero timeout sends nothing; unread/interrupted/canceled responses close
    And API v2 release stage is Stable
    And exact SDK inputs are
      """
      {"branch": "qa-branch079", "object_type": "Device079", "ontology": "qa-ontology079", "page_size": 2}
      """
    And exact HTTP expectation is
      """
      {"body": null, "headers": {"Accept": "application/json"}, "method": "GET", "path": "/v2/ontologies/qa-ontology079/objectTypes/Device079/outgoingLinkTypes", "query": {"branch": "qa-branch079", "pageSize": 2}}
      """
    And exact decoded response is
      """
      {"data": [{"apiName": "relatedDevices079", "cardinality": "MANY", "displayName": "Related devices", "linkTypeRid": "ri.qa.main.link-type.related-devices079", "objectTypeApiName": "Device079", "status": "EXPERIMENTAL"}]}
      """
    And runtime response type is foundry_sdk.v2.ontologies.models.ListOutgoingLinkTypesResponseV2
    And nested schema category is object_link
    And source named SDK error union is empty
    And exact adverse outcomes are
      """
      {"generic_403": {"class": "PermissionDeniedError", "errorName": "IndependentDenied079", "requests": 1}, "invalid_timeout": {"exception": "pydantic.ValidationError", "request_timeout": 0, "requests": 0}, "paging": {"budget": "three-distinct-cursors-partial-retain", "empty": "complete", "empty_with_continuation": "continue-until-next-data", "enabled": true, "item_budget": 1, "page_budget": 3, "repeated_cursor": "stop-retain"}, "stream": {"async_cancel": true, "caller_consumed_byte_limit": 4, "closed": true, "interrupted": true, "transport_chunk_may_be_larger": true, "unread": true}, "timeout": {"cause": "httpx.ReadTimeout", "class": "ReadTimeout", "replay": false, "requests": 1}}
      """
    And terminal empty page completes; intermediate empty page follows continuation to next data
    And repeated cursor stops; three distinct cursor pages or one-item budget retains partial items and continuation
    And caller consumes at most four stream bytes, retains partial bytes and closes response even when transport chunk is larger

  Scenario: F079-Ontology-get
    Given SDK1.101.0, frozen published reader, fake identity, independently declared Device079/Inspectable079 schema and denied public network
    When Invoke v2.ontologies.Ontology.get in six native forms with exact kwargs below
    Then Match exact wire and typed nested result; generic403/timeout each send once; zero timeout sends nothing; unread/interrupted/canceled responses close
    And API v2 release stage is Stable
    And exact SDK inputs are
      """
      {"ontology": "qa-ontology079"}
      """
    And exact HTTP expectation is
      """
      {"body": null, "headers": {"Accept": "application/json"}, "method": "GET", "path": "/v2/ontologies/qa-ontology079", "query": {}}
      """
    And exact decoded response is
      """
      {"apiName": "qa-ontology079", "description": "Synthetic inspection metadata", "displayName": "QA Ontology 079", "rid": "ri.qa.main.ontology.inspection079"}
      """
    And runtime response type is foundry_sdk.v2.ontologies.models.OntologyV2
    And nested schema category is ontology
    And source named SDK error union is empty
    And exact adverse outcomes are
      """
      {"generic_403": {"class": "PermissionDeniedError", "errorName": "IndependentDenied079", "requests": 1}, "invalid_timeout": {"exception": "pydantic.ValidationError", "request_timeout": 0, "requests": 0}, "paging": {"budget": "three-distinct-cursors-partial-retain", "empty": "complete", "empty_with_continuation": "continue-until-next-data", "enabled": false, "item_budget": 1, "page_budget": 3, "repeated_cursor": "stop-retain"}, "stream": {"async_cancel": true, "caller_consumed_byte_limit": 4, "closed": true, "interrupted": true, "transport_chunk_may_be_larger": true, "unread": true}, "timeout": {"cause": "httpx.ReadTimeout", "class": "ReadTimeout", "replay": false, "requests": 1}}
      """
    And caller consumes at most four stream bytes, retains partial bytes and closes response even when transport chunk is larger

  Scenario: F079-Ontology-get_full_metadata
    Given SDK1.101.0, frozen published reader, fake identity, independently declared Device079/Inspectable079 schema and denied public network
    When Invoke v2.ontologies.Ontology.get_full_metadata in six native forms with exact kwargs below
    Then Match exact wire and typed nested result; generic403/timeout each send once; zero timeout sends nothing; unread/interrupted/canceled responses close
    And API v2 release stage is Public Beta
    And exact SDK inputs are
      """
      {"branch": "qa-branch079", "ontology": "qa-ontology079", "preview": true}
      """
    And exact HTTP expectation is
      """
      {"body": null, "headers": {"Accept": "application/json"}, "method": "GET", "path": "/v2/ontologies/qa-ontology079/fullMetadata", "query": {"branch": "qa-branch079", "preview": true}}
      """
    And exact decoded response is
      """
      {"actionTypes": {"rename-device079": {"apiName": "rename-device079", "operations": [{"interfaceTypeApiName": "Inspectable079", "type": "modifyInterfaceObject"}], "parameters": {"device": {"dataType": {"interfaceTypeApiName": "Inspectable079", "type": "interfaceObject"}, "displayName": "Device", "required": true}, "labelText": {"dataType": {"type": "string"}, "displayName": "Label", "required": true}}, "rid": "ri.qa.main.action-type.rename-device079", "status": "EXPERIMENTAL"}}, "interfaceTypes": {"Inspectable079": {"allExtendsInterfaces": [], "allLinks": {"inspectedPeers079": {"apiName": "inspectedPeers079", "cardinality": "MANY", "displayName": "Inspected peers", "linkedEntityApiName": {"apiName": "Inspectable079", "type": "interfaceTypeApiName"}, "required": true, "rid": "ri.qa.main.interface-link-type.inspectables079"}}, "allProperties": {"deviceId": {"apiName": "deviceId", "dataType": {"type": "string"}, "displayName": "deviceId", "required": true, "rid": "ri.qa.main.shared-property.deviceId", "type": "interfaceSharedPropertyType"}, "label": {"apiName": "label", "dataType": {"type": "string"}, "displayName": "label", "required": true, "rid": "ri.qa.main.shared-property.label", "type": "interfaceSharedPropertyType"}, "recordedAt": {"apiName": "recordedAt", "dataType": {"type": "timestamp"}, "displayName": "recordedAt", "required": true, "rid": "ri.qa.main.shared-property.recordedAt", "type": "interfaceSharedPropertyType"}}, "allPropertiesV2": {"deviceId": {"apiName": "deviceId", "dataType": {"type": "string"}, "displayName": "deviceId", "requireImplementation": true, "rid": "ri.qa.main.shared-property.deviceId"}, "label": {"apiName": "label", "dataType": {"type": "string"}, "displayName": "label", "requireImplementation": true, "rid": "ri.qa.main.shared-property.label"}, "recordedAt": {"apiName": "recordedAt", "dataType": {"type": "timestamp"}, "displayName": "recordedAt", "requireImplementation": true, "rid": "ri.qa.main.shared-property.recordedAt"}}, "apiName": "Inspectable079", "displayName": "Inspectable", "extendsInterfaces": [], "implementedByObjectTypes": ["Device079"], "links": {"inspectedPeers079": {"apiName": "inspectedPeers079", "cardinality": "MANY", "displayName": "Inspected peers", "linkedEntityApiName": {"apiName": "Inspectable079", "type": "interfaceTypeApiName"}, "required": true, "rid": "ri.qa.main.interface-link-type.inspectables079"}}, "properties": {"deviceId": {"apiName": "deviceId", "dataType": {"type": "string"}, "displayName": "deviceId", "required": true, "rid": "ri.qa.main.shared-property.deviceId", "type": "interfaceSharedPropertyType"}, "label": {"apiName": "label", "dataType": {"type": "string"}, "displayName": "label", "required": true, "rid": "ri.qa.main.shared-property.label", "type": "interfaceSharedPropertyType"}, "recordedAt": {"apiName": "recordedAt", "dataType": {"type": "timestamp"}, "displayName": "recordedAt", "required": true, "rid": "ri.qa.main.shared-property.recordedAt", "type": "interfaceSharedPropertyType"}}, "propertiesV2": {"deviceId": {"apiName": "deviceId", "dataType": {"type": "string"}, "displayName": "deviceId", "required": true, "rid": "ri.qa.main.shared-property.deviceId", "type": "interfaceSharedPropertyType"}, "label": {"apiName": "label", "dataType": {"type": "string"}, "displayName": "label", "required": true, "rid": "ri.qa.main.shared-property.label", "type": "interfaceSharedPropertyType"}, "recordedAt": {"apiName": "recordedAt", "dataType": {"type": "timestamp"}, "displayName": "recordedAt", "required": true, "rid": "ri.qa.main.shared-property.recordedAt", "type": "interfaceSharedPropertyType"}}, "rid": "ri.qa.main.interface-type.inspectable079"}}, "objectTypes": {"Device079": {"implementsInterfaces": ["Inspectable079"], "implementsInterfaces2": {"Inspectable079": {"apiName": "Inspectable079", "links": {"inspectedPeers079": ["relatedDevices079"]}, "properties": {"deviceId": "deviceId", "label": "label", "recordedAt": "recordedAt"}, "propertiesV2": {"deviceId": {"propertyApiName": "deviceId", "type": "localPropertyImplementation"}, "label": {"propertyApiName": "label", "type": "localPropertyImplementation"}, "recordedAt": {"propertyApiName": "recordedAt", "type": "localPropertyImplementation"}}, "rid": "ri.qa.main.interface-type.inspectable079"}}, "linkTypes": [{"apiName": "relatedDevices079", "cardinality": "MANY", "displayName": "Related devices", "linkTypeRid": "ri.qa.main.link-type.related-devices079", "objectTypeApiName": "Device079", "status": "EXPERIMENTAL"}], "objectType": {"apiName": "Device079", "displayName": "Inspection device", "icon": {"color": "#126734", "name": "wrench", "type": "blueprint"}, "pluralDisplayName": "Inspection devices", "primaryKey": "deviceId", "properties": {"deviceId": {"dataType": {"type": "string"}, "rid": "ri.qa.main.property.deviceId"}, "label": {"dataType": {"type": "string"}, "rid": "ri.qa.main.property.label"}, "recordedAt": {"dataType": {"type": "timestamp"}, "rid": "ri.qa.main.property.recordedAt"}}, "rid": "ri.qa.main.object-type.device079", "status": "EXPERIMENTAL", "titleProperty": "label"}, "sharedPropertyTypeMapping": {"deviceId": "deviceId", "label": "label", "recordedAt": "recordedAt"}}}, "ontology": {"apiName": "qa-ontology079", "description": "Synthetic inspection metadata", "displayName": "QA Ontology 079", "rid": "ri.qa.main.ontology.inspection079"}, "queryTypes": {"countDevices079": {"apiName": "countDevices079", "output": {"type": "integer"}, "parameters": {"labelPrefix": {"dataType": {"type": "string"}, "required": true}}, "rid": "ri.qa.main.query-type.count-devices079", "typeReferences": {}, "version": "2.3.0"}}, "sharedPropertyTypes": {"deviceId": {"apiName": "deviceId", "dataType": {"type": "string"}, "displayName": "deviceId", "rid": "ri.qa.main.shared-property.deviceId"}, "label": {"apiName": "label", "dataType": {"type": "string"}, "displayName": "label", "rid": "ri.qa.main.shared-property.label"}, "recordedAt": {"apiName": "recordedAt", "dataType": {"type": "timestamp"}, "displayName": "recordedAt", "rid": "ri.qa.main.shared-property.recordedAt"}}, "valueTypes": {"InspectionDate079": {"apiName": "InspectionDate079", "constraints": [], "displayName": "Inspection date", "fieldType": {"type": "date"}, "rid": "ri.qa.main.value-type.inspection-date079", "version": "3"}}}
      """
    And runtime response type is foundry_sdk.v2.ontologies.models.OntologyFullMetadata
    And nested schema category is ontology_full
    And source named SDK error union is empty
    And exact adverse outcomes are
      """
      {"generic_403": {"class": "PermissionDeniedError", "errorName": "IndependentDenied079", "requests": 1}, "invalid_timeout": {"exception": "pydantic.ValidationError", "request_timeout": 0, "requests": 0}, "paging": {"budget": "three-distinct-cursors-partial-retain", "empty": "complete", "empty_with_continuation": "continue-until-next-data", "enabled": false, "item_budget": 1, "page_budget": 3, "repeated_cursor": "stop-retain"}, "stream": {"async_cancel": true, "caller_consumed_byte_limit": 4, "closed": true, "interrupted": true, "transport_chunk_may_be_larger": true, "unread": true}, "timeout": {"cause": "httpx.ReadTimeout", "class": "ReadTimeout", "replay": false, "requests": 1}}
      """
    And caller consumes at most four stream bytes, retains partial bytes and closes response even when transport chunk is larger

  Scenario: F079-Ontology-list
    Given SDK1.101.0, frozen published reader, fake identity, independently declared Device079/Inspectable079 schema and denied public network
    When Invoke v2.ontologies.Ontology.list in six native forms with exact kwargs below
    Then Match exact wire and typed nested result; generic403/timeout each send once; zero timeout sends nothing; unread/interrupted/canceled responses close
    And API v2 release stage is Stable
    And exact SDK inputs are
      """
      {}
      """
    And exact HTTP expectation is
      """
      {"body": null, "headers": {"Accept": "application/json"}, "method": "GET", "path": "/v2/ontologies", "query": {}}
      """
    And exact decoded response is
      """
      {"data": [{"apiName": "qa-ontology079", "description": "Synthetic inspection metadata", "displayName": "QA Ontology 079", "rid": "ri.qa.main.ontology.inspection079"}]}
      """
    And runtime response type is foundry_sdk.v2.ontologies.models.ListOntologiesV2Response
    And nested schema category is ontology
    And source named SDK error union is empty
    And exact adverse outcomes are
      """
      {"generic_403": {"class": "PermissionDeniedError", "errorName": "IndependentDenied079", "requests": 1}, "invalid_timeout": {"exception": "pydantic.ValidationError", "request_timeout": 0, "requests": 0}, "paging": {"budget": "three-distinct-cursors-partial-retain", "empty": "complete", "empty_with_continuation": "continue-until-next-data", "enabled": false, "item_budget": 1, "page_budget": 3, "repeated_cursor": "stop-retain"}, "stream": {"async_cancel": true, "caller_consumed_byte_limit": 4, "closed": true, "interrupted": true, "transport_chunk_may_be_larger": true, "unread": true}, "timeout": {"cause": "httpx.ReadTimeout", "class": "ReadTimeout", "replay": false, "requests": 1}}
      """
    And caller consumes at most four stream bytes, retains partial bytes and closes response even when transport chunk is larger

  Scenario: F079-Ontology-load_metadata
    Given SDK1.101.0, frozen published reader, fake identity, independently declared Device079/Inspectable079 schema and denied public network
    When Invoke v2.ontologies.Ontology.load_metadata in six native forms with exact kwargs below
    Then Match exact wire and typed nested result; generic403/timeout each send once; zero timeout sends nothing; unread/interrupted/canceled responses close
    And API v2 release stage is Private Beta
    And exact SDK inputs are
      """
      {"action_types": ["rename-device079"], "branch": "qa-branch079", "interface_types": ["Inspectable079"], "link_types": ["relatedDevices079"], "object_types": ["Device079"], "ontology": "qa-ontology079", "preview": true, "query_types": ["countDevices079"]}
      """
    And exact HTTP expectation is
      """
      {"body": {"actionTypes": ["rename-device079"], "interfaceTypes": ["Inspectable079"], "linkTypes": ["relatedDevices079"], "objectTypes": ["Device079"], "queryTypes": ["countDevices079"]}, "headers": {"Accept": "application/json", "Content-Type": "application/json"}, "method": "POST", "path": "/v2/ontologies/qa-ontology079/metadata", "query": {"branch": "qa-branch079", "preview": true}}
      """
    And exact decoded response is
      """
      {"actionTypes": {"rename-device079": {"apiName": "rename-device079", "operations": [{"interfaceTypeApiName": "Inspectable079", "type": "modifyInterfaceObject"}], "parameters": {"device": {"dataType": {"interfaceTypeApiName": "Inspectable079", "type": "interfaceObject"}, "displayName": "Device", "required": true}, "labelText": {"dataType": {"type": "string"}, "displayName": "Label", "required": true}}, "rid": "ri.qa.main.action-type.rename-device079", "status": "EXPERIMENTAL"}}, "interfaceTypes": {"Inspectable079": {"allExtendsInterfaces": [], "allLinks": {"inspectedPeers079": {"apiName": "inspectedPeers079", "cardinality": "MANY", "displayName": "Inspected peers", "linkedEntityApiName": {"apiName": "Inspectable079", "type": "interfaceTypeApiName"}, "required": true, "rid": "ri.qa.main.interface-link-type.inspectables079"}}, "allProperties": {"deviceId": {"apiName": "deviceId", "dataType": {"type": "string"}, "displayName": "deviceId", "required": true, "rid": "ri.qa.main.shared-property.deviceId", "type": "interfaceSharedPropertyType"}, "label": {"apiName": "label", "dataType": {"type": "string"}, "displayName": "label", "required": true, "rid": "ri.qa.main.shared-property.label", "type": "interfaceSharedPropertyType"}, "recordedAt": {"apiName": "recordedAt", "dataType": {"type": "timestamp"}, "displayName": "recordedAt", "required": true, "rid": "ri.qa.main.shared-property.recordedAt", "type": "interfaceSharedPropertyType"}}, "allPropertiesV2": {"deviceId": {"apiName": "deviceId", "dataType": {"type": "string"}, "displayName": "deviceId", "requireImplementation": true, "rid": "ri.qa.main.shared-property.deviceId"}, "label": {"apiName": "label", "dataType": {"type": "string"}, "displayName": "label", "requireImplementation": true, "rid": "ri.qa.main.shared-property.label"}, "recordedAt": {"apiName": "recordedAt", "dataType": {"type": "timestamp"}, "displayName": "recordedAt", "requireImplementation": true, "rid": "ri.qa.main.shared-property.recordedAt"}}, "apiName": "Inspectable079", "displayName": "Inspectable", "extendsInterfaces": [], "implementedByObjectTypes": ["Device079"], "links": {"inspectedPeers079": {"apiName": "inspectedPeers079", "cardinality": "MANY", "displayName": "Inspected peers", "linkedEntityApiName": {"apiName": "Inspectable079", "type": "interfaceTypeApiName"}, "required": true, "rid": "ri.qa.main.interface-link-type.inspectables079"}}, "properties": {"deviceId": {"apiName": "deviceId", "dataType": {"type": "string"}, "displayName": "deviceId", "required": true, "rid": "ri.qa.main.shared-property.deviceId", "type": "interfaceSharedPropertyType"}, "label": {"apiName": "label", "dataType": {"type": "string"}, "displayName": "label", "required": true, "rid": "ri.qa.main.shared-property.label", "type": "interfaceSharedPropertyType"}, "recordedAt": {"apiName": "recordedAt", "dataType": {"type": "timestamp"}, "displayName": "recordedAt", "required": true, "rid": "ri.qa.main.shared-property.recordedAt", "type": "interfaceSharedPropertyType"}}, "propertiesV2": {"deviceId": {"apiName": "deviceId", "dataType": {"type": "string"}, "displayName": "deviceId", "required": true, "rid": "ri.qa.main.shared-property.deviceId", "type": "interfaceSharedPropertyType"}, "label": {"apiName": "label", "dataType": {"type": "string"}, "displayName": "label", "required": true, "rid": "ri.qa.main.shared-property.label", "type": "interfaceSharedPropertyType"}, "recordedAt": {"apiName": "recordedAt", "dataType": {"type": "timestamp"}, "displayName": "recordedAt", "required": true, "rid": "ri.qa.main.shared-property.recordedAt", "type": "interfaceSharedPropertyType"}}, "rid": "ri.qa.main.interface-type.inspectable079"}}, "objectTypes": {"Device079": {"implementsInterfaces": ["Inspectable079"], "implementsInterfaces2": {"Inspectable079": {"apiName": "Inspectable079", "links": {"inspectedPeers079": ["relatedDevices079"]}, "properties": {"deviceId": "deviceId", "label": "label", "recordedAt": "recordedAt"}, "propertiesV2": {"deviceId": {"propertyApiName": "deviceId", "type": "localPropertyImplementation"}, "label": {"propertyApiName": "label", "type": "localPropertyImplementation"}, "recordedAt": {"propertyApiName": "recordedAt", "type": "localPropertyImplementation"}}, "rid": "ri.qa.main.interface-type.inspectable079"}}, "linkTypes": [{"apiName": "relatedDevices079", "cardinality": "MANY", "displayName": "Related devices", "linkTypeRid": "ri.qa.main.link-type.related-devices079", "objectTypeApiName": "Device079", "status": "EXPERIMENTAL"}], "objectType": {"apiName": "Device079", "displayName": "Inspection device", "icon": {"color": "#126734", "name": "wrench", "type": "blueprint"}, "pluralDisplayName": "Inspection devices", "primaryKey": "deviceId", "properties": {"deviceId": {"dataType": {"type": "string"}, "rid": "ri.qa.main.property.deviceId"}, "label": {"dataType": {"type": "string"}, "rid": "ri.qa.main.property.label"}, "recordedAt": {"dataType": {"type": "timestamp"}, "rid": "ri.qa.main.property.recordedAt"}}, "rid": "ri.qa.main.object-type.device079", "status": "EXPERIMENTAL", "titleProperty": "label"}, "sharedPropertyTypeMapping": {"deviceId": "deviceId", "label": "label", "recordedAt": "recordedAt"}}}, "ontology": {"apiName": "qa-ontology079", "description": "Synthetic inspection metadata", "displayName": "QA Ontology 079", "rid": "ri.qa.main.ontology.inspection079"}, "queryTypes": {"countDevices079": {"apiName": "countDevices079", "output": {"type": "integer"}, "parameters": {"labelPrefix": {"dataType": {"type": "string"}, "required": true}}, "rid": "ri.qa.main.query-type.count-devices079", "typeReferences": {}, "version": "2.3.0"}}, "sharedPropertyTypes": {"deviceId": {"apiName": "deviceId", "dataType": {"type": "string"}, "displayName": "deviceId", "rid": "ri.qa.main.shared-property.deviceId"}, "label": {"apiName": "label", "dataType": {"type": "string"}, "displayName": "label", "rid": "ri.qa.main.shared-property.label"}, "recordedAt": {"apiName": "recordedAt", "dataType": {"type": "timestamp"}, "displayName": "recordedAt", "rid": "ri.qa.main.shared-property.recordedAt"}}, "valueTypes": {"InspectionDate079": {"apiName": "InspectionDate079", "constraints": [], "displayName": "Inspection date", "fieldType": {"type": "date"}, "rid": "ri.qa.main.value-type.inspection-date079", "version": "3"}}}
      """
    And runtime response type is foundry_sdk.v2.ontologies.models.OntologyFullMetadata
    And nested schema category is ontology_full
    And source named SDK error union is empty
    And exact adverse outcomes are
      """
      {"generic_403": {"class": "PermissionDeniedError", "errorName": "IndependentDenied079", "requests": 1}, "invalid_timeout": {"exception": "pydantic.ValidationError", "request_timeout": 0, "requests": 0}, "paging": {"budget": "three-distinct-cursors-partial-retain", "empty": "complete", "empty_with_continuation": "continue-until-next-data", "enabled": false, "item_budget": 1, "page_budget": 3, "repeated_cursor": "stop-retain"}, "stream": {"async_cancel": true, "caller_consumed_byte_limit": 4, "closed": true, "interrupted": true, "transport_chunk_may_be_larger": true, "unread": true}, "timeout": {"cause": "httpx.ReadTimeout", "class": "ReadTimeout", "replay": false, "requests": 1}}
      """
    And caller consumes at most four stream bytes, retains partial bytes and closes response even when transport chunk is larger

  Scenario: F079-OntologyInterface-aggregate
    Given SDK1.101.0, frozen published reader, fake identity, independently declared Device079/Inspectable079 schema and denied public network
    When Invoke v2.ontologies.OntologyInterface.aggregate in six native forms with exact kwargs below
    Then Match exact wire and typed nested result; generic403/timeout each send once; zero timeout sends nothing; unread/interrupted/canceled responses close
    And API v2 release stage is Private Beta
    And exact SDK inputs are
      """
      {"accuracy": "ALLOW_APPROXIMATE", "aggregation": [{"field": "deviceId", "name": "uniqueDevices079", "type": "approximateDistinct"}], "branch": "qa-branch079", "group_by": [{"field": "recordedAt", "type": "duration", "unit": "DAYS", "value": 2}], "interface_type": "Inspectable079", "ontology": "qa-ontology079", "preview": true}
      """
    And exact HTTP expectation is
      """
      {"body": {"accuracy": "ALLOW_APPROXIMATE", "aggregation": [{"field": "deviceId", "name": "uniqueDevices079", "type": "approximateDistinct"}], "groupBy": [{"field": "recordedAt", "type": "duration", "unit": "DAYS", "value": 2}]}, "headers": {"Accept": "application/json", "Content-Type": "application/json"}, "method": "POST", "path": "/v2/ontologies/qa-ontology079/interfaces/Inspectable079/aggregate", "query": {"branch": "qa-branch079", "preview": true}}
      """
    And exact decoded response is
      """
      {"accuracy": "APPROXIMATE", "data": [{"group": {"recordedAt": "2026-11-16T00:00:00Z"}, "metrics": [{"name": "uniqueDevices079", "value": 2}]}]}
      """
    And runtime response type is foundry_sdk.v2.ontologies.models.AggregateObjectsResponseV2
    And nested schema category is aggregate_schema
    And source named SDK error union is empty
    And exact adverse outcomes are
      """
      {"generic_403": {"class": "PermissionDeniedError", "errorName": "IndependentDenied079", "requests": 1}, "invalid_timeout": {"exception": "pydantic.ValidationError", "request_timeout": 0, "requests": 0}, "paging": {"budget": "three-distinct-cursors-partial-retain", "empty": "complete", "empty_with_continuation": "continue-until-next-data", "enabled": false, "item_budget": 1, "page_budget": 3, "repeated_cursor": "stop-retain"}, "stream": {"async_cancel": true, "caller_consumed_byte_limit": 4, "closed": true, "interrupted": true, "transport_chunk_may_be_larger": true, "unread": true}, "timeout": {"cause": "httpx.ReadTimeout", "class": "ReadTimeout", "replay": false, "requests": 1}}
      """
    And caller consumes at most four stream bytes, retains partial bytes and closes response even when transport chunk is larger

  Scenario: F079-OntologyInterface-get
    Given SDK1.101.0, frozen published reader, fake identity, independently declared Device079/Inspectable079 schema and denied public network
    When Invoke v2.ontologies.OntologyInterface.get in six native forms with exact kwargs below
    Then Match exact wire and typed nested result; generic403/timeout each send once; zero timeout sends nothing; unread/interrupted/canceled responses close
    And API v2 release stage is Public Beta
    And exact SDK inputs are
      """
      {"branch": "qa-branch079", "interface_type": "Inspectable079", "ontology": "qa-ontology079", "preview": true, "sdk_package_rid": "ri.qa.main.sdk.package079", "sdk_version": "0.7.9"}
      """
    And exact HTTP expectation is
      """
      {"body": null, "headers": {"Accept": "application/json"}, "method": "GET", "path": "/v2/ontologies/qa-ontology079/interfaceTypes/Inspectable079", "query": {"branch": "qa-branch079", "preview": true, "sdkPackageRid": "ri.qa.main.sdk.package079", "sdkVersion": "0.7.9"}}
      """
    And exact decoded response is
      """
      {"allExtendsInterfaces": [], "allLinks": {"inspectedPeers079": {"apiName": "inspectedPeers079", "cardinality": "MANY", "displayName": "Inspected peers", "linkedEntityApiName": {"apiName": "Inspectable079", "type": "interfaceTypeApiName"}, "required": true, "rid": "ri.qa.main.interface-link-type.inspectables079"}}, "allProperties": {"deviceId": {"apiName": "deviceId", "dataType": {"type": "string"}, "displayName": "deviceId", "required": true, "rid": "ri.qa.main.shared-property.deviceId", "type": "interfaceSharedPropertyType"}, "label": {"apiName": "label", "dataType": {"type": "string"}, "displayName": "label", "required": true, "rid": "ri.qa.main.shared-property.label", "type": "interfaceSharedPropertyType"}, "recordedAt": {"apiName": "recordedAt", "dataType": {"type": "timestamp"}, "displayName": "recordedAt", "required": true, "rid": "ri.qa.main.shared-property.recordedAt", "type": "interfaceSharedPropertyType"}}, "allPropertiesV2": {"deviceId": {"apiName": "deviceId", "dataType": {"type": "string"}, "displayName": "deviceId", "requireImplementation": true, "rid": "ri.qa.main.shared-property.deviceId"}, "label": {"apiName": "label", "dataType": {"type": "string"}, "displayName": "label", "requireImplementation": true, "rid": "ri.qa.main.shared-property.label"}, "recordedAt": {"apiName": "recordedAt", "dataType": {"type": "timestamp"}, "displayName": "recordedAt", "requireImplementation": true, "rid": "ri.qa.main.shared-property.recordedAt"}}, "apiName": "Inspectable079", "displayName": "Inspectable", "extendsInterfaces": [], "implementedByObjectTypes": ["Device079"], "links": {"inspectedPeers079": {"apiName": "inspectedPeers079", "cardinality": "MANY", "displayName": "Inspected peers", "linkedEntityApiName": {"apiName": "Inspectable079", "type": "interfaceTypeApiName"}, "required": true, "rid": "ri.qa.main.interface-link-type.inspectables079"}}, "properties": {"deviceId": {"apiName": "deviceId", "dataType": {"type": "string"}, "displayName": "deviceId", "required": true, "rid": "ri.qa.main.shared-property.deviceId", "type": "interfaceSharedPropertyType"}, "label": {"apiName": "label", "dataType": {"type": "string"}, "displayName": "label", "required": true, "rid": "ri.qa.main.shared-property.label", "type": "interfaceSharedPropertyType"}, "recordedAt": {"apiName": "recordedAt", "dataType": {"type": "timestamp"}, "displayName": "recordedAt", "required": true, "rid": "ri.qa.main.shared-property.recordedAt", "type": "interfaceSharedPropertyType"}}, "propertiesV2": {"deviceId": {"apiName": "deviceId", "dataType": {"type": "string"}, "displayName": "deviceId", "required": true, "rid": "ri.qa.main.shared-property.deviceId", "type": "interfaceSharedPropertyType"}, "label": {"apiName": "label", "dataType": {"type": "string"}, "displayName": "label", "required": true, "rid": "ri.qa.main.shared-property.label", "type": "interfaceSharedPropertyType"}, "recordedAt": {"apiName": "recordedAt", "dataType": {"type": "timestamp"}, "displayName": "recordedAt", "required": true, "rid": "ri.qa.main.shared-property.recordedAt", "type": "interfaceSharedPropertyType"}}, "rid": "ri.qa.main.interface-type.inspectable079"}
      """
    And runtime response type is foundry_sdk.v2.ontologies.models.InterfaceType
    And nested schema category is interface
    And source named SDK error union is empty
    And exact adverse outcomes are
      """
      {"generic_403": {"class": "PermissionDeniedError", "errorName": "IndependentDenied079", "requests": 1}, "invalid_timeout": {"exception": "pydantic.ValidationError", "request_timeout": 0, "requests": 0}, "paging": {"budget": "three-distinct-cursors-partial-retain", "empty": "complete", "empty_with_continuation": "continue-until-next-data", "enabled": false, "item_budget": 1, "page_budget": 3, "repeated_cursor": "stop-retain"}, "stream": {"async_cancel": true, "caller_consumed_byte_limit": 4, "closed": true, "interrupted": true, "transport_chunk_may_be_larger": true, "unread": true}, "timeout": {"cause": "httpx.ReadTimeout", "class": "ReadTimeout", "replay": false, "requests": 1}}
      """
    And caller consumes at most four stream bytes, retains partial bytes and closes response even when transport chunk is larger

  Scenario: F079-OntologyInterface-get_outgoing_interface_link_type
    Given SDK1.101.0, frozen published reader, fake identity, independently declared Device079/Inspectable079 schema and denied public network
    When Invoke v2.ontologies.OntologyInterface.get_outgoing_interface_link_type in six native forms with exact kwargs below
    Then Match exact wire and typed nested result; generic403/timeout each send once; zero timeout sends nothing; unread/interrupted/canceled responses close
    And API v2 release stage is Private Beta
    And exact SDK inputs are
      """
      {"branch": "qa-branch079", "interface_link_type": "inspectedPeers079", "interface_type": "Inspectable079", "ontology": "qa-ontology079", "preview": true}
      """
    And exact HTTP expectation is
      """
      {"body": null, "headers": {"Accept": "application/json"}, "method": "GET", "path": "/v2/ontologies/qa-ontology079/interfaceTypes/Inspectable079/outgoingLinkTypes/inspectedPeers079", "query": {"branch": "qa-branch079", "preview": true}}
      """
    And exact decoded response is
      """
      {"apiName": "inspectedPeers079", "cardinality": "MANY", "displayName": "Inspected peers", "linkedEntityApiName": {"apiName": "Inspectable079", "type": "interfaceTypeApiName"}, "required": true, "rid": "ri.qa.main.interface-link-type.inspectables079"}
      """
    And runtime response type is foundry_sdk.v2.ontologies.models.InterfaceLinkType
    And nested schema category is interface_link
    And source named SDK error union is empty
    And exact adverse outcomes are
      """
      {"generic_403": {"class": "PermissionDeniedError", "errorName": "IndependentDenied079", "requests": 1}, "invalid_timeout": {"exception": "pydantic.ValidationError", "request_timeout": 0, "requests": 0}, "paging": {"budget": "three-distinct-cursors-partial-retain", "empty": "complete", "empty_with_continuation": "continue-until-next-data", "enabled": false, "item_budget": 1, "page_budget": 3, "repeated_cursor": "stop-retain"}, "stream": {"async_cancel": true, "caller_consumed_byte_limit": 4, "closed": true, "interrupted": true, "transport_chunk_may_be_larger": true, "unread": true}, "timeout": {"cause": "httpx.ReadTimeout", "class": "ReadTimeout", "replay": false, "requests": 1}}
      """
    And caller consumes at most four stream bytes, retains partial bytes and closes response even when transport chunk is larger

  Scenario: F079-OntologyInterface-list
    Given SDK1.101.0, frozen published reader, fake identity, independently declared Device079/Inspectable079 schema and denied public network
    When Invoke v2.ontologies.OntologyInterface.list in six native forms with exact kwargs below
    Then Match exact wire and typed nested result; generic403/timeout each send once; zero timeout sends nothing; unread/interrupted/canceled responses close
    And API v2 release stage is Public Beta
    And exact SDK inputs are
      """
      {"branch": "qa-branch079", "ontology": "qa-ontology079", "page_size": 2, "preview": true}
      """
    And exact HTTP expectation is
      """
      {"body": null, "headers": {"Accept": "application/json"}, "method": "GET", "path": "/v2/ontologies/qa-ontology079/interfaceTypes", "query": {"branch": "qa-branch079", "pageSize": 2, "preview": true}}
      """
    And exact decoded response is
      """
      {"data": [{"allExtendsInterfaces": [], "allLinks": {"inspectedPeers079": {"apiName": "inspectedPeers079", "cardinality": "MANY", "displayName": "Inspected peers", "linkedEntityApiName": {"apiName": "Inspectable079", "type": "interfaceTypeApiName"}, "required": true, "rid": "ri.qa.main.interface-link-type.inspectables079"}}, "allProperties": {"deviceId": {"apiName": "deviceId", "dataType": {"type": "string"}, "displayName": "deviceId", "required": true, "rid": "ri.qa.main.shared-property.deviceId", "type": "interfaceSharedPropertyType"}, "label": {"apiName": "label", "dataType": {"type": "string"}, "displayName": "label", "required": true, "rid": "ri.qa.main.shared-property.label", "type": "interfaceSharedPropertyType"}, "recordedAt": {"apiName": "recordedAt", "dataType": {"type": "timestamp"}, "displayName": "recordedAt", "required": true, "rid": "ri.qa.main.shared-property.recordedAt", "type": "interfaceSharedPropertyType"}}, "allPropertiesV2": {"deviceId": {"apiName": "deviceId", "dataType": {"type": "string"}, "displayName": "deviceId", "requireImplementation": true, "rid": "ri.qa.main.shared-property.deviceId"}, "label": {"apiName": "label", "dataType": {"type": "string"}, "displayName": "label", "requireImplementation": true, "rid": "ri.qa.main.shared-property.label"}, "recordedAt": {"apiName": "recordedAt", "dataType": {"type": "timestamp"}, "displayName": "recordedAt", "requireImplementation": true, "rid": "ri.qa.main.shared-property.recordedAt"}}, "apiName": "Inspectable079", "displayName": "Inspectable", "extendsInterfaces": [], "implementedByObjectTypes": ["Device079"], "links": {"inspectedPeers079": {"apiName": "inspectedPeers079", "cardinality": "MANY", "displayName": "Inspected peers", "linkedEntityApiName": {"apiName": "Inspectable079", "type": "interfaceTypeApiName"}, "required": true, "rid": "ri.qa.main.interface-link-type.inspectables079"}}, "properties": {"deviceId": {"apiName": "deviceId", "dataType": {"type": "string"}, "displayName": "deviceId", "required": true, "rid": "ri.qa.main.shared-property.deviceId", "type": "interfaceSharedPropertyType"}, "label": {"apiName": "label", "dataType": {"type": "string"}, "displayName": "label", "required": true, "rid": "ri.qa.main.shared-property.label", "type": "interfaceSharedPropertyType"}, "recordedAt": {"apiName": "recordedAt", "dataType": {"type": "timestamp"}, "displayName": "recordedAt", "required": true, "rid": "ri.qa.main.shared-property.recordedAt", "type": "interfaceSharedPropertyType"}}, "propertiesV2": {"deviceId": {"apiName": "deviceId", "dataType": {"type": "string"}, "displayName": "deviceId", "required": true, "rid": "ri.qa.main.shared-property.deviceId", "type": "interfaceSharedPropertyType"}, "label": {"apiName": "label", "dataType": {"type": "string"}, "displayName": "label", "required": true, "rid": "ri.qa.main.shared-property.label", "type": "interfaceSharedPropertyType"}, "recordedAt": {"apiName": "recordedAt", "dataType": {"type": "timestamp"}, "displayName": "recordedAt", "required": true, "rid": "ri.qa.main.shared-property.recordedAt", "type": "interfaceSharedPropertyType"}}, "rid": "ri.qa.main.interface-type.inspectable079"}]}
      """
    And runtime response type is foundry_sdk.v2.ontologies.models.ListInterfaceTypesResponse
    And nested schema category is interface
    And source named SDK error union is empty
    And exact adverse outcomes are
      """
      {"generic_403": {"class": "PermissionDeniedError", "errorName": "IndependentDenied079", "requests": 1}, "invalid_timeout": {"exception": "pydantic.ValidationError", "request_timeout": 0, "requests": 0}, "paging": {"budget": "three-distinct-cursors-partial-retain", "empty": "complete", "empty_with_continuation": "continue-until-next-data", "enabled": true, "item_budget": 1, "page_budget": 3, "repeated_cursor": "stop-retain"}, "stream": {"async_cancel": true, "caller_consumed_byte_limit": 4, "closed": true, "interrupted": true, "transport_chunk_may_be_larger": true, "unread": true}, "timeout": {"cause": "httpx.ReadTimeout", "class": "ReadTimeout", "replay": false, "requests": 1}}
      """
    And terminal empty page completes; intermediate empty page follows continuation to next data
    And repeated cursor stops; three distinct cursor pages or one-item budget retains partial items and continuation
    And caller consumes at most four stream bytes, retains partial bytes and closes response even when transport chunk is larger

  Scenario: F079-OntologyInterface-list_interface_linked_objects
    Given SDK1.101.0, frozen published reader, fake identity, independently declared Device079/Inspectable079 schema and denied public network
    When Invoke v2.ontologies.OntologyInterface.list_interface_linked_objects in six native forms with exact kwargs below
    Then Match exact wire and typed nested result; generic403/timeout each send once; zero timeout sends nothing; unread/interrupted/canceled responses close
    And API v2 release stage is Private Beta
    And exact SDK inputs are
      """
      {"branch": "qa-branch079", "exclude_rid": false, "interface_link_type": "inspectedPeers079", "interface_type": "Inspectable079", "object_type": "Device079", "ontology": "qa-ontology079", "page_size": 2, "preview": true, "primary_key": "D-079", "select": ["deviceId", "label", "recordedAt"], "snapshot": true}
      """
    And exact HTTP expectation is
      """
      {"body": null, "headers": {"Accept": "application/json"}, "method": "GET", "path": "/v2/ontologies/qa-ontology079/interfaces/Inspectable079/Device079/D-079/links/inspectedPeers079", "query": {"branch": "qa-branch079", "excludeRid": false, "pageSize": 2, "preview": true, "select": ["deviceId", "label", "recordedAt"], "snapshot": true}}
      """
    And exact decoded response is
      """
      {"data": [{"__apiName": "Device079", "__primaryKey": "D-080", "__rid": "ri.qa.main.object.D-080", "deviceId": "D-080", "label": "Device D-080", "recordedAt": "2026-11-16T08:00:00Z"}]}
      """
    And runtime response type is foundry_sdk.v2.ontologies.models.ListInterfaceLinkedObjectsResponse
    And nested schema category is object_record
    And source named SDK error union is empty
    And exact adverse outcomes are
      """
      {"generic_403": {"class": "PermissionDeniedError", "errorName": "IndependentDenied079", "requests": 1}, "invalid_timeout": {"exception": "pydantic.ValidationError", "request_timeout": 0, "requests": 0}, "paging": {"budget": "three-distinct-cursors-partial-retain", "empty": "complete", "empty_with_continuation": "continue-until-next-data", "enabled": true, "item_budget": 1, "page_budget": 3, "repeated_cursor": "stop-retain"}, "stream": {"async_cancel": true, "caller_consumed_byte_limit": 4, "closed": true, "interrupted": true, "transport_chunk_may_be_larger": true, "unread": true}, "timeout": {"cause": "httpx.ReadTimeout", "class": "ReadTimeout", "replay": false, "requests": 1}}
      """
    And terminal empty page completes; intermediate empty page follows continuation to next data
    And repeated cursor stops; three distinct cursor pages or one-item budget retains partial items and continuation
    And caller consumes at most four stream bytes, retains partial bytes and closes response even when transport chunk is larger

  Scenario: F079-OntologyInterface-list_objects_for_interface
    Given SDK1.101.0, frozen published reader, fake identity, independently declared Device079/Inspectable079 schema and denied public network
    When Invoke v2.ontologies.OntologyInterface.list_objects_for_interface in six native forms with exact kwargs below
    Then Match exact wire and typed nested result; generic403/timeout each send once; zero timeout sends nothing; unread/interrupted/canceled responses close
    And API v2 release stage is Private Beta
    And exact SDK inputs are
      """
      {"branch": "qa-branch079", "exclude_rid": false, "interface_type": "Inspectable079", "ontology": "qa-ontology079", "page_size": 2, "preview": true, "select": ["deviceId", "label", "recordedAt"], "snapshot": true}
      """
    And exact HTTP expectation is
      """
      {"body": null, "headers": {"Accept": "application/json"}, "method": "GET", "path": "/v2/ontologies/qa-ontology079/interfaces/Inspectable079", "query": {"branch": "qa-branch079", "excludeRid": false, "pageSize": 2, "preview": true, "select": ["deviceId", "label", "recordedAt"], "snapshot": true}}
      """
    And exact decoded response is
      """
      {"data": [{"__apiName": "Device079", "__primaryKey": "D-079", "__rid": "ri.qa.main.object.D-079", "deviceId": "D-079", "label": "Device D-079", "recordedAt": "2026-11-16T08:00:00Z"}], "totalCount": "1"}
      """
    And runtime response type is foundry_sdk.v2.ontologies.models.ListObjectsForInterfaceResponse
    And nested schema category is object_record
    And source named SDK error union is empty
    And exact adverse outcomes are
      """
      {"generic_403": {"class": "PermissionDeniedError", "errorName": "IndependentDenied079", "requests": 1}, "invalid_timeout": {"exception": "pydantic.ValidationError", "request_timeout": 0, "requests": 0}, "paging": {"budget": "three-distinct-cursors-partial-retain", "empty": "complete", "empty_with_continuation": "continue-until-next-data", "enabled": true, "item_budget": 1, "page_budget": 3, "repeated_cursor": "stop-retain"}, "stream": {"async_cancel": true, "caller_consumed_byte_limit": 4, "closed": true, "interrupted": true, "transport_chunk_may_be_larger": true, "unread": true}, "timeout": {"cause": "httpx.ReadTimeout", "class": "ReadTimeout", "replay": false, "requests": 1}}
      """
    And terminal empty page completes; intermediate empty page follows continuation to next data
    And repeated cursor stops; three distinct cursor pages or one-item budget retains partial items and continuation
    And caller consumes at most four stream bytes, retains partial bytes and closes response even when transport chunk is larger

  Scenario: F079-OntologyInterface-list_outgoing_interface_link_types
    Given SDK1.101.0, frozen published reader, fake identity, independently declared Device079/Inspectable079 schema and denied public network
    When Invoke v2.ontologies.OntologyInterface.list_outgoing_interface_link_types in six native forms with exact kwargs below
    Then Match exact wire and typed nested result; generic403/timeout each send once; zero timeout sends nothing; unread/interrupted/canceled responses close
    And API v2 release stage is Private Beta
    And exact SDK inputs are
      """
      {"branch": "qa-branch079", "interface_type": "Inspectable079", "ontology": "qa-ontology079", "preview": true}
      """
    And exact HTTP expectation is
      """
      {"body": null, "headers": {"Accept": "application/json"}, "method": "GET", "path": "/v2/ontologies/qa-ontology079/interfaceTypes/Inspectable079/outgoingLinkTypes", "query": {"branch": "qa-branch079", "preview": true}}
      """
    And exact decoded response is
      """
      {"data": [{"apiName": "inspectedPeers079", "cardinality": "MANY", "displayName": "Inspected peers", "linkedEntityApiName": {"apiName": "Inspectable079", "type": "interfaceTypeApiName"}, "required": true, "rid": "ri.qa.main.interface-link-type.inspectables079"}]}
      """
    And runtime response type is foundry_sdk.v2.ontologies.models.ListOutgoingInterfaceLinkTypesResponse
    And nested schema category is interface_link
    And source named SDK error union is empty
    And exact adverse outcomes are
      """
      {"generic_403": {"class": "PermissionDeniedError", "errorName": "IndependentDenied079", "requests": 1}, "invalid_timeout": {"exception": "pydantic.ValidationError", "request_timeout": 0, "requests": 0}, "paging": {"budget": "three-distinct-cursors-partial-retain", "empty": "complete", "empty_with_continuation": "continue-until-next-data", "enabled": false, "item_budget": 1, "page_budget": 3, "repeated_cursor": "stop-retain"}, "stream": {"async_cancel": true, "caller_consumed_byte_limit": 4, "closed": true, "interrupted": true, "transport_chunk_may_be_larger": true, "unread": true}, "timeout": {"cause": "httpx.ReadTimeout", "class": "ReadTimeout", "replay": false, "requests": 1}}
      """
    And caller consumes at most four stream bytes, retains partial bytes and closes response even when transport chunk is larger

  Scenario: F079-OntologyInterface-search
    Given SDK1.101.0, frozen published reader, fake identity, independently declared Device079/Inspectable079 schema and denied public network
    When Invoke v2.ontologies.OntologyInterface.search in six native forms with exact kwargs below
    Then Match exact wire and typed nested result; generic403/timeout each send once; zero timeout sends nothing; unread/interrupted/canceled responses close
    And API v2 release stage is Private Beta
    And exact SDK inputs are
      """
      {"augmented_interface_property_types": {}, "augmented_properties": {}, "augmented_shared_property_types": {}, "branch": "qa-branch079", "interface_type": "Inspectable079", "ontology": "qa-ontology079", "other_interface_types": [], "page_size": 2, "preview": true, "selected_interface_property_types": [], "selected_object_types": ["Device079"], "selected_shared_property_types": ["deviceId", "label", "recordedAt"], "where": {"field": "label", "type": "eq", "value": "Device D-079"}}
      """
    And exact HTTP expectation is
      """
      {"body": {"augmentedInterfacePropertyTypes": {}, "augmentedProperties": {}, "augmentedSharedPropertyTypes": {}, "otherInterfaceTypes": [], "pageSize": 2, "selectedInterfacePropertyTypes": [], "selectedObjectTypes": ["Device079"], "selectedSharedPropertyTypes": ["deviceId", "label", "recordedAt"], "where": {"field": "label", "type": "eq", "value": "Device D-079"}}, "headers": {"Accept": "application/json", "Content-Type": "application/json"}, "method": "POST", "path": "/v2/ontologies/qa-ontology079/interfaces/Inspectable079/search", "query": {"branch": "qa-branch079", "preview": true}}
      """
    And exact decoded response is
      """
      {"data": [{"__apiName": "Device079", "__primaryKey": "D-079", "__rid": "ri.qa.main.object.D-079", "deviceId": "D-079", "label": "Device D-079", "recordedAt": "2026-11-16T08:00:00Z"}], "totalCount": "1"}
      """
    And runtime response type is foundry_sdk.v2.ontologies.models.SearchObjectsResponseV2
    And nested schema category is object_record
    And source named SDK error union is empty
    And exact adverse outcomes are
      """
      {"generic_403": {"class": "PermissionDeniedError", "errorName": "IndependentDenied079", "requests": 1}, "invalid_timeout": {"exception": "pydantic.ValidationError", "request_timeout": 0, "requests": 0}, "paging": {"budget": "three-distinct-cursors-partial-retain", "empty": "complete", "empty_with_continuation": "continue-until-next-data", "enabled": true, "item_budget": 1, "page_budget": 3, "repeated_cursor": "stop-retain"}, "stream": {"async_cancel": true, "caller_consumed_byte_limit": 4, "closed": true, "interrupted": true, "transport_chunk_may_be_larger": true, "unread": true}, "timeout": {"cause": "httpx.ReadTimeout", "class": "ReadTimeout", "replay": false, "requests": 1}}
      """
    And terminal empty page completes; intermediate empty page follows continuation to next data
    And repeated cursor stops; three distinct cursor pages or one-item budget retains partial items and continuation
    And caller consumes at most four stream bytes, retains partial bytes and closes response even when transport chunk is larger

  Scenario: F079-OntologyValueType-get
    Given SDK1.101.0, frozen published reader, fake identity, independently declared Device079/Inspectable079 schema and denied public network
    When Invoke v2.ontologies.OntologyValueType.get in six native forms with exact kwargs below
    Then Match exact wire and typed nested result; generic403/timeout each send once; zero timeout sends nothing; unread/interrupted/canceled responses close
    And API v2 release stage is Public Beta
    And exact SDK inputs are
      """
      {"ontology": "qa-ontology079", "preview": true, "value_type": "InspectionDate079"}
      """
    And exact HTTP expectation is
      """
      {"body": null, "headers": {"Accept": "application/json"}, "method": "GET", "path": "/v2/ontologies/qa-ontology079/valueTypes/InspectionDate079", "query": {"preview": true}}
      """
    And exact decoded response is
      """
      {"apiName": "InspectionDate079", "constraints": [], "displayName": "Inspection date", "fieldType": {"type": "date"}, "rid": "ri.qa.main.value-type.inspection-date079", "version": "3"}
      """
    And runtime response type is foundry_sdk.v2.ontologies.models.OntologyValueType
    And nested schema category is value_type
    And source named SDK error union is empty
    And exact adverse outcomes are
      """
      {"generic_403": {"class": "PermissionDeniedError", "errorName": "IndependentDenied079", "requests": 1}, "invalid_timeout": {"exception": "pydantic.ValidationError", "request_timeout": 0, "requests": 0}, "paging": {"budget": "three-distinct-cursors-partial-retain", "empty": "complete", "empty_with_continuation": "continue-until-next-data", "enabled": false, "item_budget": 1, "page_budget": 3, "repeated_cursor": "stop-retain"}, "stream": {"async_cancel": true, "caller_consumed_byte_limit": 4, "closed": true, "interrupted": true, "transport_chunk_may_be_larger": true, "unread": true}, "timeout": {"cause": "httpx.ReadTimeout", "class": "ReadTimeout", "replay": false, "requests": 1}}
      """
    And caller consumes at most four stream bytes, retains partial bytes and closes response even when transport chunk is larger

  Scenario: F079-OntologyValueType-list
    Given SDK1.101.0, frozen published reader, fake identity, independently declared Device079/Inspectable079 schema and denied public network
    When Invoke v2.ontologies.OntologyValueType.list in six native forms with exact kwargs below
    Then Match exact wire and typed nested result; generic403/timeout each send once; zero timeout sends nothing; unread/interrupted/canceled responses close
    And API v2 release stage is Public Beta
    And exact SDK inputs are
      """
      {"ontology": "qa-ontology079", "preview": true}
      """
    And exact HTTP expectation is
      """
      {"body": null, "headers": {"Accept": "application/json"}, "method": "GET", "path": "/v2/ontologies/qa-ontology079/valueTypes", "query": {"preview": true}}
      """
    And exact decoded response is
      """
      {"data": [{"apiName": "InspectionDate079", "constraints": [], "displayName": "Inspection date", "fieldType": {"type": "date"}, "rid": "ri.qa.main.value-type.inspection-date079", "version": "3"}]}
      """
    And runtime response type is foundry_sdk.v2.ontologies.models.ListOntologyValueTypesResponse
    And nested schema category is value_type
    And source named SDK error union is empty
    And exact adverse outcomes are
      """
      {"generic_403": {"class": "PermissionDeniedError", "errorName": "IndependentDenied079", "requests": 1}, "invalid_timeout": {"exception": "pydantic.ValidationError", "request_timeout": 0, "requests": 0}, "paging": {"budget": "three-distinct-cursors-partial-retain", "empty": "complete", "empty_with_continuation": "continue-until-next-data", "enabled": false, "item_budget": 1, "page_budget": 3, "repeated_cursor": "stop-retain"}, "stream": {"async_cancel": true, "caller_consumed_byte_limit": 4, "closed": true, "interrupted": true, "transport_chunk_may_be_larger": true, "unread": true}, "timeout": {"cause": "httpx.ReadTimeout", "class": "ReadTimeout", "replay": false, "requests": 1}}
      """
    And caller consumes at most four stream bytes, retains partial bytes and closes response even when transport chunk is larger

  Scenario: F079-QueryType-get
    Given SDK1.101.0, frozen published reader, fake identity, independently declared Device079/Inspectable079 schema and denied public network
    When Invoke v2.ontologies.QueryType.get in six native forms with exact kwargs below
    Then Match exact wire and typed nested result; generic403/timeout each send once; zero timeout sends nothing; unread/interrupted/canceled responses close
    And API v2 release stage is Stable
    And exact SDK inputs are
      """
      {"ontology": "qa-ontology079", "query_api_name": "countDevices079", "sdk_package_rid": "ri.qa.main.sdk.package079", "sdk_version": "0.7.9", "version": "2.3.0"}
      """
    And exact HTTP expectation is
      """
      {"body": null, "headers": {"Accept": "application/json"}, "method": "GET", "path": "/v2/ontologies/qa-ontology079/queryTypes/countDevices079", "query": {"sdkPackageRid": "ri.qa.main.sdk.package079", "sdkVersion": "0.7.9", "version": "2.3.0"}}
      """
    And exact decoded response is
      """
      {"apiName": "countDevices079", "output": {"type": "integer"}, "parameters": {"labelPrefix": {"dataType": {"type": "string"}, "required": true}}, "rid": "ri.qa.main.query-type.count-devices079", "typeReferences": {}, "version": "2.3.0"}
      """
    And runtime response type is foundry_sdk.v2.ontologies.models.QueryTypeV2
    And nested schema category is query
    And source named SDK error union is empty
    And exact adverse outcomes are
      """
      {"generic_403": {"class": "PermissionDeniedError", "errorName": "IndependentDenied079", "requests": 1}, "invalid_timeout": {"exception": "pydantic.ValidationError", "request_timeout": 0, "requests": 0}, "paging": {"budget": "three-distinct-cursors-partial-retain", "empty": "complete", "empty_with_continuation": "continue-until-next-data", "enabled": false, "item_budget": 1, "page_budget": 3, "repeated_cursor": "stop-retain"}, "stream": {"async_cancel": true, "caller_consumed_byte_limit": 4, "closed": true, "interrupted": true, "transport_chunk_may_be_larger": true, "unread": true}, "timeout": {"cause": "httpx.ReadTimeout", "class": "ReadTimeout", "replay": false, "requests": 1}}
      """
    And caller consumes at most four stream bytes, retains partial bytes and closes response even when transport chunk is larger

  Scenario: F079-QueryType-get_by_rid_batch
    Given SDK1.101.0, frozen published reader, fake identity, independently declared Device079/Inspectable079 schema and denied public network
    When Invoke v2.ontologies.QueryType.get_by_rid_batch in six native forms with exact kwargs below
    Then Match exact wire and typed nested result; generic403/timeout each send once; zero timeout sends nothing; unread/interrupted/canceled responses close
    And API v2 release stage is Private Beta
    And exact SDK inputs are
      """
      {"branch": "qa-branch079", "ontology": "qa-ontology079", "preview": true, "requests": [{"queryTypeRid": "ri.qa.main.query-type.count-devices079"}]}
      """
    And exact HTTP expectation is
      """
      {"body": {"requests": [{"queryTypeRid": "ri.qa.main.query-type.count-devices079"}]}, "headers": {"Accept": "application/json", "Content-Type": "application/json"}, "method": "POST", "path": "/v2/ontologies/qa-ontology079/queryTypes/getByRidBatch", "query": {"branch": "qa-branch079", "preview": true}}
      """
    And exact decoded response is
      """
      {"data": [{"apiName": "countDevices079", "output": {"type": "integer"}, "parameters": {"labelPrefix": {"dataType": {"type": "string"}, "required": true}}, "rid": "ri.qa.main.query-type.count-devices079", "typeReferences": {}, "version": "2.3.0"}]}
      """
    And runtime response type is foundry_sdk.v2.ontologies.models.GetQueryTypeByRidBatchResponse
    And nested schema category is query
    And source named SDK error union is empty
    And exact adverse outcomes are
      """
      {"generic_403": {"class": "PermissionDeniedError", "errorName": "IndependentDenied079", "requests": 1}, "invalid_timeout": {"exception": "pydantic.ValidationError", "request_timeout": 0, "requests": 0}, "paging": {"budget": "three-distinct-cursors-partial-retain", "empty": "complete", "empty_with_continuation": "continue-until-next-data", "enabled": false, "item_budget": 1, "page_budget": 3, "repeated_cursor": "stop-retain"}, "stream": {"async_cancel": true, "caller_consumed_byte_limit": 4, "closed": true, "interrupted": true, "transport_chunk_may_be_larger": true, "unread": true}, "timeout": {"cause": "httpx.ReadTimeout", "class": "ReadTimeout", "replay": false, "requests": 1}}
      """
    And caller consumes at most four stream bytes, retains partial bytes and closes response even when transport chunk is larger

  Scenario: F079-QueryType-list
    Given SDK1.101.0, frozen published reader, fake identity, independently declared Device079/Inspectable079 schema and denied public network
    When Invoke v2.ontologies.QueryType.list in six native forms with exact kwargs below
    Then Match exact wire and typed nested result; generic403/timeout each send once; zero timeout sends nothing; unread/interrupted/canceled responses close
    And API v2 release stage is Stable
    And exact SDK inputs are
      """
      {"branch": "qa-branch079", "ontology": "qa-ontology079", "page_size": 2}
      """
    And exact HTTP expectation is
      """
      {"body": null, "headers": {"Accept": "application/json"}, "method": "GET", "path": "/v2/ontologies/qa-ontology079/queryTypes", "query": {"branch": "qa-branch079", "pageSize": 2}}
      """
    And exact decoded response is
      """
      {"data": [{"apiName": "countDevices079", "output": {"type": "integer"}, "parameters": {"labelPrefix": {"dataType": {"type": "string"}, "required": true}}, "rid": "ri.qa.main.query-type.count-devices079", "typeReferences": {}, "version": "2.3.0"}]}
      """
    And runtime response type is foundry_sdk.v2.ontologies.models.ListQueryTypesResponseV2
    And nested schema category is query
    And source named SDK error union is empty
    And exact adverse outcomes are
      """
      {"generic_403": {"class": "PermissionDeniedError", "errorName": "IndependentDenied079", "requests": 1}, "invalid_timeout": {"exception": "pydantic.ValidationError", "request_timeout": 0, "requests": 0}, "paging": {"budget": "three-distinct-cursors-partial-retain", "empty": "complete", "empty_with_continuation": "continue-until-next-data", "enabled": true, "item_budget": 1, "page_budget": 3, "repeated_cursor": "stop-retain"}, "stream": {"async_cancel": true, "caller_consumed_byte_limit": 4, "closed": true, "interrupted": true, "transport_chunk_may_be_larger": true, "unread": true}, "timeout": {"cause": "httpx.ReadTimeout", "class": "ReadTimeout", "replay": false, "requests": 1}}
      """
    And terminal empty page completes; intermediate empty page follows continuation to next data
    And repeated cursor stops; three distinct cursor pages or one-item budget retains partial items and continuation
    And caller consumes at most four stream bytes, retains partial bytes and closes response even when transport chunk is larger

  Scenario: Source and reader closure
    Given exact32 partition and frozen425 catalog
    When source AST, mode annotations, all model definitions and local links are reconciled
    Then every source definition, operation identity and version route agrees; changed claims fail

  Scenario: Opaque fields and local schema decisions
    Given unknown object or aggregation keys and declared interface schema
    When SDK decodes raw values and reader considers local derivation
    Then retain opaque data and stop unsupported derivation without inventing server rejection

  Scenario: Nested constraint ObjectType.get primary-key-member
    Given independent expected response for v2.ontologies.ObjectType.get
    When path ["primaryKey"] becomes "absent079"
    Then local semantic check rejects this response and records whether source SDK shape validation accepts it
    And no server validation or live execution is claimed

  Scenario: Nested constraint ObjectType.get title-member
    Given independent expected response for v2.ontologies.ObjectType.get
    When path ["titleProperty"] becomes "absent079"
    Then local semantic check rejects this response and records whether source SDK shape validation accepts it
    And no server validation or live execution is claimed

  Scenario: Nested constraint ObjectType.get primary-key-type
    Given independent expected response for v2.ontologies.ObjectType.get
    When path ["properties", "deviceId", "dataType"] becomes {"type": "integer"}
    Then local semantic check rejects this response and records whether source SDK shape validation accepts it
    And no server validation or live execution is claimed

  Scenario: Nested constraint ObjectType.get title-type
    Given independent expected response for v2.ontologies.ObjectType.get
    When path ["properties", "label", "dataType"] becomes {"type": "date"}
    Then local semantic check rejects this response and records whether source SDK shape validation accepts it
    And no server validation or live execution is claimed

  Scenario: Nested constraint ObjectType.get_full_metadata interface-membership
    Given independent expected response for v2.ontologies.ObjectType.get_full_metadata
    When path ["implementsInterfaces"] becomes ["Unknown079"]
    Then local semantic check rejects this response and records whether source SDK shape validation accepts it
    And no server validation or live execution is claimed

  Scenario: Nested constraint ObjectType.get_full_metadata backing-property
    Given independent expected response for v2.ontologies.ObjectType.get_full_metadata
    When path ["implementsInterfaces2", "Inspectable079", "properties", "deviceId"] becomes "absent079"
    Then local semantic check rejects this response and records whether source SDK shape validation accepts it
    And no server validation or live execution is claimed

  Scenario: Nested constraint ObjectType.get_full_metadata link-implementation
    Given independent expected response for v2.ontologies.ObjectType.get_full_metadata
    When path ["implementsInterfaces2", "Inspectable079", "links"] becomes {"inspectedPeers079": ["missing079"]}
    Then local semantic check rejects this response and records whether source SDK shape validation accepts it
    And no server validation or live execution is claimed

  Scenario: Nested constraint ObjectType.get_full_metadata property-implementation-discriminator
    Given independent expected response for v2.ontologies.ObjectType.get_full_metadata
    When path ["implementsInterfaces2", "Inspectable079", "propertiesV2", "label", "type"] becomes "unknown079"
    Then local semantic check rejects this response and records whether source SDK shape validation accepts it
    And no server validation or live execution is claimed

  Scenario: Nested constraint OntologyInterface.get inheritance-self-cycle
    Given independent expected response for v2.ontologies.OntologyInterface.get
    When path ["extendsInterfaces"] becomes ["Inspectable079"]
    Then local semantic check rejects this response and records whether source SDK shape validation accepts it
    And no server validation or live execution is claimed

  Scenario: Nested constraint OntologyInterface.get inherited-member-type
    Given independent expected response for v2.ontologies.OntologyInterface.get
    When path ["allProperties", "label", "dataType"] becomes {"type": "integer"}
    Then local semantic check rejects this response and records whether source SDK shape validation accepts it
    And no server validation or live execution is claimed

  Scenario: Nested constraint OntologyInterface.get required-member
    Given independent expected response for v2.ontologies.OntologyInterface.get
    When path ["propertiesV2", "deviceId", "required"] becomes false
    Then local semantic check rejects this response and records whether source SDK shape validation accepts it
    And no server validation or live execution is claimed

  Scenario: Nested constraint OntologyInterface.get implementation-required
    Given independent expected response for v2.ontologies.OntologyInterface.get
    When path ["allPropertiesV2", "deviceId", "requireImplementation"] becomes false
    Then local semantic check rejects this response and records whether source SDK shape validation accepts it
    And no server validation or live execution is claimed

  Scenario: Nested constraint OntologyInterface.get link-target
    Given independent expected response for v2.ontologies.OntologyInterface.get
    When path ["links", "inspectedPeers079", "linkedEntityApiName", "apiName"] becomes "Unknown079"
    Then local semantic check rejects this response and records whether source SDK shape validation accepts it
    And no server validation or live execution is claimed

  Scenario: Nested constraint ActionType.get parameter-type
    Given independent expected response for v2.ontologies.ActionType.get
    When path ["parameters", "device", "dataType", "interfaceTypeApiName"] becomes "Unknown079"
    Then local semantic check rejects this response and records whether source SDK shape validation accepts it
    And no server validation or live execution is claimed

  Scenario: Nested constraint ActionTypeFullMetadata.get summary-discriminator
    Given independent expected response for v2.ontologies.ActionTypeFullMetadata.get
    When path ["actionType", "operations", 0, "type"] becomes "modifyInterface"
    Then local semantic check rejects this response and records whether source SDK shape validation accepts it
    And no server validation or live execution is claimed

  Scenario: Nested constraint ActionTypeFullMetadata.get full-rule-discriminator
    Given independent expected response for v2.ontologies.ActionTypeFullMetadata.get
    When path ["fullLogicRules", 0, "type"] becomes "modifyInterfaceObject"
    Then local semantic check rejects this response and records whether source SDK shape validation accepts it
    And no server validation or live execution is claimed

  Scenario: Nested constraint ActionTypeFullMetadata.get rule-target-reference
    Given independent expected response for v2.ontologies.ActionTypeFullMetadata.get
    When path ["fullLogicRules", 0, "interfaceObjectToModify"] becomes "absent079"
    Then local semantic check rejects this response and records whether source SDK shape validation accepts it
    And no server validation or live execution is claimed

  Scenario: Nested constraint ActionTypeFullMetadata.get rule-property-parameter-reference
    Given independent expected response for v2.ontologies.ActionTypeFullMetadata.get
    When path ["fullLogicRules", 0, "sharedPropertyArguments", "label", "parameterId"] becomes "absent079"
    Then local semantic check rejects this response and records whether source SDK shape validation accepts it
    And no server validation or live execution is claimed

  Scenario: Nested constraint ObjectType.get_edits_history typed-history-key
    Given independent expected response for v2.ontologies.ObjectType.get_edits_history
    When path ["data", 0, "objectPrimaryKey", "deviceId", "type"] becomes "integerValue"
    Then local semantic check rejects this response and records whether source SDK shape validation accepts it
    And no server validation or live execution is claimed

  Scenario: Nested constraint ObjectType.get_edits_history plain-create-key
    Given independent expected response for v2.ontologies.ObjectType.get_edits_history
    When path ["data", 0, "edit", "properties", "deviceId"] becomes {"type": "stringValue", "value": "D-079"}
    Then local semantic check rejects this response and records whether source SDK shape validation accepts it
    And no server validation or live execution is claimed

  Scenario: Nested constraint OntologyValueType.get date-versus-struct
    Given independent expected response for v2.ontologies.OntologyValueType.get
    When path ["constraints"] becomes [{"type": "struct", "properties": {}}]
    Then local semantic check rejects this response and records whether source SDK shape validation accepts it
    And no server validation or live execution is claimed

  Scenario: Nested constraint OntologyValueType.get value-type-version
    Given independent expected response for v2.ontologies.OntologyValueType.get
    When path ["version"] becomes "4"
    Then local semantic check rejects this response and records whether source SDK shape validation accepts it
    And no server validation or live execution is claimed

  Scenario: Nested constraint QueryType.get query-version
    Given independent expected response for v2.ontologies.QueryType.get
    When path ["version"] becomes "9.9.9"
    Then local semantic check rejects this response and records whether source SDK shape validation accepts it
    And no server validation or live execution is claimed
