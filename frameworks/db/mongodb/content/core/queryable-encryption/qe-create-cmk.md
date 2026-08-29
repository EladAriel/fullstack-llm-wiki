---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/queryable-encryption/qe-create-cmk.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.781392Z"
---
**facet:** :name: programming_language
   :values: csharp, go, java, javascript/typescript, python, shell

**meta:** :keywords: code example, node.js, compass

.. _qe-create-cmk:

# Create a {+cmk-long+}

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

## Overview

In this guide, you will learn how to generate a {+cmk-long+} in your {+kms-long+} of choice. Generate a {+cmk-long+} before creating your {+qe+}-enabled application.

**tip:** Customer Master Keys

   To learn more about the {+cmk-long+}, see
   :ref:`qe-reference-keys-key-vaults`


## Before You Start

Complete the preceding tasks before continuing:

#. :ref:`Install a {+qe+} compatible driver and dependencies <qe-install>`

#. :ref:`Install and configure a {+qe+} library <qe-csfle-install-library>`


## Procedure

Select your key provider below.

.. composable-tutorial::
   :options: key-provider
   :defaults: aws

   .. selected-content::
      :selections: aws

      .. procedure::

         .. _qe-create-cmk-aws:

         .. step:: Create the {+cmk-long+}
      
            .. include:: /includes/queryable-encryption/tutorials/automatic/aws/cmk.rst

         .. _qe-create-aws-iam-user:

         .. step:: Create an AWS IAM User

            .. include:: /includes/queryable-encryption/tutorials/automatic/aws/user.rst

   .. selected-content::
      :selections: azure

      .. procedure::

         .. _qe-register-cmk-azure:
         
         .. step:: Register your Application with Azure

            .. include:: /includes/queryable-encryption/tutorials/automatic/azure/register.rst

         .. _qe-create-cmk-azure:

         .. step:: Create the {+cmk-long+}

            .. include:: /includes/queryable-encryption/tutorials/automatic/azure/cmk.rst

   .. selected-content::
      :selections: google

      .. procedure::

         .. step:: Register a {+gcp-abbr+} Service Account

            .. include:: /includes/queryable-encryption/tutorials/automatic/gcp/register.rst

         .. _qe-create-cmk-gcp:

         .. step:: Create a {+gcp-abbr+} {+cmk-long+}

            .. include:: /includes/queryable-encryption/tutorials/automatic/gcp/cmk.rst

   .. selected-content::
      :selections: kmip

      .. procedure::

         .. step:: Configure your {+kmip-kms-title+}

            .. include:: /includes/queryable-encryption/tutorials/automatic/kmip/configure.rst

         .. step:: Specify your Certificates

            .. _qe-kmip-tutorial-specify-your-certificates:

            .. include:: /includes/queryable-encryption/tutorials/automatic/kmip/certificates.rst

## Next Steps

After installing drivers and dependencies and creating a {+cmk-long+}, 
you can :ref:`create your {+qe+} enabled application <qe-create-application>`.
      