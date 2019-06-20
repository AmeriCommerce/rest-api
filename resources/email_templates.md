email_templates
===============

## Get Email Template

```shell
GET /api/v1/email_templates
```

**Required scope**: `read_marketing`, `marketing`

###### Sample Model

```json
{
	"id": 30,
	"type": "Blog Comment Approved",
	"body": "Your blog comment has been approved! Use the following link to see your post. ##PROFILEPOSTLINK##",
	"subject": "Blog Comment Approved",
	"from_name": "##STORENAME##",
	"from_email": "##STOREEMAIL##",
	"is_enabled": false,
	"admin_alert_header": "",
	"admin_alert_subject": "",
	"is_admin_alert_enabled": false,
	"email_format": "TEXT"
}
```

## Send Email

Sends an email template as specified by the model in the request. 

###### Example Request

```shell
POST /api/v1/email_templates/{template_id}/send
```

```json
{
	"order_id": 100,
	"customer_id": 7,
	"email_address": "coolGuy89@americommerce.com",
	"merge_codes": {
		"##TESTMERGE##" : "what's up",
		"##ANOTHERMERGE##" : "10"
	}
}
```


