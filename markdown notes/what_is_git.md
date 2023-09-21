# What is Git?

Git is a version control system used for tracking changes to files. It is generally used for source code management in software development.



- Most file systems store information as file-based changes.
- Git thinks of data as a series of snapshots
- Each git "commit" takes a picture of how the files look in that moment and stores a reference to that snapshot.
- Git operates on local files

## Three states of git

- Modified - changed the file but not committed to database.
- Staged - you have a modified file in its current version to go into your next commit snapshot.
- Committed - the data is safely stored in the local database.

## Git workflow

The basic git workflow:

1) Modify files in your working tree.
2) Selectively stage just those changes you want to be part of your next commit.
3) Do a commit.
