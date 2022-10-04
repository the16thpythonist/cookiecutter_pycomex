import os
import pathlib
import subprocess
import typing as t

PATH = pathlib.Path(__file__).parent.absolute()
PROJECT_PATH = os.path.dirname(PATH)


def run_command(command: str,
                cwd: t.Optional[str] = None,
                ) -> t.Tuple[subprocess.CompletedProcess, str, str]:
    proc = subprocess.run(
        command,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        cwd=cwd
    )
    out = proc.stdout.decode()
    err = proc.stderr.decode()

    return proc, out, err
