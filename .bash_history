ipython
wget https://github.com/Foundations-of-Applied-Mathematics/Student-Materials/raw/master/PythonEssentials.zipLinks to an external site.
unzip PythonEssentials.zip
cd PythonEssentials
wget https://github.com/Foundations-of-Applied-Mathematics/Student-Materials/raw/master/PythonEssentials.zip
unzip PythonEssentials.zip
cd PythonEssentials
./download_data.sh
ls
cd ..
wget https://github.com/Foundations-of-Applied-Mathematics/Student-Materials/raw/master/Volume1.zip
unzip Volume1.zip 
cd Volume1
./download_data.sh 
ls
cd ..
mv Volume1/* PythonEssentials/
mv Volume2/* PythonEssentials/
ssh-keygen -t ed25519 -C "munkr@oregonstate.edu"
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
wget https://github.com/Foundations-of-Applied-Mathematics/Student-Materials/raw/master/Volume2.zip
unzip Volume2.zip 
cd Volume2
./download_data.sh 
cd ..
mv Volume2/* PythonEssentials/
ssh-keygen -t ed25519 -C "munkr@oregonstate.edu"
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
cat ~/.ssh/id_ed25519.pub
clip.exe< ~/.ssh/id_ed25519.pub
cat ~/.ssh/id_ed25519.pub >/dev/clipboard
git init
git config --local user.name spiraldoodles
git config --local user.email munkr@oregonstate.edu
git remote add origin git@github.com:spiraldoodles/MTH420_RM.git
git add --all
git commit -m "initial commit"
git branch -M main
git push origin main
clip < ~/.ssh/id_ed25519.pub
clip.exe < ~/.ssh/id_ed25519.pub
git init
git remote add origin git@github.com:spiraldoodles/MTH420_RM.git
git branch -M main
git push origin main