"""Synthetic business mapping checks; does not configure a Foundry Ontology."""


def index_objects(rows, key):
    result = {}
    for row in rows:
        value = row.get(key)
        if not isinstance(value, str) or not value:
            raise ValueError("key must be a nonempty string")
        if value in result:
            raise ValueError("duplicate object key")
        result[value] = dict(row)
    return result


def interface_view(row, mapping, declared_types):
    if "name" not in mapping:
        raise ValueError("required name mapping missing")
    if declared_types[mapping["name"]] != "string":
        raise ValueError("required name mapping incompatible")
    name = row[mapping["name"]]
    if not isinstance(name, str):
        raise ValueError("required name value incompatible")
    return {"name": name, "region": row.get(mapping.get("region"))}


def main():
    customers = index_objects([{"customerId": "c1", "customerName": "Ada"}], "customerId")
    orders = index_objects([{"orderId": "o1", "customerId": "c1", "totalCents": 1200}], "orderId")
    assert customers[orders["o1"]["customerId"]]["customerName"] == "Ada"
    customers["c1"]["customerName"] = "Grace"
    assert customers[orders["o1"]["customerId"]]["customerName"] == "Grace"
    for rows in [[{"orderId": "o1"}, {"orderId": "o1"}], [{"orderId": 1}]]:
        try:
            index_objects(rows, "orderId")
        except ValueError:
            pass
        else:
            raise AssertionError("invalid object identity accepted")
    assert interface_view({"customerName": "Ada"}, {"name": "customerName"}, {"customerName": "string"}) == {"name": "Ada", "region": None}
    assert interface_view({"supplierName": "Acme", "supplierRegion": "West"}, {"name": "supplierName", "region": "supplierRegion"}, {"supplierName": "string", "supplierRegion": "string"}) == {"name": "Acme", "region": "West"}
    for mapping, types in [({}, {}), ({"name": "supplierNumber"}, {"supplierNumber": "integer"})]:
        try:
            interface_view({"supplierNumber": 1}, mapping, types)
        except ValueError:
            pass
        else:
            raise AssertionError("invalid interface mapping accepted")
    print("mapping fixtures passed: stable keys/link, duplicate/type rejection, optional interface and incompatible mapping")


if __name__ == "__main__":
    main()
