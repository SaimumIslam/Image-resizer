#!/bin/sh

green=`tput setaf 2`
pink=`tput setaf 5`
aqua=`tput setaf 6`
reset=`tput sgr0`

echo "${pink} creating venv ${reset}"
python3 -m venv venv
source "venv/bin/activate"

echo "${aqua}  - install requirements packages ${reset}"
pip install -r requirements.txt

echo "${aqua}  - creating output folder ${reset}"
mkdir "output"
mkdir "input"

echo "${green}  Successful .${reset}"
