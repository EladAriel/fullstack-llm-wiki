---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/authenticate-a-user.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.591780Z"
---
.. _authentication-auth-as-user:

# Authenticate a User with Self-Managed Deployments

.. default-domain:: mongodb

**meta:** :keywords: on-prem
   :description: Authenticate users in self-managed MongoDB deployments using `mongosh` with username, password, and authentication database.

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

.. dismissible-skills-card::
   :skill: Secure MongoDB Self-Managed: AuthN and AuthZ
   :url: https://learn.mongodb.com/skills/?openTab=security

To authenticate as a user, you must provide a username, password, and the 
:option:`authentication database <mongosh --authenticationDatabase>` associated 
with that user.

**important:** It is not possible to switch between users in the same
   :binary:`~bin.mongosh` session. Authenticating as a different user
   means the session has the privileges of **both** authenticated
   users. To switch between users exit and relaunch
   :binary:`~bin.mongosh`.

Using :binary:`~bin.mongosh`, you can:

**tabs:** tabs:
      - id: cmdline
        name: Authenticate during Connection
        content: |
           Start :binary:`~bin.mongosh` with the :option:`-u
           \<username\> <mongosh -u>`, :option:`-p <mongosh -p>`, and the
           :option:`--authenticationDatabase \<database\> <mongosh
           --authenticationDatabase>` command line options:

           .. code-block:: bash

              mongosh --port 27017  --authenticationDatabase \
                  "admin" -u "myUserAdmin" -p

           Enter your password when prompted.

      - id: authafter
        name: Authenticate after Connection
        content: |

           Using :binary:`~bin.mongosh`, connect to the
           :binary:`~bin.mongod` or :binary:`~bin.mongos` instance:

           .. code-block:: bash

              mongosh --port 27017

           In :binary:`~bin.mongosh`, switch to the
           authentication database (in this case, ``admin``), and
           use the :method:`db.auth(\<username\>, \<pwd\>)
           <db.auth()>` method or the :dbcommand:`authenticate`
           command to authenticate against the 
           :option:`authentication database <mongosh --authenticationDatabase>`:

           .. code-block:: javascript

              use admin
              db.auth("myUserAdmin", passwordPrompt()) // or cleartext password

           .. tip::

              .. include:: /includes/extracts/mongosh-password-prompt.rst

           Enter the password when prompted.

For examples using a MongoDB driver, see the :driver:`driver documentation </>`.