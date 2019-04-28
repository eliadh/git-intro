What is git ?
=============
Introduction
------------
*   Version control is not a backup
*   Snapshots, not differences

    Every commit contains a complete snapshot of the repository. tree = directory and blob = file.
*   Nearly every operation is local

    Since all the repository is local almost everything happens at local

*   Integrity - fear not the sha!

    Every object in git structure get sha-1 [1]_ unique identifier.
