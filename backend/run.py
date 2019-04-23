# -*- coding: utf-8 -*-
from __future__ import absolute_import

from app.demo import app
from app.demo.v1.api.implement import init_ml

if __name__ == '__main__':
    # for convenience, config env var here
    # for security and privacy consideration, remove these lines after
    import os

    # check env var
    assert ('GOOGLE_APPLICATION_CREDENTIALS' or 'PROJECT_ID' in os.environ)
    app.run(debug=True)
