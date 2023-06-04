# flake8: noqa F401
import pytest
import subprocess
from mkShapesRDF.lib.utils import getFrameworkPath

fwPath = getFrameworkPath()


def test_compile():
    r"""Test the compilation of the configuration folder ``examples/2016Real``."""
    proc = subprocess.Popen(
        f"cd {fwPath} && source start.sh; cd examples/2016Real && mkShapesRDF -c 1",
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        executable="/bin/bash",
    )
    out, err = proc.communicate()
    print(out)
    print(err)
    assert proc.returncode == 0


def test_run_10evts():
    r"""Test the compilation and run on 10 events for the configuration folder ``examples/2016Real``."""
    proc = subprocess.Popen(
        f"cd {fwPath} && source start.sh; cd examples/2016Real && mkShapesRDF -c 1 -o 0 -l 10",
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        executable="/bin/bash",
    )
    out, err = proc.communicate()
    print(out)
    print(err)
    assert proc.returncode == 0
