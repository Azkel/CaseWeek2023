# Python sample — CaseWeek 2023

Django **polls** application used in the CI/CD workshop track. Based on the [Microsoft Django + Azure App Service sample](https://learn.microsoft.com/azure/app-service/quickstart-python), configured for deployment to Azure App Service with PostgreSQL in production.

## Layout

Application root: `Python/source/` (not `Python/src` — a common mistake in workshop pipelines).

```
Python/source/
├── manage.py
├── azuresite/          # Django project settings
├── polls/              # Polls app with tests
├── requirements.txt
└── test-example.py     # Intentional bug — see exercises
```

## Run locally

```bash
cd Python/source
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python manage.py test
python manage.py runserver
```

## CI/CD

| Workflow | File |
|----------|------|
| Build & test | [`.github/workflows/python-ci.yml`](../../.github/workflows/python-ci.yml) |
| Deploy to Azure App Service | [`.github/workflows/azure-webapps-python.yml`](../../.github/workflows/azure-webapps-python.yml) |

## Azure production settings

When deployed to App Service, configure application settings for PostgreSQL:

- `DBHOST` — server name only (not full URL)
- `DBUSER` — username only
- `DBPASS` — password
- `DBNAME` — database name

See `azuresite/production.py` and the [Microsoft tutorial](https://learn.microsoft.com/azure/postgresql/flexible-server/tutorial-django-app-service-postgres).

## Failing pipeline exercise

[`test-example.py`](test-example.py) uses invalid Python (`true` instead of `True`) on purpose. See [docs/exercises.md](../../docs/exercises.md) for how to wire it into CI and fix it.

## Upstream sample

Original Microsoft sample changelog and license: [LICENSE.md](LICENSE.md).
