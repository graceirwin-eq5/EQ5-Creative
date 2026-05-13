#!/bin/bash

cd /Users/graceirwin/Documents/GitHub/eq5-creative

echo "Adding all changes..."
git add .

echo "Enter a commit message:"
read message

git commit -m "$message"

echo "Pushing to GitHub..."
git push

echo "Done! Changes are live on GitHub."
