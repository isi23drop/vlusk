### Migrations
This repository adopts SQLite3 as default database for portability, specially in constrained environments such as pipelines CI/CD or ARM deploys.

'click' in the ./db.py file defines a CLI command 'init-db' that will call the init_db function.

```
flask --app flaskr init-db
```


