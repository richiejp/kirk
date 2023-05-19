"""
Unittests for host SUT implementations.
"""
import pytest
from kirk.host import HostSUT
from kirk.tests.sut import _TestSUT
from kirk.tests.sut import Printer


pytestmark = pytest.mark.asyncio


@pytest.fixture
async def sut():
    sut = HostSUT()
    sut.setup()

    yield sut

    if await sut.is_running:
        await sut.stop()


class TestHostSUT(_TestSUT):
    """
    Test HostSUT implementation.
    """

    @pytest.fixture
    def sut_stop_sleep(self, request):
        """
        Host SUT test doesn't require time sleep in `test_stop_communicate`.
        """
        return request.param * 0

    async def test_fetch_file_stop(self):
        pytest.skip(reason="Coroutines don't support I/O file handling")
