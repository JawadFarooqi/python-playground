#!/usr/bin/env python3
"""Simple test script that runs notebooks to verify they work."""

import subprocess
import sys
from pathlib import Path


def test_notebooks():
    """Test notebooks by executing them."""
    notebooks_dir = Path("notebooks")
    
    if not notebooks_dir.exists():
        print("❌ notebooks/ directory not found")
        return False
    
    # Find all notebooks
    notebooks = list(notebooks_dir.rglob("*.ipynb"))
    notebooks.sort()  # Process in order
    
    print(f"🧪 Testing {len(notebooks)} notebooks...")
    
    passed = 0
    failed = 0
    
    for notebook in notebooks:
        print(f"  Testing {notebook}...", end=" ")
        
        try:
            # Use nbconvert to execute the notebook
            result = subprocess.run([
                "jupyter", "nbconvert", 
                "--to", "notebook",
                "--execute",
                "--output", "/dev/null",  # Don't save output
                str(notebook)
            ], capture_output=True, timeout=30)
            
            if result.returncode == 0:
                print("✅")
                passed += 1
            else:
                print("❌")
                print(f"    Error: {result.stderr.decode()}")
                failed += 1
                
        except subprocess.TimeoutExpired:
            print("⏰ (timeout)")
            failed += 1
        except Exception as e:
            print(f"💥 (error: {e})")
            failed += 1
    
    print(f"\n📊 Results: {passed} passed, {failed} failed")
    return failed == 0


def test_code():
    """Test the Python code."""
    print("🐍 Testing Python code...")
    
    try:
        result = subprocess.run([
            sys.executable, "-m", "pytest", "tests/", "-v"
        ], capture_output=True)
        
        if result.returncode == 0:
            print("✅ All tests passed")
            return True
        else:
            print("❌ Some tests failed")
            print(result.stdout.decode())
            return False
            
    except Exception as e:
        print(f"💥 Error running tests: {e}")
        return False


def main():
    """Run all tests."""
    print("🚀 Python Playground Testing")
    print("=" * 30)
    
    # Test code first
    code_ok = test_code()
    
    # Then test notebooks
    notebooks_ok = test_notebooks()
    
    if code_ok and notebooks_ok:
        print("\n🎉 All tests passed!")
        return 0
    else:
        print("\n💥 Some tests failed!")
        return 1


if __name__ == "__main__":
    sys.exit(main())
