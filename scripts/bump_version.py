#!/usr/bin/env python
"""
Script to bump version in drf_spectacular/__init__.py

Usage:
    python scripts/bump_version.py [patch|minor|major]
    
Default is patch bump.
"""

import os
import re
import sys


def get_current_version():
    """Extract current version from __init__.py"""
    init_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 
                             'drf_spectacular', '__init__.py')
    with open(init_path, 'r') as f:
        content = f.read()
    
    match = re.search(r"__version__ = ['\"]([^'\"]+)['\"]", content)
    if not match:
        raise ValueError("Could not find version in __init__.py")
    
    return match.group(1)


def bump_version(current_version, bump_type='patch'):
    """Calculate new version based on bump type"""
    parts = current_version.split('.')
    if len(parts) != 3:
        raise ValueError(f"Invalid version format: {current_version}")
    
    major, minor, patch = map(int, parts)
    
    if bump_type == 'major':
        major += 1
        minor = 0
        patch = 0
    elif bump_type == 'minor':
        minor += 1
        patch = 0
    elif bump_type == 'patch':
        patch += 1
    else:
        raise ValueError(f"Invalid bump type: {bump_type}")
    
    return f"{major}.{minor}.{patch}"


def update_version_file(new_version):
    """Update version in __init__.py"""
    init_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 
                             'drf_spectacular', '__init__.py')
    
    with open(init_path, 'r') as f:
        content = f.read()
    
    content = re.sub(
        r"__version__ = ['\"]([^'\"]+)['\"]",
        f"__version__ = '{new_version}'",
        content
    )
    
    with open(init_path, 'w') as f:
        f.write(content)


def main():
    bump_type = sys.argv[1] if len(sys.argv) > 1 else 'patch'
    
    if bump_type not in ['patch', 'minor', 'major']:
        print(f"Error: Invalid bump type '{bump_type}'")
        print("Valid options: patch, minor, major")
        sys.exit(1)
    
    try:
        current = get_current_version()
        print(f"Current version: {current}")
        
        new = bump_version(current, bump_type)
        print(f"New version: {new}")
        
        update_version_file(new)
        print(f"Updated __init__.py with new version: {new}")
        
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()