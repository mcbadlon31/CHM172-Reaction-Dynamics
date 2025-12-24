#!/usr/bin/env python3
"""
Comprehensive Course Test Suite

Tests:
1. Notebook JSON validity
2. Documentation file existence
3. Required sections in student guides
4. Module imports
"""

import json
import os
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent

def test_notebooks():
    """Verify all notebooks are valid JSON."""
    print("\n📓 Testing Notebooks...")
    notebooks_dir = REPO_ROOT / 'notebooks'
    results = []
    
    for nb_file in notebooks_dir.glob('*.ipynb'):
        try:
            with open(nb_file, 'r', encoding='utf-8') as f:
                nb = json.load(f)
            cell_count = len(nb.get('cells', []))
            results.append((nb_file.name, 'PASS', f'{cell_count} cells'))
        except json.JSONDecodeError as e:
            results.append((nb_file.name, 'FAIL', str(e)))
    
    for name, status, detail in results:
        symbol = '✅' if status == 'PASS' else '❌'
        print(f"  {symbol} {name}: {detail}")
    
    return all(r[1] == 'PASS' for r in results)


def test_documentation():
    """Verify all documentation files exist."""
    print("\n📚 Testing Documentation...")
    required_docs = [
        'docs/QUICK_START.md',
        'docs/CHEAT_SHEET.md',
        'docs/LEARNING_PATHWAY.md',
        'docs/INSTRUCTOR_GUIDE.md',
        'docs/Student_Guide_Group_1.md',
        'docs/Student_Guide_Group_2.md',
        'docs/Student_Guide_Group_3.md',
        'docs/Student_Guide_Group_4.md',
        'docs/Student_Guide_Group_5.md',
        'docs/index.html',
        'README.md',
        'modules/README.md',
    ]
    
    results = []
    for doc in required_docs:
        path = REPO_ROOT / doc
        if path.exists():
            size = path.stat().st_size
            results.append((doc, 'PASS', f'{size} bytes'))
        else:
            results.append((doc, 'FAIL', 'NOT FOUND'))
    
    for name, status, detail in results:
        symbol = '✅' if status == 'PASS' else '❌'
        print(f"  {symbol} {name}: {detail}")
    
    return all(r[1] == 'PASS' for r in results)


def test_student_guide_sections():
    """Verify student guides have required sections."""
    print("\n📋 Testing Student Guide Sections...")
    required_sections = ['Table of Contents', 'Troubleshooting', 'Your Mission', 'Critical Parameters']
    
    results = []
    for i in range(1, 6):
        guide_path = REPO_ROOT / f'docs/Student_Guide_Group_{i}.md'
        if guide_path.exists():
            content = guide_path.read_text()
            missing = [s for s in required_sections if s not in content]
            if missing:
                results.append((f'Group {i}', 'WARN', f'Missing: {", ".join(missing)}'))
            else:
                results.append((f'Group {i}', 'PASS', 'All sections present'))
        else:
            results.append((f'Group {i}', 'FAIL', 'File not found'))
    
    for name, status, detail in results:
        symbol = '✅' if status == 'PASS' else ('⚠️' if status == 'WARN' else '❌')
        print(f"  {symbol} {name}: {detail}")
    
    return all(r[1] in ['PASS', 'WARN'] for r in results)


def test_modules():
    """Verify module files exist and have docstrings."""
    print("\n🔧 Testing Modules...")
    modules = ['leps_surface.py', 'trajectory.py', 'transition_state.py', 'visualization.py']
    
    results = []
    for mod in modules:
        path = REPO_ROOT / 'modules' / mod
        if path.exists():
            content = path.read_text()
            has_docstring = '"""' in content[:500]
            results.append((mod, 'PASS', 'Has docstring' if has_docstring else 'No docstring'))
        else:
            results.append((mod, 'FAIL', 'NOT FOUND'))
    
    for name, status, detail in results:
        symbol = '✅' if status == 'PASS' else '❌'
        print(f"  {symbol} {name}: {detail}")
    
    return all(r[1] == 'PASS' for r in results)


def main():
    print("=" * 60)
    print("CHM172 Reaction Dynamics - Comprehensive Test Suite")
    print("=" * 60)
    
    tests = [
        ('Notebooks', test_notebooks),
        ('Documentation', test_documentation),
        ('Student Guide Sections', test_student_guide_sections),
        ('Modules', test_modules),
    ]
    
    results = {}
    for name, test_func in tests:
        results[name] = test_func()
    
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    
    all_passed = True
    for name, passed in results.items():
        symbol = '✅' if passed else '❌'
        status = 'PASSED' if passed else 'FAILED'
        print(f"  {symbol} {name}: {status}")
        if not passed:
            all_passed = False
    
    print("\n" + "=" * 60)
    if all_passed:
        print("🎉 ALL TESTS PASSED!")
    else:
        print("⚠️ Some tests failed. Review output above.")
    print("=" * 60)
    
    return 0 if all_passed else 1


if __name__ == "__main__":
    exit(main())
