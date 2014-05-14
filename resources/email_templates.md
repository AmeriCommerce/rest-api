email_templates
===============

```shell
GET /api/v1/email_templates
```

Sample Model
------------

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