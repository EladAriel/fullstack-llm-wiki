---
type: "Framework Learn Page"
framework: "pytest"
source_repo: "https://github.com/pytest-dev/pytest"
source_branch: "main"
source_path: "doc/en/how-to/bash-completion.rst"
source_commit: "fdba12e1708313f56e9cf713d260c029764ca2b7"
source_commit_short: "fdba12e"
source_commit_date: "2026-08-27T21:55:50+02:00"
generated_at: "2026-08-29T09:40:11.224705Z"
---
.. _bash_completion:

# How to set up bash completion

When using bash as your shell, ``pytest`` can use argcomplete
(https://kislyuk.github.io/argcomplete/) for auto-completion.
For this ``argcomplete`` needs to be installed **and** enabled.

Install argcomplete using:

.. code-block:: bash

    sudo pip install 'argcomplete>=0.5.7'

For global activation of all argcomplete enabled python applications run:

.. code-block:: bash

    sudo activate-global-python-argcomplete

For permanent (but not global) ``pytest`` activation, use:

.. code-block:: bash

    register-python-argcomplete pytest >> ~/.bashrc

For one-time activation of argcomplete for ``pytest`` only, use:

.. code-block:: bash

    eval "$(register-python-argcomplete pytest)"