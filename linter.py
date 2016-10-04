# Written by tbeu
# Copyright (c) 2014 tbeu
# License: MIT
# Changed for CudaLint: Alexey T.

import os
from cuda_lint import Linter, util


class MoParser(Linter):
    """Provides an interface to moparser."""

    syntax = 'Modelica'
    cmd = ('moparser', '-e', '@')

    regex = r'^.+ on line (?P<line>\d+).+:\s+(?P<message>.+)'
    tempfile_suffix = '.mo'
    error_stream = util.STREAM_STDOUT
