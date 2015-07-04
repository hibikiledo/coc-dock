__author__ = 'Hibiki'

from utils import pretty_subprocess
from utils import make_fn_call


matlab_bin = '/Applications/MATLAB_R2014a.app/bin/matlab';

matlab_opts = ' '.join([
    '-nodesktop', '-nosplash',    # options
])

base_cmd = "cd matlabs"


def preprocess(infname, outfname):

    fn_str = make_fn_call('preprocess', ['../screenshots/'+infname, '../screenshots/'+outfname])

    cmd = MatlabCommandBuilder()
    cmd.inject(base_cmd).inject(fn_str)

    pretty_subprocess([matlab_bin, matlab_opts, '-r', cmd.cmd_string()], 'preprocess.m')


def locateres(imfname, temfname, scrapfname):

    fn_str = make_fn_call('locateres', ['../screenshots/'+imfname, '../templates/'+temfname, '../temp/'+scrapfname])

    cmd = MatlabCommandBuilder()
    cmd.inject(base_cmd).inject(fn_str)

    pretty_subprocess([matlab_bin, matlab_opts, '-r', cmd.cmd_string()], 'locateres.m')


'''
    CommandBuilder class handles concatination of commands
    Code is much cleaner !
'''
class MatlabCommandBuilder:

    def __init__(self):
        self.cmds = []

    def inject(self, cmd):
        self.cmds.append(cmd)
        return self

    def cmd_string(self):
        return ';'.join(self.cmds)