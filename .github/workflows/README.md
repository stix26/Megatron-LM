# CI/CD Workflow Documentation

This directory contains GitHub Actions workflows for the Megatron-LM project.

## Workflows

### CI Workflow (`ci.yml`)

The main CI workflow that runs on every push to main/develop branches and pull requests.

#### Jobs Overview

1. **Code Quality & Linting** (`lint`)
   - Runs code formatting checks (Black, isort)
   - Performs static code analysis (flake8, pylint)
   - Type checking with mypy
   - Security linting with bandit

2. **Unit Tests** (`unit-tests`)
   - Runs unit tests across multiple Python versions (3.8, 3.9, 3.10)
   - Generates coverage reports
   - Uploads coverage to Codecov

3. **Integration Tests** (`integration-tests`)
   - Runs functional/integration tests
   - Depends on unit tests completion
   - Uses longer timeout for complex tests

4. **Security Scanning** (`security`)
   - Vulnerability scanning with Safety
   - Security code analysis with Bandit
   - Container and filesystem scanning with Trivy
   - Uploads results to GitHub Security tab

5. **Docker Build & Test** (`docker`)
   - Builds all Docker images (ci.dev, ci.lts, linting)
   - Tests Docker image functionality
   - Security scanning of Docker images
   - Validates containerization

6. **Dependency Management** (`dependencies`)
   - Checks for unused dependencies
   - Generates dependency tree
   - Validates package requirements

7. **Build Package** (`build`)
   - Creates distributable packages
   - Validates build process
   - Uploads build artifacts

8. **Performance Tests** (`performance`)
   - Basic performance benchmarking
   - Memory usage validation
   - Import time checks

9. **Documentation Check** (`docs`)
   - Validates documentation build
   - Checks README integrity
   - Ensures documentation completeness

10. **CI Status Summary** (`status`)
    - Provides overall CI status
    - Reports job results
    - Ensures critical jobs passed

#### Triggers

- **Push**: Runs on pushes to `main` and `develop` branches
- **Pull Request**: Runs on all PRs to `main` and `develop`
- **Schedule**: Weekly security scans (Mondays at 2 AM UTC)

#### Environment Variables

- `PYTHON_VERSION`: Default Python version (3.9)
- `PIP_CACHE_DIR`: Cache directory for pip dependencies

#### Dependencies

The workflow uses the following key dependencies:
- `requirements_ci.txt`: CI-specific requirements
- `requirements_mlm.txt`: Main project requirements
- `pyproject.toml`: Project configuration
- `setup.py`: Package setup

#### Security Features

1. **Vulnerability Scanning**
   - Safety: Checks for known vulnerabilities in dependencies
   - Bandit: Static analysis for common security issues
   - Trivy: Comprehensive vulnerability scanner

2. **Code Quality**
   - Black: Code formatting
   - isort: Import sorting
   - flake8: Style guide enforcement
   - pylint: Code analysis
   - mypy: Type checking

3. **Container Security**
   - Docker image vulnerability scanning
   - Container build validation
   - Security best practices enforcement

#### Artifacts

The workflow generates several artifacts:
- Coverage reports (HTML, XML)
- Security scan reports (JSON, SARIF)
- Build packages (wheel, source)
- Dependency trees
- Test results

#### Failure Handling

- Critical jobs (lint, unit-tests, security) must pass for overall success
- Non-critical jobs can fail without blocking the pipeline
- Detailed error reporting and logging
- Retry logic for transient failures

#### Performance Optimizations

- Dependency caching with pip
- Parallel job execution where possible
- Conditional job execution based on file changes
- Efficient resource usage

#### Monitoring

- GitHub Security tab integration
- Codecov coverage tracking
- Detailed job status reporting
- Artifact preservation for analysis

## Configuration Files

### `.bandit`
Bandit security scanner configuration:
- Excludes test directories
- Skips false positives for ML code
- Comprehensive test coverage
- Configurable severity levels

### `.flake8`
Flake8 linting configuration:
- Line length limits
- Complexity thresholds
- Error code selection
- Directory exclusions

### `.pylintrc`
Pylint configuration:
- Disable specific warnings
- Configure output format
- Set severity levels
- Customize analysis rules

### `mypy.ini`
MyPy type checking configuration:
- Type checking strictness
- Module exclusions
- Configuration options
- Error handling

## Usage

### Local Development

To run CI checks locally:

```bash
# Install CI dependencies
pip install -r requirements_ci.txt

# Run linting
black --check .
isort --check-only .
flake8 .
pylint megatron/

# Run tests
pytest tests/unit_tests/ -v

# Run security scans
bandit -r megatron/
safety check
```

### GitHub Actions

The workflow runs automatically on:
- Push to main/develop branches
- Pull requests
- Weekly scheduled runs

### Manual Trigger

You can manually trigger the workflow from the GitHub Actions tab.

## Troubleshooting

### Common Issues

1. **Dependency Conflicts**
   - Check `requirements_ci.txt` for conflicts
   - Update dependency versions
   - Review pip cache

2. **Test Failures**
   - Check test environment setup
   - Verify Python version compatibility
   - Review test dependencies

3. **Security Warnings**
   - Review Bandit configuration
   - Check for false positives
   - Update security rules

4. **Build Failures**
   - Verify setup.py configuration
   - Check package dependencies
   - Review build environment

### Debugging

- Check workflow logs for detailed error messages
- Review artifact contents for analysis
- Use local testing to reproduce issues
- Consult GitHub Actions documentation

## Contributing

When modifying the CI workflow:

1. Test changes locally first
2. Update documentation
3. Consider impact on build times
4. Maintain backward compatibility
5. Follow security best practices

## Support

For CI/CD related issues:
- Check GitHub Actions documentation
- Review workflow logs
- Consult project maintainers
- Open issues for bugs or improvements 