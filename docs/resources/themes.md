themes
=====

## Import Theme


**Required scope**: `themes`

###### Sample Request
```shell
POST /api/v1/themes/import
```

```json
{
    "theme_name": "ThemeName",
    "file_path": "path-to-theme-import-file.zip"
}

```

###### Sample Response

```json
{
    "theme_id": 1234,
    "theme_name": "ThemeName"
}

```
Theme name is included because it can be changed by the import process in the case of duplicates. (ex: ThemeName_1)
