#!/bin/bash
set -e

BACKUP_ROOT="../Pirjo_Website_Backups"

if [ ! -d "$BACKUP_ROOT" ]; then
  echo "Backup folder not found: $BACKUP_ROOT"
  exit 1
fi

echo "Available backups, newest first:"
echo

BACKUPS=()
i=1
for d in "$BACKUP_ROOT"/Pirjo_Website_Project_backup_*; do
  [ -d "$d" ] || continue
  BACKUPS+=("$d")
done

if [ ${#BACKUPS[@]} -eq 0 ]; then
  echo "No backups found."
  exit 1
fi

IFS=$'\n' BACKUPS_SORTED=($(ls -td "${BACKUPS[@]}"))
unset IFS

for d in "${BACKUPS_SORTED[@]}"; do
  echo "[$i] $(basename "$d")"
  i=$((i+1))
done

echo
read -p "Type the backup number to restore: " CHOICE

if ! [[ "$CHOICE" =~ ^[0-9]+$ ]]; then
  echo "Invalid choice."
  exit 1
fi

INDEX=$((CHOICE-1))

if [ "$INDEX" -lt 0 ] || [ "$INDEX" -ge "${#BACKUPS_SORTED[@]}" ]; then
  echo "Choice out of range."
  exit 1
fi

SELECTED="${BACKUPS_SORTED[$INDEX]}"

echo
echo "Restoring from:"
echo "$SELECTED"

cp "$SELECTED/src/_includes/base.njk" src/_includes/base.njk
cp "$SELECTED/src/index.md" src/index.md

echo
echo "Restore done."
