harpies
=======

Helps you to generate link previews on the fly! Use ``harpies`` to get
the information of a webpage to generate a preview, then you know how
you want to style the preview with the information.

Installation
------------

You can install harpies using pip,

.. code:: sh

   pip install harpies

Requires Python 3 or above to run. If you have Python 2 installed too,
make sure to use the right pip.

Usage
-----

::

   >>> import harpies
   >>> data = harpies.preview_data("iamlizu.com")
   >>> print(data)
   {"title": "S M Mahmudul Hasan", "description": "WordPress security expert, creates technological contents in spare times, mostly found on tech forums, 
   part-time gamer, listens to electronic music.", "image": "https://iamlizu.com/wp-content/uploads/2019/10/iamlizu.com-cover.png", "url": "https://iamlizu.com/"}

Please look for logs at ‘~/Documents/harpies.log’