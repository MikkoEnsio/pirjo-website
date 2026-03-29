#!/bin/bash
set -e

BACKUP_ROOT="../Pirjo_Website_Backups"
PROJECT_NAME="$(basename "$PWD")"
STAMP="$(date +%Y%m%d_%H%M%S)"
DEST="$BACKUP_ROOT/${PROJECT_NAME}_backup_$STAMP"

mkdir -p "$BACKUP_ROOT"
cp -R . "$DEST"

echo "Backup created:"
echo "$DEST"
