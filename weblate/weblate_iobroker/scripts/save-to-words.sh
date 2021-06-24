#!/bin/bash
npm install
if [[ $(jq '.scripts.translate!=null' package.json) = 'true' ]]
then
    npm run translate adminLanguages2words
else
    gulp adminLanguages2words
fi
git add .
