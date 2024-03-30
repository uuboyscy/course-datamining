#!/bin/bash
set -x

cp /root/.gitconfig_mounted /root/.gitconfig \
&& cp -r /root/.ssh_mounted/* /root/.ssh/ \
&& chmod 400 /root/.ssh/id_rsa \
&& chmod 755 /root/.ssh/config

git config --global --add safe.directory /workspaces/*

sed -i 's/ZSH_THEME="robbyrussell"/ZSH_THEME="xiong-chiamiov-plus"/' /root/.zshrc \
&& sed -i '/HIST_STAMPS="mm\/dd\/yyyy"/s/^#*//;s/mm\/dd\/yyyy/yyyy-mm-dd/' /root/.zshrc

zsh
