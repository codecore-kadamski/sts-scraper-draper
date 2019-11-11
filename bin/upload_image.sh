#! /bin/sh

version=`sed -ne '/current_version/s/current_version = //p' < setup.cfg`
docker tag $1 $GITHUB_REGISTRY/$1:v$version
docker push $GITHUB_REGISTRY/$1:v$version
