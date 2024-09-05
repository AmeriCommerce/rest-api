import
=========

`/api/v1/import` is a specialized endpoint for importing data through the api.

## Import File

The first part of this request should be json, and the second part should be the csv file for importing. Import type and mapping info must be included.  

###### Example Requests

```shell
POST /api/v1/import/file
```

```json
{
	"import_type": "Product",
	"log_errors_to_file": false,
	"import_email_address": "",
	"mapping_info":[ 
            {    
                "destination_column": "ItemID",   
                "source_column": "ItemID"
            },
            {   
                "destination_column": "Cost",    
                "source_column": "Cost"
            }
         ]
}
```

## Import Fetch

This endpoint will import by grabbing a file from a url. Import type, file url and mapping info must be included.  

###### Example Requests

```shell
POST /api/v1/import/fetch
```

```json
{
	"import_type": "Product",
	"log_errors_to_file": false,
	"import_email_address": "",
        "file_url": "https://test.com/addaproductwithbasicinfo.csv",
	"mapping_info":[ 
            {    
                "destination_column": "ItemID",   
                "source_column": "ItemID"
            },
            {   
                "destination_column": "Cost",    
                "source_column": "Cost"
            }
         ]
}
```