import os
import pytest
import tempfile

import shop
@pytest.fixture
def app():
    db_fd, shop.app.config['DATABASE'] =tempfile.mkstemp()
    shop.app.testing = True

    yield shop.app.test_client()

    os.close(db_fd)
    os.unlink(shop.app.config['DATABASE'])
