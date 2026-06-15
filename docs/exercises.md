# Workshop exercises

Step-by-step instructions for reproducing CaseWeek 2023 exercises on your own fork. All paths assume the repository root.

---

## Session 1

### Exercise 1 — Simple workflow

**Goal:** Understand triggers, jobs, and steps.

1. In GitHub, go to **Actions → New workflow**.
2. Choose a starter template or “set up a workflow yourself”.
3. Save as `.github/workflows/hello.yml`:

```yaml
name: Hello CaseWeek
on:
  workflow_dispatch:
  push:
    branches: [main]
jobs:
  demo:
    runs-on: ubuntu-latest
    steps:
      - name: Greet
        run: echo "CaseWeek 2023 — GitHub Actions works"
```

4. Commit, push, and confirm the run is green under **Actions**.

---

## Session 2

### Exercise 2 — CI pipeline for Python or .NET

**Goal:** Run build and tests on every push/PR.

**Python**

1. Use [`.github/workflows/python-ci.yml`](../.github/workflows/python-ci.yml) (already in repo).
2. Confirm `working-directory` is `./Python/source`.
3. Push a change under `Python/source/` and verify tests run.

**/.NET**

1. Use [`.github/workflows/dotnet-ci.yml`](../.github/workflows/dotnet-ci.yml).
2. Push a change under `DotNet/` and verify build + test.

**Tips from the workshop**

- GitHub Action Wizard: pick “Python” or “.NET” template, then fix directory paths.
- If using ChatGPT, paste the repo layout and ask for paths relative to `Python/source` or `DotNet/src/ExampleWebApp/`.

### Exercise 3 — Failing pipeline

**Goal:** Learn to read CI logs and fix test failures.

**Python option**

File [`Python/source/test-example.py`](../Python/source/test-example.py) contains an **intentional bug** (`true` instead of `True`). To include it in the test run, either:

- Move it into `polls/tests_example.py` and import it, or
- Run `python -m pytest test-example.py` in a CI step (requires adding `pytest`).

Fix the assertion so the pipeline passes.

**/.NET option**

In [`DotNet/src/ExampleWebApp.Tests/UnitTest1.cs`](../DotNet/src/ExampleWebApp.Tests/UnitTest1.cs), uncomment:

```csharp
Assert.Fail();
```

Push, watch the pipeline fail, then remove or fix the assertion.

### Exercise 4 — Status badge

**Goal:** Display CI status in the README.

Add to your README (replace `YOUR_USER` and workflow filename):

```markdown
![Python CI](https://github.com/YOUR_USER/CaseWeek2023/actions/workflows/python-ci.yml/badge.svg)
![.NET CI](https://github.com/YOUR_USER/CaseWeek2023/actions/workflows/dotnet-ci.yml/badge.svg)
```

### Exercise 5 — Slack notification (optional)

**Goal:** Notify a channel when a workflow completes.

1. Create a Slack incoming webhook.
2. Store URL as GitHub secret `SLACK_WEBHOOK_URL`.
3. Add a final step (example):

```yaml
- name: Notify Slack
  if: always()
  uses: slackapi/slack-github-action@v1.24.0
  with:
    payload: |
      {"text": "Workflow ${{ github.workflow }} finished with status ${{ job.status }}"}
  env:
    SLACK_WEBHOOK_URL: ${{ secrets.SLACK_WEBHOOK_URL }}
```

This was optional in the workshop; not included in reference workflows by default.

---

## Session 3

### Exercise 6 — Explore Azure with CLI

**Goal:** Find your App Service resources from the command line.

```bash
az login
az group list --output table
az appservice plan list --output table
az webapp list --output table
az webapp show --name YOUR_WEBAPP_NAME --resource-group YOUR_RG --output table
```

During CaseWeek, students looked up **their** pre-assigned web app. For self-study, use resources you create (see [self-study-azure.md](self-study-azure.md)).

### Exercise 7 — Deploy Python app to Azure

**Goal:** CD from GitHub Actions to App Service.

1. Create a Web App (Python 3.x stack) in Azure.
2. Download **Publish profile** from the app’s Overview blade.
3. In GitHub: **Settings → Secrets → Actions** → create `AZURE_WEBAPP_PYTHON_PUBLISH_PROFILE` with the full XML content.
4. In [`.github/workflows/azure-webapps-python.yml`](../.github/workflows/azure-webapps-python.yml), set:

```yaml
env:
  AZURE_WEBAPP_NAME: your-webapp-name
```

5. Push to `main` or run **workflow_dispatch**.
6. Open `https://your-webapp-name.azurewebsites.net`.

**Workshop gotcha:** Templates often use `Python/src`; this repo uses **`Python/source`**. The archival workflow already points to the correct directory.

### Exercise 8 — Deploy .NET app to Azure

**Goal:** Build, publish, and deploy ASP.NET Core to App Service.

1. Create a Web App (.NET 6 stack).
2. Add secret `AZURE_WEBAPP_DOTNET_PUBLISH_PROFILE`.
3. Configure [`.github/workflows/azure-webapps-dotnet.yml`](../.github/workflows/azure-webapps-dotnet.yml) with your app name.
4. Push and verify deployment.

During the live workshop, students had to **find missing configuration** (app name, secret names, publish output path). The reference workflow in this repo is complete; compare with what you would write from scratch.

### Exercise 9 — Service principal login (advanced)

**Goal:** Understand non–publish-profile authentication (covered in slides).

Alternative to publish profile:

1. Create an App Registration / service principal with contributor access to the resource group.
2. Store `AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_SUBSCRIPTION_ID`, `AZURE_CLIENT_SECRET` as secrets.
3. Add before deploy:

```yaml
- uses: azure/login@v2
  with:
    client-id: ${{ secrets.AZURE_CLIENT_ID }}
    tenant-id: ${{ secrets.AZURE_TENANT_ID }}
    subscription-id: ${{ secrets.AZURE_SUBSCRIPTION_ID }}
```

Publish profiles were used in the workshop for simplicity; service principals scale better for teams.

---

## Checklist

- [ ] Hello workflow runs on GitHub
- [ ] Python CI passes on `main`
- [ ] .NET CI passes on `main`
- [ ] Fixed intentional failing test exercise
- [ ] Status badge visible in README
- [ ] Azure Web App created in your subscription
- [ ] Python or .NET CD workflow deploys successfully
- [ ] (Optional) Slack or Teams notification on pipeline result
