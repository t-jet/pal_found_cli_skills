# foundry_sdk.v2.ontologies.models.PropertyValue


An Ontology property value uses the JSON encoding for its declared property type. The local type table below lists arrays, primitives, date/time, GeoJSON, Cipher, attachment, media and time-series encodings. Match the target property metadata; an attachment or media reference needs its documented object shape, not a display string.

## JSON encodings by Ontology property type

`typing.Any` is the SDK's Python alias, not permission to send an arbitrary JSON shape. Read the target property's type from permitted Ontology metadata, then use its encoding below. JSON examples illustrate shape with synthetic values; substitute authorized tenant identifiers, metadata and real encrypted values.

| Property type | JSON encoding | JSON example |
| --- | --- | --- |
| Array | array | `["alpha","bravo"]` |
| Attachment | JSON encoded `AttachmentProperty` object | `{"rid":"ri.blobster.main.attachment.synthetic"}` |
| Boolean | boolean | `true` |
| Byte | number | `31` |
| CipherText | string | `"CIPHER::ri.bellaso.main.cipher-channel.synthetic::opaque::CIPHER"` |
| Date | ISO 8601 extended local date string | `"2021-05-01"` |
| Decimal | string | `"2.718281828"` |
| Double | number | `3.14159265` |
| Float | number | `3.14159265` |
| GeoPoint | geojson | `{"type":"Point","coordinates":[102.0,0.5]}` |
| GeoShape | geojson | `{"type":"LineString","coordinates":[[102.0,0.0],[103.0,1.0]]}` |
| Integer | number | `238940` |
| Long | string | `"58319870951433"` |
| MediaReference | JSON encoded `MediaReference` object | `{"mimeType":"application/pdf","reference":{"type":"mediaSetViewItem","mediaSetViewItem":{"mediaSetRid":"ri.mio.main.media-set.synthetic","mediaSetViewRid":"ri.mio.main.view.synthetic","mediaItemRid":"ri.mio.main.media-item.synthetic"}}}` |
| Secured Property Value | JSON encoded `SecuredPropertyValue` object | `{"value":10,"propertySecurityIndex":5}` |
| Short | number | `8739` |
| String | string | `"Call me Ishmael"` |
| Struct | JSON object of struct field API name -> value | `{"firstName":"Alex","lastName":"Karp"}` |
| Timestamp | ISO 8601 extended offset date-time string in UTC zone | `"2021-01-04T05:00:00Z"` |
| Timeseries | JSON encoded `TimeseriesProperty` object or seriesId string | `{"seriesId":"wellPressureSeriesId","syncRid":"ri.time-series-catalog.main.sync.synthetic"}`<br>`{"templateRid":"ri.codex-emu.main.template.synthetic","templateVersion":"0.0.0"}`<br>`"wellPressureSeriesId"` |
| Vector | array | `[0.1,0.3,0.02]` |

Decimal and Long are JSON strings so their values are not rounded through a JSON number. Date uses a local ISO 8601 date; Timestamp uses an ISO 8601 UTC offset date-time. GeoPoint and GeoShape use GeoJSON objects. Struct is an object keyed by struct field API name. An Attachment is an object with `rid`; a MediaReference has `mimeType` and a typed `reference`; a secured value has `value` and `propertySecurityIndex`. Timeseries accepts an object with `seriesId` and `syncRid`, an object with `templateRid` and `templateVersion`, or a bare series ID string. For compatibility the source also accepts Boolean, Byte, Double, Float, Integer and Short as JSON strings; prefer the primary encoding shown above.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
PropertyValue: typing_extensions.TypeAlias = typing.Any
```

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](PropertyValue.md)
