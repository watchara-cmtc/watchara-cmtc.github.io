#!/usr/bin/env sh

# abort on errors
# set -e

# build
python manage.py runserver

# navigate into the build output directory
# cd dist
# cp index.html 404.html
# cd ..

# if you are deploying to a custom domain
# echo 'www.example.com' > CNAME

git init
git add .
git commit -m 'deploy'

# if you are deploying to https://<USERNAME>.github.io
# git push -f https://github.com/guerriers/guerriers.github.io.git master

# if you are deploying to https://<USERNAME>.github.io/<REPO>
git push -f https://github.com/watchara-cmtc/watchara-cmtc.github.io.git main:gh-pages

# cd -