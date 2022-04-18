#!/usr/bin/env bash
# enable Kodi addon
#
# $1 = addon_id

addon_id=$1
if [ -z "${addon_id}" ]
then
  echo "addon_id must be provided as argument"
  exit 1
fi

kodi_version=`kodi --version | head -n1 | cut -d '.' -f1`
if [ -z "${kodi_version}" ]
then
  echo "Could not determine kodi version. Exiting."
  exit 1
fi

case "${kodi_version}" in
  19) db=~/.kodi/userdata/Database/Addons27.db
      ;;
esac

# init empty db
if [ ! -f "${db}" ]
then
  mkdir -p ~/.kodi/userdata/Database
  sqlite3 "${db}" <<"HERE"
CREATE TABLE version (idVersion integer, iCompressCount integer);
CREATE TABLE repo (id integer primary key, addonID text,checksum text, lastcheck text, version text);
CREATE TABLE addonlinkrepo (idRepo integer, idAddon integer);
CREATE TABLE broken (id integer primary key, addonID text, reason text);
CREATE TABLE blacklist (id integer primary key, addonID text);
CREATE TABLE package (id integer primary key, addonID text, filename text, hash text);
CREATE TABLE installed (id INTEGER PRIMARY KEY, addonID TEXT UNIQUE, enabled BOOLEAN, installDate TEXT, lastUpdated TEXT, lastUsed TEXT, origin TEXT NOT NULL DEFAULT '');
CREATE TABLE addons (id INTEGER PRIMARY KEY,metadata BLOB,addonID TEXT NOT NULL,version TEXT NOT NULL,name TEXT NOT NULL,summary TEXT NOT NULL,description TEXT NOT NULL, news TEXT NOT NULL DEFAULT '');
CREATE INDEX idxAddons ON addons(addonID);
CREATE UNIQUE INDEX ix_addonlinkrepo_1 ON addonlinkrepo ( idAddon, idRepo )
;
CREATE UNIQUE INDEX ix_addonlinkrepo_2 ON addonlinkrepo ( idRepo, idAddon )
;
CREATE UNIQUE INDEX idxBroken ON broken(addonID);
CREATE UNIQUE INDEX idxBlack ON blacklist(addonID);
CREATE UNIQUE INDEX idxPackage ON package(filename);
INSERT INTO version (idVersion, iCompressCount) VALUES (27, 0);
HERE
fi

if [ -z "${db}" ]
then
  echo "No db found, skipped" >&2
  exit
fi

sqlite3 "${db}" 'SELECT * from installed where addonID="'"${addon_id}"'"' | grep -q "${addon_id}"
if [ $? -ne 0 ]
then
  echo "Adding ${addon_id} to list of installed addons and enabling it.."
  sqlite3 "${db}" 'INSERT INTO installed (addonId, enabled, installDate) VALUES ("'"${addon_id}"'", 1, "1970-01-01 00:00:01");'
else
  echo "Making sure ${addon_id} is enabled.."
  sqlite3 "${db}" 'UPDATE installed SET enabled=1 WHERE addonId="'"${addon_id}"'"'
fi