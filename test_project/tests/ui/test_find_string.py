import pytest
from test_project.pages.ContextMenuPage import ContextMenuPage


@pytest.mark.usefixtures('get_driver')
class TestFindString:

    @pytest.mark.parametrize('text_to_find', [
        pytest.param('the-internet'),
        pytest.param('Alibaba', marks=pytest.mark.xfail) 
    ])
    def test_find_text(self, text_to_find):
        cmp = ContextMenuPage(self.driver)
        cmp.open_page()
        assert text_to_find in cmp.get_page_source()
