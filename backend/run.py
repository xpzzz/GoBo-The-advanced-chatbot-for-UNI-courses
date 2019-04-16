# -*- coding: utf-8 -*-
from __future__ import absolute_import

from app.demo import app
from app.demo.v1.api.implement import init_ml

if __name__ == '__main__':
    # for convenience, config env var here
    # for security and privacy consideration, remove these lines after
    import os

    # check env var
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'config/gobo-97e5e-38bad1ed63df.json'
    os.environ['PROJECT_ID'] = 'gobo-97e5e'
    assert ('GOOGLE_APPLICATION_CREDENTIALS' or 'PROJECT_ID' in os.environ)
    app.run(debug=True)
