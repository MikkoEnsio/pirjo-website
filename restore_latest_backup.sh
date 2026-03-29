#!/bin/bash
set -e

BACKUP_ROOT="../Pirjo_Website_Backups"
LATEST_BACKUP=$(ls -td "$BACKUP_ROOT"/Pirjo_Website_Project_backup_* | head -n 1)

if [ -z "$LATEST_BACKUP" ]; then
  echo "No backup found."
  exit 1
fi

echo "Restoring from:"
echo "$LATEST_BACKUP"

cp "$LATEST_BACKUP/src/_includes/base.njk" src/_includes/base.njk
cp "$LATEST_BACKUP/src/index.md" src/index.md

echo "Restore done."
