#!/usr/bin/zsh

# Passing the project name as an argument
project_name=$1

# Syncing the project
echo "Syncing project: $project_name"
source_path="../codecrafters-$project_name-python"
target_path="./$project_name-python"

# Makedir if not exists
if [ ! -d $target_path ]; then
	mkdir $target_path
fi
cp -rf $source_path/* $target_path/
rm -rf $target_path/.git

# Committing the changes
git add .
echo "Done, please commit to git"
