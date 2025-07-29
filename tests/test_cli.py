import subprocess
import sys

from space_war import __version__


def test_cli_version():
    cmd = [sys.executable, "-m", "space_war", "--version"]
    assert subprocess.check_output(cmd).decode().strip() == __version__
