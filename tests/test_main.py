from unittest.mock import patch
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent / 'lego_cli'))

from lego_cli.main import LegoCLI


# Test to verify the analyze_lego_data method with a mock
@patch('matplotlib.pyplot.show')
@patch('lego_cli.main.analyze_by_theme')
def test_analyze_lego_data(mock_analyze, mock_show):
    cli = LegoCLI()
    cli.option.analyze_by_theme = True
    cli.option.csv_path = 'tests/Brickset-MySets-all.csv'
    cli.option.theme = 'Star Wars'
    cli.option.subtheme = 'Episode IV'
    cli.analyze_lego_data()
    mock_analyze.assert_called_once_with(
        'tests/Brickset-MySets-all.csv',
        'Star Wars',
        'Episode IV'
        )
