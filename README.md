This repo includes some support files for using [jrnl](http://jrnl.sh/) and
tracking the resulting journal files in git.

Copying the template
====================

You *can* fork this to create your own, but you'll probably want to make your
fork private. To do so, do the following:

1. Create a new repo on GitHub using the UI, we'll call it `youruser/journal`

2. Clone and push to your new repo:

    ```
    git clone --bare https://github.com/werebus/journal-template.git
    cd journal-template.git
    git push --mirror git@github.com:youruser/journal.git
    cd ..
    rm -rf journal-template.git
    ```

3.  Clone your private copy

    ```
    git clone git@github.com:youruser/journal.git
    ```

4.  Optionally, add the template as an upstream for updates

    ```
    cd journal
    git remote add upstream https://github.com/werebus/journal-template.git
    ```

Installing the software
=======================

```
pip install -r requirements.txt
python install.py
```

This will install some Python libraries. In addition, it will output a
`.jrnl_config` file in the default location (usually your home directory).
You may edit that file however you like. The install script also removes
`*.txt` from the `.gitignore` file, so you can actually track _your_ journal.

Modifying the license
=====================

Likely -- for the same reason that you might want to keep your repository
private -- you'll want to modify the license file to exclude your journal
contents.
