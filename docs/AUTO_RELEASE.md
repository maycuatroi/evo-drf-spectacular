# Auto Release Documentation

This document describes the automated release process for drf-spectacular.

## Overview

The repository now includes automated version bumping and PyPI releases that trigger after successful CI runs on the master branch.

## Workflow Files

### 1. `auto-release.yml` (Simple Version)
- Triggers after CI workflow completes successfully on master
- Automatically bumps the patch version (e.g., 0.28.0 → 0.28.1)
- Creates a git tag and triggers the existing release workflow

### 2. `auto-release-advanced.yml` (Advanced Version)
- Includes all features of the simple version
- Supports manual triggering with version bump selection
- Detects version bump type from commit messages:
  - `[major]` in commit message → major version bump
  - `[minor]` in commit message → minor version bump
  - Default → patch version bump
- Generates changelog from recent commits

## How It Works

1. **CI Completion**: When CI tests pass on the master branch
2. **Version Bump**: The workflow reads the current version from `drf_spectacular/__init__.py` and increments it
3. **Commit & Tag**: Creates a commit with the version change and a corresponding git tag
4. **Release**: The existing `release.yml` workflow is triggered by the new tag
5. **PyPI Upload**: The release workflow builds and uploads the package to PyPI

## Usage

### Automatic Releases

By default, every successful CI run on master will trigger a patch version release.

### Controlling Releases

#### Skip Release
Add `[skip release]` to your commit message to prevent auto-release:
```bash
git commit -m "Update docs [skip release]"
```

#### Skip CI and Release
Add `[skip ci]` to skip both CI and release:
```bash
git commit -m "Update version [skip ci]"
```

#### Version Bump Types
Control the version bump type in commit messages:
- `[major]` - Bumps major version (1.0.0 → 2.0.0)
- `[minor]` - Bumps minor version (1.0.0 → 1.1.0)
- Default - Bumps patch version (1.0.0 → 1.0.1)

Example:
```bash
git commit -m "Add new API feature [minor]"
```

### Manual Release

You can manually trigger a release with a specific version bump:

1. Go to Actions → Auto Release Advanced
2. Click "Run workflow"
3. Select version bump type (patch/minor/major)
4. Run the workflow

### Manual Version Bumping

Use the provided script for local version bumping:
```bash
# Bump patch version
python scripts/bump_version.py

# Bump minor version
python scripts/bump_version.py minor

# Bump major version
python scripts/bump_version.py major
```

## Configuration

### Required Secrets

Ensure the following secrets are configured in your repository:
- `PYPI_API_TOKEN` - PyPI API token for package uploads

### Workflow Selection

Choose which auto-release workflow to use:
- Use `auto-release.yml` for simple patch-only releases
- Use `auto-release-advanced.yml` for full control over version bumps

Enable only one workflow by renaming or deleting the other.

## Best Practices

1. **Commit Messages**: Use clear commit messages that indicate the type of change
2. **Testing**: Ensure all tests pass before merging to master
3. **Version Control**: Review version bumps before major releases
4. **Manual Override**: Use `[skip release]` for commits that shouldn't trigger releases

## Troubleshooting

### Release Not Triggering
- Check if CI passed successfully
- Verify you're on the master branch
- Check for `[skip release]` or `[skip ci]` in commit message

### Version Already Exists
- The workflow checks for existing tags and skips if version exists
- Manually bump version if needed

### PyPI Upload Fails
- Verify `PYPI_API_TOKEN` secret is set correctly
- Check PyPI for any service issues