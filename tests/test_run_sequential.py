import subprocess
import pytest
import sys
from pathlib import Path

# Get project root path dynamically
PROJECT_ROOT = Path(__file__).parent.parent

@pytest.mark.order(1)
def test_run_prpose():
    """Run prpose.py first"""
    prpose_script = PROJECT_ROOT / "Pages" / "managementcommitee_propose.py"
    subprocess.run([sys.executable, str(prpose_script)], check=True)

@pytest.mark.order(2)
def test_run_rec():
    """Run managementcommittee_recommender.py after prpose.py"""
    rec_script = PROJECT_ROOT / "Pages" / "managementcommittee_recommender.py"
    subprocess.run([sys.executable, str(rec_script)], check=True)
