
# Go to directory
cd ~/GitHub/econgrowth.github.io-src

# Clone
git clone git@github.com:econgrowth/econgrowth.github.io-src ghpages

# Move into directory for pages and check
cd ghpages
git remote -v

# Clone output
git submodule add git@github.com:econgrowth/econgrowth.github.io.git output

# Create baseline
pelican-quickstart

# copy files
ipython copy_content.ipy

# Create content and see website
make html && make serve
make html && make publish && make serve
# If it is ok
make html && make publish

# Publish and git commit
cd output
git add .
git commit -m "V.1.0"
git push -u origin master
cd ..
echo '*.pyc' >> .gitignore #don't need pyc files
git add .
git commit -m "V1.0"
git push -u origin master

# Publish and git commit
cd output
git add .
git commit -m "Updated jupyter notebooks Economic Data"
git push -u origin master
cd ..
git add .
git commit -m "Updated jupyter notebooks Economic Data"
git push -u origin master

cd output
git add .
git commit -m "Updated gitignore"
git push -u origin master
cd ..
git add .
git commit -m "Updated gitignore"
git push -u origin master
