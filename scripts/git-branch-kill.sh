for branch in $(git for-each-ref --format '%(refname:short)' HEAD refs/heads/)
do
    git branch -d ${branch}
done
