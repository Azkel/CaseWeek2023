# Creating CI/CD Automation Using GitHub Actions — DevOps Deployments to Azure Cloud

**Archived workshop materials** from [IAESTE CaseWeek 2023](https://caseweek.iaeste.pl/) at [AGH University of Science and Technology](https://www.agh.edu.pl/en/), Kraków, Poland.

| | |
|---|---|
| **Instructor** | [Michał Smyk](https://www.linkedin.com/in/michal-smyk/) |
| **Event language** | English |
| **Year** | 2023 |
| **Status** | Archived — not actively maintained; workflows updated for current GitHub Actions |

![Python CI](https://github.com/Azkel/CaseWeek2023/actions/workflows/python-ci.yml/badge.svg)
![.NET CI](https://github.com/Azkel/CaseWeek2023/actions/workflows/dotnet-ci.yml/badge.svg)

This repository preserves the **sample applications**, **reference GitHub Actions workflows**, and **written session notes** from a three-part workshop on CI/CD with GitHub Actions and Azure App Service. Slide decks from the live sessions are not included in this archive.

During the event, each student worked in a **personal GitHub repository** and deployed to **dedicated Azure App Service instances** provisioned for the class. You can reproduce the same learning path today with your own Azure subscription and GitHub account.

## What you will learn

- DevOps, CI, and CD in a practical pipeline context
- GitHub Actions workflows in YAML
- Build and test Python (Django) and .NET (ASP.NET Core) applications in CI
- Deploy web applications to **Azure App Service** (PaaS) from GitHub Actions
- Authenticate pipelines to Azure using **publish profiles** and **service principals**

## Workshop agenda (three sessions, ~4.5 h)

| Session | Topic | Duration |
|---------|--------|----------|
| 1 | Introduction — DevOps, tooling landscape, first GitHub Actions workflow | ~1.5 h |
| 2 | Continuous Integration — build, test, artifacts, PR validation, badges | ~1.5 h |
| 3 | Continuous Deployment — Azure overview, App Service, automated deployment | ~1.5 h |

Session notes and exercises: **[docs/workshop-guide.md](docs/workshop-guide.md)** · **[docs/exercises.md](docs/exercises.md)**

## Repository layout

```
CaseWeek2023/
├── Python/source/          # Django polls app (Microsoft sample, adapted for Azure App Service)
├── DotNet/src/             # ASP.NET Core 6 Razor Pages app + unit test project
├── .github/workflows/      # Reference CI/CD pipelines
└── docs/                   # Archival guides for self-study
```

### Sample applications

| Track | Path | Stack | CI workflow | CD workflow |
|-------|------|-------|-------------|-------------|
| Python | `Python/source/` | Django 3.x, PostgreSQL on Azure | [python-ci.yml](.github/workflows/python-ci.yml) | [azure-webapps-python.yml](.github/workflows/azure-webapps-python.yml) |
| .NET | `DotNet/src/ExampleWebApp/` | ASP.NET Core 6 Razor Pages | [dotnet-ci.yml](.github/workflows/dotnet-ci.yml) | [azure-webapps-dotnet.yml](.github/workflows/azure-webapps-dotnet.yml) |

The Python app is based on the [Microsoft Django + Azure App Service sample](https://learn.microsoft.com/azure/app-service/quickstart-python). The .NET app is a standard `dotnet new webapp` template with a minimal MSTest project.

## Quick start (self-study)

### 1. Fork or clone

```bash
git clone https://github.com/Azkel/CaseWeek2023.git
cd CaseWeek2023
```

### 2. Run CI locally (optional)

**Python** — from `Python/source/`:

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python manage.py test
```

**.NET** — from `DotNet/src/ExampleWebApp/`:

```bash
dotnet test ../ExampleWebApp.Tests/ExampleWebApp.Tests.csproj
dotnet build
```

### 3. CI on GitHub

Push to your fork. CI workflows run on `push` and `pull_request` to `main`.

### 4. Deploy to Azure (optional)

CD workflows are **manual only** (`workflow_dispatch`) — configure your own App Service first. See **[docs/self-study-azure.md](docs/self-study-azure.md)**.

1. Create an **App Service Plan** and **Web App** in the [Azure Portal](https://portal.azure.com).
2. Add a GitHub secret with the app's **publish profile**.
3. Set `AZURE_WEBAPP_NAME` in the CD workflow.
4. Run the workflow from the **Actions** tab.

> **Note:** The instructor-provided Azure subscription from CaseWeek 2023 is no longer available.

## How the live workshop worked

1. Students provided GitHub usernames and e-mail addresses before the CI/CD sessions.
2. Each student created a **personal repository** (often forked from templates like this one).
3. Pre-provisioned **Azure App Service** instances and **service principals** were shared per student or team.
4. Students wired GitHub Actions secrets, fixed pipeline paths, and ran successful deployments.
5. Exercises included intentionally failing tests, status badges, and (optionally) Slack notifications.

This repo is the **reference solution** for comparison or as a starting baseline.

## GitHub Actions workflows

| Workflow | Purpose | Triggers |
|----------|---------|----------|
| `python-ci.yml` | Install deps, run Django tests | push / PR → `main` |
| `dotnet-ci.yml` | Restore, build, test .NET solution | push / PR → `main` |
| `azure-webapps-python.yml` | Build artifact, deploy Django app to App Service | manual |
| `azure-webapps-dotnet.yml` | Build & publish .NET app, deploy to App Service | manual |

## Related links

- [Workshop listing — blog.smyk.it/talks](https://blog.smyk.it/talks/)
- [IAESTE CaseWeek](https://caseweek.iaeste.pl/)
- [GitHub Actions documentation](https://docs.github.com/en/actions)
- [Deploy to Azure App Service from GitHub Actions](https://learn.microsoft.com/azure/app-service/deploy-github-actions)

## License

See [LICENSE](LICENSE). The Python sample retains Microsoft sample licensing in `Python/source/LICENSE.md`.
