#!/bin/bash
command -v curl > /dev/null 2>&1 || {  echo >&2 "Se requiere curl pero no está instalado. \n   Instalando..."; apt install curl -y; }
command -v python > /dev/null 2>&1 || {  echo >&2 "Se requiere python pero no está instalado. \n   Instalando..."; apt install python -y; }
command -v pip > /dev/null 2>&1 || {  echo >&2 "Se requiere pip pero no está instalado. \n   Instalando..."; curl https:bootstrap.pypa.io/get-pip.py -o get-pip.py && python get-pip.py ; }
command -v toilet > /dev/null 2>&1 || {  echo >&2 "Se requiere toilet pero no está instalado. \n   Instalando..."; apt install toilet -y; }