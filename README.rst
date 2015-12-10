******************************
birdhousebuilder.recipe.docker
******************************

.. image:: https://travis-ci.org/bird-house/birdhousebuilder.recipe.docker.svg?branch=master
   :target: https://travis-ci.org/bird-house/birdhousebuilder.recipe.docker
   :alt: Travis Build

.. contents::

Introduction
************

``birdhousebuilder.recipe.docker`` is a `Buildout`_ recipe to generate a `Dockerfile`_ for `Birdhouse`_ applications.

.. _`Buildout`: http://buildout.org/
.. _`Dockerfile`: https://www.docker.com/
.. _`Birdhouse`: http://bird-house.github.io/

Usage
*****

The recipe will generate a Dockerfile for your application. You can find the Dockerfile in the root folder of the application. 

Supported options
=================

This recipe supports the following options:

**image-name**
   The docker base image name. Default is ``ubuntu``.

**image-version**
   The docker base image version. Default is ``latest``.

**maintainer**
   The maintainer of the Dockerfile.

**description**
   Description of the Dockerfile.

**vendor**
   The vendor of the application. Default: Birdhouse

**version**
   The version of the application. Default: 1.0.0

**expose**
   List of exposed ports.

**environment**
   List of KEY=value pairs added as ENV parameters in the Dockerfile.


Example usage
=============

The following example ``buildout.cfg`` generates a Dockerfile for Ubuntu 14.04:

.. code-block:: ini 

  [buildout]
  parts = docker

  [docker]
  recipe = birdhousebuilder.recipe.docker
  image-name = ubuntu
  image-version = 14.04
  maintainer = Birdhouse
  description = My Birdhouse App
  expose = 8090 8094
  environment =
       MY_DATA_DIR=/opt/data
       OUTPUT_PORT=8090




