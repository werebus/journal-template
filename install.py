from mako.template import Template
import jrnl.cli
import sys
import os
import fileinput
import re

this_dir = os.path.dirname(os.path.realpath(sys.argv[0]))

# Output the config template in the default location for jrnl
config_template = Template(filename=this_dir + '/jrnl_config.tpl')
conf = open(jrnl.cli.CONFIG_PATH, 'w')
conf.write(config_template.render(dir=this_dir))
conf.close()

# Remove the exclusion of *.txt from git
match = re.compile('^\*.txt$').search
gitignore = this_dir + '/.gitignore'
with fileinput.FileInput(gitignore, inplace=1, backup='.old') as gifile:
    for line in gifile:
        if not match(line):
            print(line, end='')
