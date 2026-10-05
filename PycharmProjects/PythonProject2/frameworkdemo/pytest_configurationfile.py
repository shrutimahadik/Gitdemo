from builtins import \
   function  #got this error    C:\Users\GNESH\PycharmProjects\PythonProject2\frameworkdemo\test_newe2e.py:22: PytestUnknownMarkWarning: Unknown pytest.mark.smoke - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/stable/how-to/mark.html

import pytest
import smoke

#type below
[pytest]
asyncio_default_fixure_loop_scope=function
markers= smoke
