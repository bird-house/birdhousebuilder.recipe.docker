# vim:set ft=dockerfile:
FROM ${image_name}:${image_version}
MAINTAINER ${maintainer}

LABEL Description="${description}" Vendor="${vendor}" Version="${version}"

# Configure hostname and user for services 
ENV HOSTNAME localhost
ENV USER www-data
%for key,value in environment.items():
ENV ${key} ${value}
% endfor 

% if image_name.lower() in ['centos', 'fedora']:
# Setup sudo
RUN yum install -y sudo
# Don't require terminal when using sudo with root
RUN echo 'Defaults:root !requiretty' > /etc/sudoers.d/999-birdhouse
% endif

# Set current home
ENV HOME /root

# Add application sources
ADD . /opt/birdhouse

# cd into application
WORKDIR /opt/birdhouse

# Install system dependencies
RUN bash bootstrap.sh -i && bash requirements.sh

# Set conda enviroment
ENV ANACONDA_HOME /opt/conda
ENV CONDA_ENVS_DIR /opt/conda/envs

# Run install
RUN make clean install 

# Volume for data, cache, logfiles, ...
RUN chown -R $USER $CONDA_ENVS_DIR/birdhouse
RUN mv $CONDA_ENVS_DIR/birdhouse/var /data && ln -s /data $CONDA_ENVS_DIR/birdhouse/var
VOLUME /data/cache
VOLUME /data/lib

% if expose:
# Ports used in birdhouse
EXPOSE ${expose}
% endif

# Start supervisor in foreground
ENV DAEMON_OPTS --nodaemon --user $USER

# Update config and start supervisor ...
CMD ["make", "update-config", "start"]

