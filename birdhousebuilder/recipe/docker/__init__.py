# -*- coding: utf-8 -*-
# Copyright (C)2014 DKRZ GmbH

"""Recipe docker"""

import os
from mako.template import Template

from birdhousebuilder.recipe import conda

templ_dockerfile = Template(filename=os.path.join(os.path.dirname(__file__), "Dockerfile"))

class Recipe(object):
    """Buildout recipe to generate a Dockerfile."""

    def __init__(self, buildout, name, options):
        self.buildout, self.name, self.options = buildout, name, options
        b_options = buildout['buildout']

        self.buildout_dir = b_options.get('directory')
        self.anaconda_home = b_options.get('anaconda-home', conda.anaconda_home())
        self.conda_channels = b_options.get('conda-channels')
        
        self.options['image-name'] = options.get('image-name', 'ubuntu')
        self.options['image-version'] = options.get('image-version', 'latest')
        self.options['maintainer'] = options.get('maintainer', 'Generated by birdhousebuilder.recipe.docker')

    def install(self):
        installed = []
        installed += list(self.install_dockerfile())
        return installed

    def install_dockerfile(self):
        result = templ_dockerfile.render(
            image_name = self.options['image-name'],
            image_version = self.options['image-version'],
            maintainer = self.options['maintainer'])
        output = os.path.join(self.buildout_dir, 'Dockerfile')
        
        try:
            os.remove(output)
        except OSError:
            pass

        with open(output, 'wt') as fp:
            fp.write(result)
            os.chmod(output, 0o644)
        return [output]

    def update(self):
        return self.install()

def uninstall(name, options):
    pass

