# Self-study Azure setup

The CaseWeek 2023 workshop used a **shared Azure subscription** with pre-created App Service instances and service principals. That environment is **not available** for archival use. Follow this guide to reproduce deployments on your own account.

## Prerequisites

- [Azure account](https://azure.microsoft.com/free/) — students at AGH could use verified academic credits; [Azure for Students](https://azure.microsoft.com/free/students/) may apply
- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) (optional but recommended)
- GitHub repository (fork of this repo or your own)

## 1. Create resources

### Option A — Azure Portal

1. Sign in to [portal.azure.com](https://portal.azure.com).
2. **Create a resource → Web App**.
3. Choose:
   - **Resource group:** new, e.g. `rg-caseweek-lab`
   - **Name:** globally unique, e.g. `myname-python-caseweek`
   - **Publish:** Code
   - **Runtime stack:** Python 3.11 or .NET 6 (match your track)
   - **Region:** West Europe or closest to you
   - **App Service Plan:** new, Basic B1 is enough for lab work
4. Review + create.

Repeat for a second app if you want both Python and .NET tracks.

### Option B — Azure CLI

```bash
az login
az group create --name rg-caseweek-lab --location westeurope

# Python web app
az appservice plan create --name plan-caseweek --resource-group rg-caseweek-lab --sku B1 --is-linux
az webapp create --resource-group rg-caseweek-lab --plan plan-caseweek \
  --name myname-python-caseweek --runtime "PYTHON|3.11"

# .NET web app (separate plan or share the same plan)
az webapp create --resource-group rg-caseweek-lab --plan plan-caseweek \
  --name myname-dotnet-caseweek --runtime "DOTNET|6.0"
```

Replace `myname-*` with a unique prefix.

## 2. Configure GitHub secrets

### Publish profile (method used in workshop)

1. In Portal, open your Web App → **Overview → Download publish profile**.
2. In GitHub: **Settings → Secrets and variables → Actions → New repository secret**.
3. Create:
   - `AZURE_WEBAPP_PYTHON_PUBLISH_PROFILE` — full XML for Python app
   - `AZURE_WEBAPP_DOTNET_PUBLISH_PROFILE` — full XML for .NET app

4. Update workflow `env.AZURE_WEBAPP_NAME` to match the web app name exactly.

### Service principal (alternative)

```bash
az ad sp create-for-rbac --name "github-caseweek-deploy" \
  --role contributor \
  --scopes /subscriptions/SUBSCRIPTION_ID/resourceGroups/rg-caseweek-lab \
  --sdk-auth
```

Store JSON output fields as GitHub secrets and use `azure/login@v2` before deploy. See [Deploy to Azure App Service using GitHub Actions](https://learn.microsoft.com/azure/app-service/deploy-github-actions).

## 3. Python-specific notes

The Django sample expects PostgreSQL in production (`DBHOST`, `DBUSER`, `DBPASS`, `DBNAME` in App Service **Configuration → Application settings**). For a minimal lab deploy without a database:

- App Service may start but polls features need DB configuration, or
- Add an **Azure Database for PostgreSQL flexible server** and set connection settings per [Microsoft tutorial](https://learn.microsoft.com/azure/postgresql/flexible-server/tutorial-django-app-service-postgres).

Local CI tests use SQLite (default Django test settings) and do not require Azure DB.

## 4. .NET-specific notes

The reference CD workflow runs:

```bash
dotnet publish -c Release -o ./publish
```

and deploys the `./publish` folder. Ensure the Web App runtime stack is **.NET 6**.

## 5. Verify deployment

1. Push to `main` or trigger **Actions → Build and deploy … → Run workflow**.
2. Check job logs for `azure/webapps-deploy` success.
3. Browse `https://<AZURE_WEBAPP_NAME>.azurewebsites.net`.
4. If the app errors, use **Log stream** in Portal or `az webapp log tail`.

## 6. Clean up

Delete the resource group when finished to avoid charges:

```bash
az group delete --name rg-caseweek-lab --yes --no-wait
```

## Mapping to workshop concepts

| Workshop concept | Your self-study equivalent |
|------------------|----------------------------|
| Instructor-provided subscription | Your Azure subscription or student credits |
| Per-student Web App | Web App you create with unique name |
| Shared service principal | Publish profile or SP you create |
| `smyk-python-caseweek` (instructor example) | Your chosen `AZURE_WEBAPP_NAME` |
