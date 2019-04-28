Basic workflow
--------------
*   The 3(4) states: committed, modified, staged (, untracked)

        1. modify files in the working tree
        2. selectively stage changes
        3. commit

*   Communicate with git

        command line (recommended), other...

*   First time setup

      * Config locations

        precedence like in css files, each level overrides the previous level:
        system < profile (user) < specific repository

        | Windows
        | system = ``C:\ProgramData\Git\config`` - usually should not be modified directly
        | global = ``$HOME\.gitconfig``

        | Linux
        | system = ``/etc/gitconfig``
        | global = ``~/.gitconfig or ~/.config/git/config``


        ``git config --list --show-origin``

      * identity, editor, ssh

        identity

        .. code-block:: bash

            git config --global user.name "John Doe"
            git config --global user.email johndoe@example.com

        editor

        .. code-block:: bash

            # linux:
            git config --global core.editor vim (also the default)
            # windows:
            git config --global core.editor "'C:/Program Files/Notepad++/notepad++.exe' -multiInst -nosession"

        ssh

        for communicating with git repository on the server
