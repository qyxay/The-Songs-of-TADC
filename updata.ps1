$REPO_BRANCH = "main"
$COMMIT_MSG = "Update TADC audio files"
# ----------------------------------------
git status
git add .
git commit -m $COMMIT_MSG
git stash push -m "temp stash before pull"
git pull origin $REPO_BRANCH --rebase
git stash pop
git push origin $REPO_BRANCH
git log --oneline -3