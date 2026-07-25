---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/tutorials/automatic/aws/cmk.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

a. Log in to your [AWS Management Console](https://aws.amazon.com/console/)_.

#. Navigate to the [AWS KMS Console](https://aws.amazon.com/kms/)_.

#. Create your {+cmk-long+}

Create a new symmetric key by following the official AWS documentation on [Creating symmetric KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html#create-symmetric-cmk)_. The key you create is your {+cmk-long+}. Choose a name and description that helps you identify it; these fields do not affect the functionality or configuration of your {+cmk-abbr+}.

In the :guilabel:`Usage Permissions` step of the key generation process, apply the following default key policy that enables Identity and Access Management ({+aws-iam-abbr+}) policies to grant access to your {+cmk-long+}:
