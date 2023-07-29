Contributing
============

.. rst-class:: lead

    Thank you for considering contributing to this little library!

----

Support questions
-----------------

Please don't use the issue tracker for this. The issue tracker is a tool
to address bugs and feature requests. Use the our `GitHub Discussions`_
for questions about captcha.

.. _GitHub Discussions: https://github.com/lepture/captcha/discussions


Reporting issues
----------------

Include the following information in your post:

-   Describe what you expected to happen.
-   If possible, include a `minimal reproducible example`_ to help us
    identify the issue. This also helps check that the issue is not with
    your own code.
-   Describe what actually happened. Include the full traceback if there
    was an exception.
-   List your Python and ``captcha`` versions. If possible, check if this
    issue is already fixed in the latest releases or the latest code in
    the repository.

.. _minimal reproducible example: https://stackoverflow.com/help/minimal-reproducible-example


Submitting patches
------------------

If you found something you can improve, a "Pull Request" is always
welcoming. Here are something you need to notice before submitting
the PR.

If there is not an open issue for what you want to submit, prefer
opening one for discussion before working on a PR. You can work on any
issue that doesn't have an open PR linked to it or a maintainer assigned
to it. These show up in the sidebar. No need to ask if you can work on
an issue that interests you.

Include the following in your patch:

-   Include tests if your patch adds or changes code. Make sure the test
    fails without your patch.
-   Update any relevant docs pages and docstrings. Docs pages and
    docstrings should be wrapped at 72 characters.
-   Add an entry in ``CHANGES.rst``. Use the same style as other
    entries. Also include ``.. versionchanged::`` inline changelogs in
    relevant docstrings.

Running the tests
~~~~~~~~~~~~~~~~~

Run the basic test suite with pytest.

.. code-block:: text

    $ pytest


Updating the docs
~~~~~~~~~~~~~~~~~

When something has been changed, document them in the docs. You may need
to add a change log in the ``changelog.rst`` file.

Conventional Commits
~~~~~~~~~~~~~~~~~~~~

We are using `Conventional Commits <https://www.conventionalcommits.org/en/v1.0.0/>`_.
When you ``git commit`` some changes, please follow the "Conventional Commits" for the
commit message.
