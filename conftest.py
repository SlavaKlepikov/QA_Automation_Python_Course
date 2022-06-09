import pytest
import logging
from code_for_testing import Human

logger = logging.getLogger()
logger.setLevel('INFO')


@pytest.fixture
def human_object():
    logger.info(msg='\nFixture create Human object is started')
    human = Human(name="Maks", age=25, gender="female")
    yield human
    logger.info(msg='\nFixture create Human object is finished')
