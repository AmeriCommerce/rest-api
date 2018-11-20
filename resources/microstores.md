microstores
=========

## Get Microstores

###### Example Requests

```shell
GET /api/v1/microstores/{id}
```

```shell
GET /api/v1/microstores?id=5
```

```shell
GET /api/v1/microstores?name=fakestore
```

###### Example Response

```json
{
    "total_count": 1,
    "microstores": [
        {
            "id": 5,
            "name": "fakestore",
            "address_line_1": "1234 AmeriCommerce Blvd",
            "address_line_2": "Suite 1",
            "city": "Beaumont",
            "state": "Texas",
            "country": "United States",
            "postal_code": "77702",
            "phone": "555-555-5555",
            "fax": "",
            "parent_store_id": 3,
            "is_micro_store": true,
            "set_cookie": false,
            "cookie_expiration": 0,
            "activation_date": "1900-01-01T00:00:00-06:00",
            "expiration_date": "1900-01-01T00:00:00-06:00",
            "logo_image": "",
            "path": "/fakestore.aspx"
        }
    ]
}
```

## Adding Microstores

Creates a microstore as specified by the model in the request. After successfull creation, the model will be returned along with the new microstore ID. 

###### Example Request

```shell
POST /api/v1/microstores
```

```json
{
    "name": "fakestore",
    "address_line_1": "1234 AmeriCommerce Blvd",
    "address_line_2": "Suite 1",
    "city": "Beaumont",
    "state": "Texas",
    "country": "United States",
    "postal_code": "77702",
    "phone": "555-555-5555",
    "fax": "",
    "parent_store_id": 3,
    "is_micro_store": true,
    "set_cookie": false,
    "cookie_expiration": 0,
    "activation_date": "1900-01-01T00:00:00-06:00",
    "expiration_date": "1900-01-01T00:00:00-06:00",
    "logo_image": "",
    "path": "/fakestore.aspx"
}
```

###### Example Response

```json
{
    "id": 11,
    "name": "fakestore",
    "address_line_1": "1234 AmeriCommerce Blvd",
    "address_line_2": "Suite 1",
    "city": "Beaumont",
    "state": "Texas",
    "country": "United States",
    "postal_code": "77702",
    "phone": "555-555-5555",
    "fax": "",
    "parent_store_id": 3,
    "is_micro_store": true,
    "set_cookie": false,
    "cookie_expiration": 0,
    "activation_date": "1900-01-01T00:00:00-06:00",
    "expiration_date": "1900-01-01T00:00:00-06:00",
    "logo_image": "",
    "path": "/fakestore.aspx"
}
```

## Modifying Microstores

Modifies the microstore as specified by the model in the request. The ID of the microstore must be in the request url as seen below:


###### Example Request

```shell
PUT /api/v1/microstores/{id}
```

```json
{
    "name": "fakestore2",
    "address_line_1": "1234 AmeriCommerce Blvd",
    "address_line_2": "Suite 1",
    "city": "Beaumont",
    "state": "Texas",
    "country": "United States",
    "postal_code": "77702",
    "phone": "555-555-5555",
    "fax": "",
    "parent_store_id": 3,
    "is_micro_store": true,
    "set_cookie": false,
    "cookie_expiration": 0,
    "activation_date": "1900-01-01T00:00:00-06:00",
    "expiration_date": "1900-01-01T00:00:00-06:00",
    "logo_image": "",
    "path": "/fakestore.aspx"
}
```

###### Example Response

```json
{
    "id": 11,
    "name": "fakestore2",
    "address_line_1": "1234 AmeriCommerce Blvd",
    "address_line_2": "Suite 1",
    "city": "Beaumont",
    "state": "Texasz",
    "country": "United States",
    "postal_code": "77702",
    "phone": "555-555-5555",
    "fax": "",
    "parent_store_id": 3,
    "is_micro_store": true,
    "set_cookie": false,
    "cookie_expiration": 0,
    "activation_date": "1900-01-01T00:00:00-06:00",
    "expiration_date": "1900-01-01T00:00:00-06:00",
    "logo_image": "",
    "path": "/fakestore.aspx"
}
```

## Deleting Microstores

###### Example Request

```shell
DELETE /api/v1/microstores/{id}
```


## Getting Active Catalog of Microstores

###### Example Request

```shell
GET /api/v1/microstores/{id}/active_catalog
```

###### Example Response

```json
{
    "store_id": 10,
    "is_micro_store": true,
    "microstore_catalog_override": true,
    "root_category_id": 3,
    "category_ids": [
        3,
        1,
        9,
        7
    ],
    "product_ids": []
}
```

## Modify Active Catalog of Microstores

###### Example Request

```shell
PUT /api/v1/microstores/{id}/active_catalog
```

```json
{
    "store_id": 10,
    "is_micro_store": true,
    "microstore_catalog_override": true,
    "root_category_id": 3,
    "category_ids": [
        3,
        1,
        9,
        8
    ],
    "product_ids": []
}
```

###### Example Response

```json
{
    "store_id": 10,
    "is_micro_store": true,
    "microstore_catalog_override": true,
    "root_category_id": 3,
    "category_ids": [
        3,
        1,
        9,
        8
    ],
    "product_ids": []
}
```