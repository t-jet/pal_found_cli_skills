Feature: Frozen SDK v1 Ontology operations in an isolated fake-HTTP enrollment
  Background:
    Given prepared SDK 1.101.0 and public sockets denied
    And synthetic Flight and Airport metadata with distinct primary keys
    And frozen local contracts, behavior, examples and transitive models

  Scenario Outline: F077-01 v1.ontologies.Action.apply complete wire and result
    Given source bindings and frozen assets for v1.ontologies.Action.apply
    When SDK runs <mode> with case JSON literal kwargs
    Then request equals POST /v1/ontologies/ri.qa.main.ontology.flight077/actions/schedule-flight/apply
    And query, headers, body and seven-second timeout equal literal wire oracle
    And response equals case JSON literal payload with tenant-schema meaning preserved
    And response and client close on successful completion
    And ordinary sync/async 403 and timeout preserve failure identity
    And raw sync/async consumer failures and applicable malformed JSON decode failures close resources
    And streaming sync/async consumer exceptions and async cancellation close resources
    And sync/async zero timeout rejects before HTTP
    Examples:
      | mode |
      | sync_ordinary |
      | sync_raw |
      | sync_streaming |
      | async_ordinary |
      | async_raw |
      | async_streaming |

  Scenario: F077-01 generic failures and validation
    Given source declares zero named throwable errors
    When fake HTTP denies permission with generic 403 envelope
    Then SDK preserves error identity and makes one request
    When fake HTTP raises timeout
    Then SDK reports transport failure without replay
    When request_timeout is zero
    Then SDK rejects input before HTTP

  Scenario Outline: F077-02 v1.ontologies.Action.apply_batch complete wire and result
    Given source bindings and frozen assets for v1.ontologies.Action.apply_batch
    When SDK runs <mode> with case JSON literal kwargs
    Then request equals POST /v1/ontologies/ri.qa.main.ontology.flight077/actions/schedule-flight/applyBatch
    And query, headers, body and seven-second timeout equal literal wire oracle
    And response equals case JSON literal payload with tenant-schema meaning preserved
    And response and client close on successful completion
    And ordinary sync/async 403 and timeout preserve failure identity
    And raw sync/async consumer failures and applicable malformed JSON decode failures close resources
    And streaming sync/async consumer exceptions and async cancellation close resources
    And sync/async zero timeout rejects before HTTP
    Examples:
      | mode |
      | sync_ordinary |
      | sync_raw |
      | sync_streaming |
      | async_ordinary |
      | async_raw |
      | async_streaming |

  Scenario: F077-02 generic failures and validation
    Given source declares zero named throwable errors
    When fake HTTP denies permission with generic 403 envelope
    Then SDK preserves error identity and makes one request
    When fake HTTP raises timeout
    Then SDK reports transport failure without replay
    When request_timeout is zero
    Then SDK rejects input before HTTP

  Scenario Outline: F077-03 v1.ontologies.Action.validate complete wire and result
    Given source bindings and frozen assets for v1.ontologies.Action.validate
    When SDK runs <mode> with case JSON literal kwargs
    Then request equals POST /v1/ontologies/ri.qa.main.ontology.flight077/actions/schedule-flight/validate
    And query, headers, body and seven-second timeout equal literal wire oracle
    And response equals case JSON literal payload with tenant-schema meaning preserved
    And response and client close on successful completion
    And ordinary sync/async 403 and timeout preserve failure identity
    And raw sync/async consumer failures and applicable malformed JSON decode failures close resources
    And streaming sync/async consumer exceptions and async cancellation close resources
    And sync/async zero timeout rejects before HTTP
    Examples:
      | mode |
      | sync_ordinary |
      | sync_raw |
      | sync_streaming |
      | async_ordinary |
      | async_raw |
      | async_streaming |

  Scenario: F077-03 generic failures and validation
    Given source declares zero named throwable errors
    When fake HTTP denies permission with generic 403 envelope
    Then SDK preserves error identity and makes one request
    When fake HTTP raises timeout
    Then SDK reports transport failure without replay
    When request_timeout is zero
    Then SDK rejects input before HTTP

  Scenario Outline: F077-04 v1.ontologies.ActionType.get complete wire and result
    Given source bindings and frozen assets for v1.ontologies.ActionType.get
    When SDK runs <mode> with case JSON literal kwargs
    Then request equals GET /v1/ontologies/ri.qa.main.ontology.flight077/actionTypes/schedule-flight
    And query, headers, body and seven-second timeout equal literal wire oracle
    And response equals case JSON literal payload with tenant-schema meaning preserved
    And response and client close on successful completion
    And ordinary sync/async 403 and timeout preserve failure identity
    And raw sync/async consumer failures and applicable malformed JSON decode failures close resources
    And streaming sync/async consumer exceptions and async cancellation close resources
    And sync/async zero timeout rejects before HTTP
    Examples:
      | mode |
      | sync_ordinary |
      | sync_raw |
      | sync_streaming |
      | async_ordinary |
      | async_raw |
      | async_streaming |

  Scenario: F077-04 generic failures and validation
    Given source declares zero named throwable errors
    When fake HTTP denies permission with generic 403 envelope
    Then SDK preserves error identity and makes one request
    When fake HTTP raises timeout
    Then SDK reports transport failure without replay
    When request_timeout is zero
    Then SDK rejects input before HTTP

  Scenario Outline: F077-05 v1.ontologies.ActionType.list complete wire and result
    Given source bindings and frozen assets for v1.ontologies.ActionType.list
    When SDK runs <mode> with case JSON literal kwargs
    Then request equals GET /v1/ontologies/ri.qa.main.ontology.flight077/actionTypes
    And query, headers, body and seven-second timeout equal literal wire oracle
    And response equals case JSON literal payload with tenant-schema meaning preserved
    And response and client close on successful completion
    And ordinary sync/async 403 and timeout preserve failure identity
    And raw sync/async consumer failures and applicable malformed JSON decode failures close resources
    And streaming sync/async consumer exceptions and async cancellation close resources
    And sync/async zero timeout rejects before HTTP
    Examples:
      | mode |
      | sync_ordinary |
      | sync_raw |
      | sync_streaming |
      | async_ordinary |
      | async_raw |
      | async_streaming |

  Scenario: F077-05 generic failures and validation
    Given source declares zero named throwable errors
    When fake HTTP denies permission with generic 403 envelope
    Then SDK preserves error identity and makes one request
    When fake HTTP raises timeout
    Then SDK reports transport failure without replay
    When request_timeout is zero
    Then SDK rejects input before HTTP

  Scenario: F077-05 finite paging
    Given two pages with distinct objects or schema identities
    When ordinary iterator or explicit search continuation advances
    Then exactly two requests retain initial filters and token placement
    And repeated token and page/item bounds preserve partial results
    And stopping after one item causes no next request

  Scenario Outline: F077-06 v1.ontologies.Attachment.get complete wire and result
    Given source bindings and frozen assets for v1.ontologies.Attachment.get
    When SDK runs <mode> with case JSON literal kwargs
    Then request equals GET /v1/attachments/ri.qa.main.attachment.flight077
    And query, headers, body and seven-second timeout equal literal wire oracle
    And response equals case JSON literal payload with tenant-schema meaning preserved
    And response and client close on successful completion
    And ordinary sync/async 403 and timeout preserve failure identity
    And raw sync/async consumer failures and applicable malformed JSON decode failures close resources
    And streaming sync/async consumer exceptions and async cancellation close resources
    And sync/async zero timeout rejects before HTTP
    Examples:
      | mode |
      | sync_ordinary |
      | sync_raw |
      | sync_streaming |
      | async_ordinary |
      | async_raw |
      | async_streaming |

  Scenario: F077-06 generic failures and validation
    Given source declares zero named throwable errors
    When fake HTTP denies permission with generic 403 envelope
    Then SDK preserves error identity and makes one request
    When fake HTTP raises timeout
    Then SDK reports transport failure without replay
    When request_timeout is zero
    Then SDK rejects input before HTTP

  Scenario Outline: F077-07 v1.ontologies.Attachment.read complete wire and result
    Given source bindings and frozen assets for v1.ontologies.Attachment.read
    When SDK runs <mode> with case JSON literal kwargs
    Then request equals GET /v1/attachments/ri.qa.main.attachment.flight077/content
    And query, headers, body and seven-second timeout equal literal wire oracle
    And response equals case JSON literal payload with tenant-schema meaning preserved
    And response and client close on successful completion
    And ordinary sync/async 403 and timeout preserve failure identity
    And raw sync/async consumer failures and applicable malformed JSON decode failures close resources
    And streaming sync/async consumer exceptions and async cancellation close resources
    And sync/async zero timeout rejects before HTTP
    Examples:
      | mode |
      | sync_ordinary |
      | sync_raw |
      | sync_streaming |
      | async_ordinary |
      | async_raw |
      | async_streaming |

  Scenario: F077-07 generic failures and validation
    Given source declares zero named throwable errors
    When fake HTTP denies permission with generic 403 envelope
    Then SDK preserves error identity and makes one request
    When fake HTTP raises timeout
    Then SDK reports transport failure without replay
    When request_timeout is zero
    Then SDK rejects input before HTTP

  Scenario Outline: F077-08 v1.ontologies.Attachment.upload complete wire and result
    Given source bindings and frozen assets for v1.ontologies.Attachment.upload
    When SDK runs <mode> with case JSON literal kwargs
    Then request equals POST /v1/attachments/upload
    And query, headers, body and seven-second timeout equal literal wire oracle
    And response equals case JSON literal payload with tenant-schema meaning preserved
    And response and client close on successful completion
    And ordinary sync/async 403 and timeout preserve failure identity
    And raw sync/async consumer failures and applicable malformed JSON decode failures close resources
    And streaming sync/async consumer exceptions and async cancellation close resources
    And sync/async zero timeout rejects before HTTP
    Examples:
      | mode |
      | sync_ordinary |
      | sync_raw |
      | sync_streaming |
      | async_ordinary |
      | async_raw |
      | async_streaming |

  Scenario: F077-08 generic failures and validation
    Given source declares zero named throwable errors
    When fake HTTP denies permission with generic 403 envelope
    Then SDK preserves error identity and makes one request
    When fake HTTP raises timeout
    Then SDK reports transport failure without replay
    When request_timeout is zero
    Then SDK rejects input before HTTP

  Scenario Outline: F077-09 v1.ontologies.ObjectType.get complete wire and result
    Given source bindings and frozen assets for v1.ontologies.ObjectType.get
    When SDK runs <mode> with case JSON literal kwargs
    Then request equals GET /v1/ontologies/ri.qa.main.ontology.flight077/objectTypes/Flight
    And query, headers, body and seven-second timeout equal literal wire oracle
    And response equals case JSON literal payload with tenant-schema meaning preserved
    And response and client close on successful completion
    And ordinary sync/async 403 and timeout preserve failure identity
    And raw sync/async consumer failures and applicable malformed JSON decode failures close resources
    And streaming sync/async consumer exceptions and async cancellation close resources
    And sync/async zero timeout rejects before HTTP
    Examples:
      | mode |
      | sync_ordinary |
      | sync_raw |
      | sync_streaming |
      | async_ordinary |
      | async_raw |
      | async_streaming |

  Scenario: F077-09 generic failures and validation
    Given source declares zero named throwable errors
    When fake HTTP denies permission with generic 403 envelope
    Then SDK preserves error identity and makes one request
    When fake HTTP raises timeout
    Then SDK reports transport failure without replay
    When request_timeout is zero
    Then SDK rejects input before HTTP

  Scenario Outline: F077-10 v1.ontologies.ObjectType.get_outgoing_link_type complete wire and result
    Given source bindings and frozen assets for v1.ontologies.ObjectType.get_outgoing_link_type
    When SDK runs <mode> with case JSON literal kwargs
    Then request equals GET /v1/ontologies/ri.qa.main.ontology.flight077/objectTypes/Flight/outgoingLinkTypes/destination
    And query, headers, body and seven-second timeout equal literal wire oracle
    And response equals case JSON literal payload with tenant-schema meaning preserved
    And response and client close on successful completion
    And ordinary sync/async 403 and timeout preserve failure identity
    And raw sync/async consumer failures and applicable malformed JSON decode failures close resources
    And streaming sync/async consumer exceptions and async cancellation close resources
    And sync/async zero timeout rejects before HTTP
    Examples:
      | mode |
      | sync_ordinary |
      | sync_raw |
      | sync_streaming |
      | async_ordinary |
      | async_raw |
      | async_streaming |

  Scenario: F077-10 generic failures and validation
    Given source declares zero named throwable errors
    When fake HTTP denies permission with generic 403 envelope
    Then SDK preserves error identity and makes one request
    When fake HTTP raises timeout
    Then SDK reports transport failure without replay
    When request_timeout is zero
    Then SDK rejects input before HTTP

  Scenario Outline: F077-11 v1.ontologies.ObjectType.list complete wire and result
    Given source bindings and frozen assets for v1.ontologies.ObjectType.list
    When SDK runs <mode> with case JSON literal kwargs
    Then request equals GET /v1/ontologies/ri.qa.main.ontology.flight077/objectTypes
    And query, headers, body and seven-second timeout equal literal wire oracle
    And response equals case JSON literal payload with tenant-schema meaning preserved
    And response and client close on successful completion
    And ordinary sync/async 403 and timeout preserve failure identity
    And raw sync/async consumer failures and applicable malformed JSON decode failures close resources
    And streaming sync/async consumer exceptions and async cancellation close resources
    And sync/async zero timeout rejects before HTTP
    Examples:
      | mode |
      | sync_ordinary |
      | sync_raw |
      | sync_streaming |
      | async_ordinary |
      | async_raw |
      | async_streaming |

  Scenario: F077-11 generic failures and validation
    Given source declares zero named throwable errors
    When fake HTTP denies permission with generic 403 envelope
    Then SDK preserves error identity and makes one request
    When fake HTTP raises timeout
    Then SDK reports transport failure without replay
    When request_timeout is zero
    Then SDK rejects input before HTTP

  Scenario: F077-11 finite paging
    Given two pages with distinct objects or schema identities
    When ordinary iterator or explicit search continuation advances
    Then exactly two requests retain initial filters and token placement
    And repeated token and page/item bounds preserve partial results
    And stopping after one item causes no next request

  Scenario Outline: F077-12 v1.ontologies.ObjectType.list_outgoing_link_types complete wire and result
    Given source bindings and frozen assets for v1.ontologies.ObjectType.list_outgoing_link_types
    When SDK runs <mode> with case JSON literal kwargs
    Then request equals GET /v1/ontologies/ri.qa.main.ontology.flight077/objectTypes/Flight/outgoingLinkTypes
    And query, headers, body and seven-second timeout equal literal wire oracle
    And response equals case JSON literal payload with tenant-schema meaning preserved
    And response and client close on successful completion
    And ordinary sync/async 403 and timeout preserve failure identity
    And raw sync/async consumer failures and applicable malformed JSON decode failures close resources
    And streaming sync/async consumer exceptions and async cancellation close resources
    And sync/async zero timeout rejects before HTTP
    Examples:
      | mode |
      | sync_ordinary |
      | sync_raw |
      | sync_streaming |
      | async_ordinary |
      | async_raw |
      | async_streaming |

  Scenario: F077-12 generic failures and validation
    Given source declares zero named throwable errors
    When fake HTTP denies permission with generic 403 envelope
    Then SDK preserves error identity and makes one request
    When fake HTTP raises timeout
    Then SDK reports transport failure without replay
    When request_timeout is zero
    Then SDK rejects input before HTTP

  Scenario: F077-12 finite paging
    Given two pages with distinct objects or schema identities
    When ordinary iterator or explicit search continuation advances
    Then exactly two requests retain initial filters and token placement
    And repeated token and page/item bounds preserve partial results
    And stopping after one item causes no next request

  Scenario Outline: F077-13 v1.ontologies.Ontology.get complete wire and result
    Given source bindings and frozen assets for v1.ontologies.Ontology.get
    When SDK runs <mode> with case JSON literal kwargs
    Then request equals GET /v1/ontologies/ri.qa.main.ontology.flight077
    And query, headers, body and seven-second timeout equal literal wire oracle
    And response equals case JSON literal payload with tenant-schema meaning preserved
    And response and client close on successful completion
    And ordinary sync/async 403 and timeout preserve failure identity
    And raw sync/async consumer failures and applicable malformed JSON decode failures close resources
    And streaming sync/async consumer exceptions and async cancellation close resources
    And sync/async zero timeout rejects before HTTP
    Examples:
      | mode |
      | sync_ordinary |
      | sync_raw |
      | sync_streaming |
      | async_ordinary |
      | async_raw |
      | async_streaming |

  Scenario: F077-13 generic failures and validation
    Given source declares zero named throwable errors
    When fake HTTP denies permission with generic 403 envelope
    Then SDK preserves error identity and makes one request
    When fake HTTP raises timeout
    Then SDK reports transport failure without replay
    When request_timeout is zero
    Then SDK rejects input before HTTP

  Scenario Outline: F077-14 v1.ontologies.Ontology.list complete wire and result
    Given source bindings and frozen assets for v1.ontologies.Ontology.list
    When SDK runs <mode> with case JSON literal kwargs
    Then request equals GET /v1/ontologies
    And query, headers, body and seven-second timeout equal literal wire oracle
    And response equals case JSON literal payload with tenant-schema meaning preserved
    And response and client close on successful completion
    And ordinary sync/async 403 and timeout preserve failure identity
    And raw sync/async consumer failures and applicable malformed JSON decode failures close resources
    And streaming sync/async consumer exceptions and async cancellation close resources
    And sync/async zero timeout rejects before HTTP
    Examples:
      | mode |
      | sync_ordinary |
      | sync_raw |
      | sync_streaming |
      | async_ordinary |
      | async_raw |
      | async_streaming |

  Scenario: F077-14 generic failures and validation
    Given source declares zero named throwable errors
    When fake HTTP denies permission with generic 403 envelope
    Then SDK preserves error identity and makes one request
    When fake HTTP raises timeout
    Then SDK reports transport failure without replay
    When request_timeout is zero
    Then SDK rejects input before HTTP

  Scenario Outline: F077-15 v1.ontologies.OntologyObject.aggregate complete wire and result
    Given source bindings and frozen assets for v1.ontologies.OntologyObject.aggregate
    When SDK runs <mode> with case JSON literal kwargs
    Then request equals POST /v1/ontologies/ri.qa.main.ontology.flight077/objects/Flight/aggregate
    And query, headers, body and seven-second timeout equal literal wire oracle
    And response equals case JSON literal payload with tenant-schema meaning preserved
    And response and client close on successful completion
    And ordinary sync/async 403 and timeout preserve failure identity
    And raw sync/async consumer failures and applicable malformed JSON decode failures close resources
    And streaming sync/async consumer exceptions and async cancellation close resources
    And sync/async zero timeout rejects before HTTP
    Examples:
      | mode |
      | sync_ordinary |
      | sync_raw |
      | sync_streaming |
      | async_ordinary |
      | async_raw |
      | async_streaming |

  Scenario: F077-15 generic failures and validation
    Given source declares zero named throwable errors
    When fake HTTP denies permission with generic 403 envelope
    Then SDK preserves error identity and makes one request
    When fake HTTP raises timeout
    Then SDK reports transport failure without replay
    When request_timeout is zero
    Then SDK rejects input before HTTP

  Scenario Outline: F077-16 v1.ontologies.OntologyObject.get complete wire and result
    Given source bindings and frozen assets for v1.ontologies.OntologyObject.get
    When SDK runs <mode> with case JSON literal kwargs
    Then request equals GET /v1/ontologies/ri.qa.main.ontology.flight077/objects/Flight/QA-077
    And query, headers, body and seven-second timeout equal literal wire oracle
    And response equals case JSON literal payload with tenant-schema meaning preserved
    And response and client close on successful completion
    And ordinary sync/async 403 and timeout preserve failure identity
    And raw sync/async consumer failures and applicable malformed JSON decode failures close resources
    And streaming sync/async consumer exceptions and async cancellation close resources
    And sync/async zero timeout rejects before HTTP
    Examples:
      | mode |
      | sync_ordinary |
      | sync_raw |
      | sync_streaming |
      | async_ordinary |
      | async_raw |
      | async_streaming |

  Scenario: F077-16 generic failures and validation
    Given source declares zero named throwable errors
    When fake HTTP denies permission with generic 403 envelope
    Then SDK preserves error identity and makes one request
    When fake HTTP raises timeout
    Then SDK reports transport failure without replay
    When request_timeout is zero
    Then SDK rejects input before HTTP

  Scenario Outline: F077-17 v1.ontologies.OntologyObject.get_linked_object complete wire and result
    Given source bindings and frozen assets for v1.ontologies.OntologyObject.get_linked_object
    When SDK runs <mode> with case JSON literal kwargs
    Then request equals GET /v1/ontologies/ri.qa.main.ontology.flight077/objects/Flight/QA-077/links/destination/SOF
    And query, headers, body and seven-second timeout equal literal wire oracle
    And response equals case JSON literal payload with tenant-schema meaning preserved
    And response and client close on successful completion
    And ordinary sync/async 403 and timeout preserve failure identity
    And raw sync/async consumer failures and applicable malformed JSON decode failures close resources
    And streaming sync/async consumer exceptions and async cancellation close resources
    And sync/async zero timeout rejects before HTTP
    Examples:
      | mode |
      | sync_ordinary |
      | sync_raw |
      | sync_streaming |
      | async_ordinary |
      | async_raw |
      | async_streaming |

  Scenario: F077-17 generic failures and validation
    Given source declares zero named throwable errors
    When fake HTTP denies permission with generic 403 envelope
    Then SDK preserves error identity and makes one request
    When fake HTTP raises timeout
    Then SDK reports transport failure without replay
    When request_timeout is zero
    Then SDK rejects input before HTTP

  Scenario Outline: F077-18 v1.ontologies.OntologyObject.list complete wire and result
    Given source bindings and frozen assets for v1.ontologies.OntologyObject.list
    When SDK runs <mode> with case JSON literal kwargs
    Then request equals GET /v1/ontologies/ri.qa.main.ontology.flight077/objects/Flight
    And query, headers, body and seven-second timeout equal literal wire oracle
    And response equals case JSON literal payload with tenant-schema meaning preserved
    And response and client close on successful completion
    And ordinary sync/async 403 and timeout preserve failure identity
    And raw sync/async consumer failures and applicable malformed JSON decode failures close resources
    And streaming sync/async consumer exceptions and async cancellation close resources
    And sync/async zero timeout rejects before HTTP
    Examples:
      | mode |
      | sync_ordinary |
      | sync_raw |
      | sync_streaming |
      | async_ordinary |
      | async_raw |
      | async_streaming |

  Scenario: F077-18 generic failures and validation
    Given source declares zero named throwable errors
    When fake HTTP denies permission with generic 403 envelope
    Then SDK preserves error identity and makes one request
    When fake HTTP raises timeout
    Then SDK reports transport failure without replay
    When request_timeout is zero
    Then SDK rejects input before HTTP

  Scenario: F077-18 finite paging
    Given two pages with distinct objects or schema identities
    When ordinary iterator or explicit search continuation advances
    Then exactly two requests retain initial filters and token placement
    And repeated token and page/item bounds preserve partial results
    And stopping after one item causes no next request

  Scenario Outline: F077-19 v1.ontologies.OntologyObject.list_linked_objects complete wire and result
    Given source bindings and frozen assets for v1.ontologies.OntologyObject.list_linked_objects
    When SDK runs <mode> with case JSON literal kwargs
    Then request equals GET /v1/ontologies/ri.qa.main.ontology.flight077/objects/Flight/QA-077/links/destination
    And query, headers, body and seven-second timeout equal literal wire oracle
    And response equals case JSON literal payload with tenant-schema meaning preserved
    And response and client close on successful completion
    And ordinary sync/async 403 and timeout preserve failure identity
    And raw sync/async consumer failures and applicable malformed JSON decode failures close resources
    And streaming sync/async consumer exceptions and async cancellation close resources
    And sync/async zero timeout rejects before HTTP
    Examples:
      | mode |
      | sync_ordinary |
      | sync_raw |
      | sync_streaming |
      | async_ordinary |
      | async_raw |
      | async_streaming |

  Scenario: F077-19 generic failures and validation
    Given source declares zero named throwable errors
    When fake HTTP denies permission with generic 403 envelope
    Then SDK preserves error identity and makes one request
    When fake HTTP raises timeout
    Then SDK reports transport failure without replay
    When request_timeout is zero
    Then SDK rejects input before HTTP

  Scenario: F077-19 finite paging
    Given two pages with distinct objects or schema identities
    When ordinary iterator or explicit search continuation advances
    Then exactly two requests retain initial filters and token placement
    And repeated token and page/item bounds preserve partial results
    And stopping after one item causes no next request

  Scenario Outline: F077-20 v1.ontologies.OntologyObject.search complete wire and result
    Given source bindings and frozen assets for v1.ontologies.OntologyObject.search
    When SDK runs <mode> with case JSON literal kwargs
    Then request equals POST /v1/ontologies/ri.qa.main.ontology.flight077/objects/Flight/search
    And query, headers, body and seven-second timeout equal literal wire oracle
    And response equals case JSON literal payload with tenant-schema meaning preserved
    And response and client close on successful completion
    And ordinary sync/async 403 and timeout preserve failure identity
    And raw sync/async consumer failures and applicable malformed JSON decode failures close resources
    And streaming sync/async consumer exceptions and async cancellation close resources
    And sync/async zero timeout rejects before HTTP
    Examples:
      | mode |
      | sync_ordinary |
      | sync_raw |
      | sync_streaming |
      | async_ordinary |
      | async_raw |
      | async_streaming |

  Scenario: F077-20 generic failures and validation
    Given source declares zero named throwable errors
    When fake HTTP denies permission with generic 403 envelope
    Then SDK preserves error identity and makes one request
    When fake HTTP raises timeout
    Then SDK reports transport failure without replay
    When request_timeout is zero
    Then SDK rejects input before HTTP

  Scenario: F077-20 finite paging
    Given two pages with distinct objects or schema identities
    When ordinary iterator or explicit search continuation advances
    Then exactly two requests retain initial filters and token placement
    And repeated token and page/item bounds preserve partial results
    And stopping after one item causes no next request

  Scenario Outline: F077-21 v1.ontologies.Query.execute complete wire and result
    Given source bindings and frozen assets for v1.ontologies.Query.execute
    When SDK runs <mode> with case JSON literal kwargs
    Then request equals POST /v1/ontologies/ri.qa.main.ontology.flight077/queries/countScheduledFlights/execute
    And query, headers, body and seven-second timeout equal literal wire oracle
    And response equals case JSON literal payload with tenant-schema meaning preserved
    And response and client close on successful completion
    And ordinary sync/async 403 and timeout preserve failure identity
    And raw sync/async consumer failures and applicable malformed JSON decode failures close resources
    And streaming sync/async consumer exceptions and async cancellation close resources
    And sync/async zero timeout rejects before HTTP
    Examples:
      | mode |
      | sync_ordinary |
      | sync_raw |
      | sync_streaming |
      | async_ordinary |
      | async_raw |
      | async_streaming |

  Scenario: F077-21 generic failures and validation
    Given source declares zero named throwable errors
    When fake HTTP denies permission with generic 403 envelope
    Then SDK preserves error identity and makes one request
    When fake HTTP raises timeout
    Then SDK reports transport failure without replay
    When request_timeout is zero
    Then SDK rejects input before HTTP

  Scenario Outline: F077-22 v1.ontologies.QueryType.get complete wire and result
    Given source bindings and frozen assets for v1.ontologies.QueryType.get
    When SDK runs <mode> with case JSON literal kwargs
    Then request equals GET /v1/ontologies/ri.qa.main.ontology.flight077/queryTypes/countScheduledFlights
    And query, headers, body and seven-second timeout equal literal wire oracle
    And response equals case JSON literal payload with tenant-schema meaning preserved
    And response and client close on successful completion
    And ordinary sync/async 403 and timeout preserve failure identity
    And raw sync/async consumer failures and applicable malformed JSON decode failures close resources
    And streaming sync/async consumer exceptions and async cancellation close resources
    And sync/async zero timeout rejects before HTTP
    Examples:
      | mode |
      | sync_ordinary |
      | sync_raw |
      | sync_streaming |
      | async_ordinary |
      | async_raw |
      | async_streaming |

  Scenario: F077-22 generic failures and validation
    Given source declares zero named throwable errors
    When fake HTTP denies permission with generic 403 envelope
    Then SDK preserves error identity and makes one request
    When fake HTTP raises timeout
    Then SDK reports transport failure without replay
    When request_timeout is zero
    Then SDK rejects input before HTTP

  Scenario Outline: F077-23 v1.ontologies.QueryType.list complete wire and result
    Given source bindings and frozen assets for v1.ontologies.QueryType.list
    When SDK runs <mode> with case JSON literal kwargs
    Then request equals GET /v1/ontologies/ri.qa.main.ontology.flight077/queryTypes
    And query, headers, body and seven-second timeout equal literal wire oracle
    And response equals case JSON literal payload with tenant-schema meaning preserved
    And response and client close on successful completion
    And ordinary sync/async 403 and timeout preserve failure identity
    And raw sync/async consumer failures and applicable malformed JSON decode failures close resources
    And streaming sync/async consumer exceptions and async cancellation close resources
    And sync/async zero timeout rejects before HTTP
    Examples:
      | mode |
      | sync_ordinary |
      | sync_raw |
      | sync_streaming |
      | async_ordinary |
      | async_raw |
      | async_streaming |

  Scenario: F077-23 generic failures and validation
    Given source declares zero named throwable errors
    When fake HTTP denies permission with generic 403 envelope
    Then SDK preserves error identity and makes one request
    When fake HTTP raises timeout
    Then SDK reports transport failure without replay
    When request_timeout is zero
    Then SDK rejects input before HTTP

  Scenario: F077-23 finite paging
    Given two pages with distinct objects or schema identities
    When ordinary iterator or explicit search continuation advances
    Then exactly two requests retain initial filters and token placement
    And repeated token and page/item bounds preserve partial results
    And stopping after one item causes no next request

  Scenario: Mutation and validation lifecycle boundaries
    Given INVALID action validation with failed submission criteria
    Then safe application makes zero apply calls
    Given VALID validation and generic 403 apply denial
    Then validation does not prove existing-object constraints or mutation success
    And uncertain mutation timeout is retained without automatic retry
    And frozen SDK documentation states OSv1 eventual visibility and OSv2 post-completion visibility
    And no server visibility timing is executed

  Scenario: Attachment upload source defect and retention
    Given binary content and supplied application/octet-stream
    Then frozen SDK sends */* and exact byte length
    And fixture success makes no live MIME acceptance claim
    And frozen SDK documentation states new unattached upload removal after one hour
    And frozen SDK documentation states disconnected attachment cleanup is biweekly
    And no server retention timer or cleanup is executed

  Scenario: Unknown aggregation labels remain uninterpreted
    Given group labels and values are arbitrary server response data
    Then unknown labels stop derived computation
    And mixed confirmed and unknown keys stop local reader calculation with raw group retained
    And old presence/type-only guard fails the mixed-label contract
    And SDK opaque group data is accepted without asserting a server rejection policy
    And request field paths establish no response label or timezone guarantee

  Scenario: R077-01 application guards reject malformed tenant values
    Given independent Flight metadata and a separately confirmed application label mapping
    When valid and mutated object and group payloads enter reader-derived decision guards
    Then valid values permit use and mismatches stop with original response retained
    And bypassing either guard makes the corresponding check fail

  Scenario: R077-02 uncertain mutation recovery
    Given one synthetic accepted apply, partial apply_batch, or upload whose HTTP response is lost
    When actual SDK transport raises read timeout with retries disabled
    Then action effect observations use at most two authorized object reads
    And observations remain partial and causality uncertain with no mutation replay
    And lost upload with no RID escalates with zero unsupported lookup requests
    And retention and consistency claims are reviewed against frozen source documentation only

  Scenario: R077-04 finite items and response paging
    Given six automatic iterators and one explicit SearchObjectsResponse pager
    When each explicit response pager has item limit one and unread data plus continuation
    Then one item is returned and unread items plus token remain available
    And six async automatic iterators stop after one item without fetching next page

  Scenario: R077-06 runnable distributed examples
    When every frozen distributed verify executes with sockets denied
    Then actual invocation AST resolves to correct SDK resource and method
    And exact runtime decoded model or bytes identity matches source contract
    And independently corrupting each decoded result makes example assertion fail
