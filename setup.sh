#!/bin/bash
# Example Execution for Ubuntu default
#  sudo ./setup.sh -d /etc/datadog-agent

while getopts d: flag
do
    case "${flag}" in
        d) dir=${OPTARG};;
    esac
done
echo "Datadog Agent Directory Path: $dir";

# Copy conf.d directories
for conf_dir in ./conf.d/*/     
do
    conf_dir=${conf_dir%*/}
    target_path=$dir${conf_dir:1}
    mkdir -p $target_path
    cp $conf_dir/* $target_path
    echo "Copied $conf_dir and its contents to $target_path"
done

# Copy checks.d files
cp ./checks.d/* $dir/checks.d/
