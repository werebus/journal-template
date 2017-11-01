from mako.template import Template
import jrnl.cli
import sys
import os

this_dir = os.path.dirname(os.path.realpath(sys.argv[0]))
config_template = Template(filename=this_dir + '/jrnl_config.tpl')

conf = open(jrnl.cli.CONFIG_PATH, 'w')
conf.write(config_template.render(dir=this_dir))
conf.close()
