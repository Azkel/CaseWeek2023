# Workshop guide — session by session

Archival notes for **Creating CI/CD Automation Using GitHub Actions — DevOps Deployments to Azure Cloud** (IAESTE CaseWeek 2023, AGH Kraków).

Original slide decks from the live sessions are not part of this repository archive. The sections below summarize what each session covered.

---

## Session 1 — Introduction (~1.5 h)

### Topics covered

- **DevOps** — culture, automation, and common specializations
- **CI vs CD vs Continuous Deployment** — definitions (Atlassian model)
- **Tooling landscape**
  - Version control: GitHub, GitLab, Bitbucket, Azure DevOps
  - CI: GitHub Actions, Jenkins, GitLab CI, Azure Pipelines, TeamCity
  - CD: same CI tools, Octopus Deploy, cloud-native pipelines
  - Deployment targets: on-premises, Azure, AWS, GCP
- **Languages in pipelines**
  - Pipeline definition: YAML (GitHub Actions), Groovy (Jenkins), JSON, others
  - Scripting: Bash, PowerShell, Python
  - Application code: depends on the project
- **GitHub Actions basics**
  - How to create a workflow from the Actions tab
  - What happens under the hood (runners, jobs, steps)
  - Anatomy of a YAML pipeline

### Exercise

**Exercise 1 — create a simple workflow**

Create a workflow that runs on `push` to `main` and prints a message or runs `echo "Hello from Actions"`. Use the GitHub Actions wizard or write YAML by hand.

Example minimal workflow:

```yaml
name: Hello CaseWeek
on:
  push:
    branches: [main]
jobs:
  greet:
    runs-on: ubuntu-latest
    steps:
      - run: echo "Hello from GitHub Actions"
```

### Logistics (live event)

Students shared e-mail addresses and GitHub usernames before the break so Azure and repository access could be prepared for Sessions 2–3.

---

## Session 2 — Continuous Integration (~1.5 h)

### Topics covered

- **Purpose of CI** — fast feedback, merge safety, quality gates
- **Branching strategies** — trunk-based, Gitflow, GitHub Flow; avoid `master`-only workflows
- **Pull request validation** — compile, mergeability, coverage and custom gates
- **Standard CI steps**
  1. Retrieve source code
  2. Install tooling
  3. Restore dependencies
  4. Build / compile
  5. Test
  6. Publish artifacts (build output, container image, package registry)
- **Extended pipeline ideas** — code coverage, E2E tests, OWASP ZAP, notifications, test database provisioning

### Reference workflows in this repo

- Python: [`.github/workflows/python-ci.yml`](../.github/workflows/python-ci.yml) — runs `python manage.py test` in `Python/source/`
- .NET: [`.github/workflows/dotnet-ci.yml`](../.github/workflows/dotnet-ci.yml) — `dotnet test` and `dotnet build`

### Two approaches taught for writing pipelines

1. **GitHub Action Wizard** — pick a template in the web UI, then adjust paths to match this repository layout.
2. **ChatGPT / AI assist** — generate an initial YAML, then fix paths, secrets, and runner images manually.

Always verify generated YAML; common mistakes are wrong working directories and outdated action versions.

### Exercises

See [exercises.md](exercises.md) for:

- Failing pipeline (fix intentional test bugs)
- README status badge
- Optional Slack notification on success/failure

---

## Session 3 — Continuous Deployment (~1.5 h)

### Topics covered

- **Cloud basics** — paying for managed infrastructure, ecosystem and scale
- **Accessing Azure**
  - Portal (beginner-friendly, troubleshooting)
  - Azure CLI (automation, JSON output)
  - REST API (what Portal and CLI use under the hood)
- **Authentication for pipelines**
  - User accounts vs **service principals**
  - Publish profiles vs `azure/login` + service principal secrets
- **Hosting models**
  - **IaaS** — VMs, full control, you manage OS and runtime
  - **PaaS** — App Service, Azure maintains platform; workshop focus
  - **Containers** — ACI, AKS; configuration portability
- **App Service resources**
  - Resource group
  - App Service Plan
  - Web App (and optionally deployment slots)
  - Related services (SQL, Storage, Key Vault) — mentioned, out of workshop scope
- **Infrastructure as Code** — Terraform, Bicep, Ansible; workshop used pre-provisioned resources

### Deployment flow taught

1. CI produces a deployable artifact (folder or published binaries).
2. CD job downloads the artifact on a fresh runner.
3. Deployment action pushes to Azure App Service using publish profile or Azure credentials.

### Reference CD workflows

- Python: [`.github/workflows/azure-webapps-python.yml`](../.github/workflows/azure-webapps-python.yml)
- .NET: [`.github/workflows/azure-webapps-dotnet.yml`](../.github/workflows/azure-webapps-dotnet.yml)

### Exercises

- Use Azure CLI to list App Service Plans and Web Apps (`az appservice plan list`, `az webapp list`).
- Complete the Python deployment pipeline (secrets + app name).
- Write or adapt the .NET deployment pipeline — during the workshop some values were left for students to discover.

### Azure CLI exercise (from slides)

```bash
# Install: https://learn.microsoft.com/cli/azure/install-azure-cli
az login
az appservice plan list --output table
az webapp list --output table
```

---

## Repository paths (important)

During the workshop, several student pipelines failed because templates assumed `Python/src/` while this repo uses **`Python/source/`**. All reference workflows in this archival repo use the correct path.

| Component | Correct path |
|-----------|--------------|
| Django project root | `Python/source/` |
| .NET solution | `DotNet/src/ExampleWebApp/ExampleWebApp.sln` |
| .NET tests | `DotNet/src/ExampleWebApp.Tests/` |

---

## Suggested self-study order

1. Read Session 1 notes below; create a hello-world workflow in your fork.
2. Enable `python-ci.yml` and `dotnet-ci.yml`; open a PR and observe checks.
3. Complete the failing-pipeline exercise.
4. Follow [self-study-azure.md](self-study-azure.md) to create App Service resources.
5. Configure CD secrets and run a deployment to your web app.
6. Add a status badge to your README.
