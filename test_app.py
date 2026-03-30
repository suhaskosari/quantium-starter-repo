import pytest
import chromedriver_autoinstaller
from app import app

chromedriver_autoinstaller.install()

@pytest.fixture
def dash_duo(dash_duo):
    dash_duo.start_server(app)
    return dash_duo

def test_header_present(dash_duo):
    header = dash_duo.find_element("h1")
    assert header is not None
    assert "Pink Morsel Sales Visualiser" in header.text

def test_chart_present(dash_duo):
    chart = dash_duo.find_element("#sales-chart")
    assert chart is not None

def test_region_picker_present(dash_duo):
    region_picker = dash_duo.find_element("#region-filter")
    assert region_picker is not None