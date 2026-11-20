# Project Structure: [Your Project Name]

> Tool-neutral template. Replace every `[...]` placeholder. Describe YOUR project here,
> not the AI tooling. Where the tool-specific files live is documented in the readme.

```
my-project/
├── src/                        # Main source code
│   ├── __init__.py             # Public API exports
│   ├── service.py              # Business logic (Service Layer)
│   ├── repository.py           # Data access (Repository Pattern)
│   └── error.py                # Custom error classes
├── test/
│   ├── run.py                  # Test entry point
│   └── testcase/               # Test modules (one per feature area)
│       ├── __init__.py
│       └── feature_test.py
├── specs/                      # Feature-cut specs (one folder per feature)
│   └── <feature-name>/         # e.g. password-reset/
│       ├── requirements.md     # EARS criteria + glossary
│       ├── design.md           # Architecture, data flow, error handling
│       └── tasks.md            # Task checklist + dependency graph
├── setup.py                    # Package metadata and build config
├── requirements.txt            # Pinned dependencies
├── .env                        # Local environment variables (never commit)
└── readme.md                   # Usage documentation
```

## Architecture Notes

- **[Pattern name]**: [Description — e.g., "Service-Layer Pattern. Logic resides in service.py, separated from controllers/routes."]
- **[Module responsibility]**: [Description — e.g., "All custom errors extend BaseError in error.py. Error codes use offset 5000+."]
- **[Testing approach]**: [Description — e.g., "Tests run against the built artifact, not source directly. Test runner: pytest with coverage."]
- **[Data flow]**: [Description — e.g., "Request → Controller → Validation → Service → Repository → Response"]
