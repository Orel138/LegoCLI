do not:
python ./lego_cli/main.py --help
python ./lego_cli/main.py --csv_path ./tests/Brickset-MySets-all.csv --analyze_by_theme --theme "Star Wars"
python ./lego_cli/main.py --csv_path ./tests/Brickset-MySets-all.csv --analyze_by_theme --theme "Star Wars" -verbose

do:
python -m lego_cli.main --csv_path ./tests/Brickset-MySets-all.csv --help