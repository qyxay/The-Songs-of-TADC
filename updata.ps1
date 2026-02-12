# ====================== 配置项（可修改！）======================
$REPO_BRANCH = "main"          # 你的分支名（main/master）
$COMMIT_MSG = "Update TADC audio files"   # 自定义提交信息
# ================================================================

Write-Host "===== 1. 检查 Git 状态 =====" -ForegroundColor Green
git status

Write-Host "`n===== 2. 暂存所有本地更新 =====" -ForegroundColor Green
git add .

Write-Host "`n===== 3. 提交变更 =====" -ForegroundColor Green
git commit -m $COMMIT_MSG

# 处理本地与远程不同步问题
Write-Host "`n===== 4. 同步远程仓库最新内容 =====" -ForegroundColor Green
# 暂存未提交的变更
git stash push -m "temp stash before pull"
# 拉取远程最新内容
git pull origin $REPO_BRANCH --rebase
# 恢复暂存的变更
git stash pop

Write-Host "`n===== 5. 推送到 GitHub =====" -ForegroundColor Green
git push origin $REPO_BRANCH

Write-Host "`n===== 操作完成！=====" -ForegroundColor Green
# 验证推送结果
git log --oneline -3