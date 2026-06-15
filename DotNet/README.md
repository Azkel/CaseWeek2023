# .NET sample — CaseWeek 2023

ASP.NET Core 6 **Razor Pages** web application used in the CI/CD workshop track.

## Layout

```
DotNet/src/
├── ExampleWebApp/           # Web app (solution root)
│   ├── ExampleWebApp.sln
│   └── ExampleWebApp.csproj
└── ExampleWebApp.Tests/     # MSTest unit tests
```

## Run locally

```bash
cd DotNet/src/ExampleWebApp
dotnet restore
dotnet build
dotnet test ../ExampleWebApp.Tests/ExampleWebApp.Tests.csproj
dotnet run --project ExampleWebApp/ExampleWebApp.csproj
```

Open the URL shown in the console (typically `https://localhost:7xxx`).

## CI/CD

| Workflow | File |
|----------|------|
| Build & test | [`.github/workflows/dotnet-ci.yml`](../.github/workflows/dotnet-ci.yml) |
| Deploy to Azure App Service | [`.github/workflows/azure-webapps-dotnet.yml`](../.github/workflows/azure-webapps-dotnet.yml) |

During the workshop, students completed the deployment workflow configuration (app name, secrets, publish path). See [docs/exercises.md](../docs/exercises.md).

## Failing pipeline exercise

[`ExampleWebApp.Tests/UnitTest1.cs`](src/ExampleWebApp.Tests/UnitTest1.cs) contains a commented `Assert.Fail()` — uncomment it to simulate a broken pipeline, then fix it to restore green builds.
