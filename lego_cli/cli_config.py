# cli_config.py

# Global options for the LEGO CLI
OPTIONS = {
    "Configurations": {
        "verbose": {
            "default": False,
            "help": "more logs",
            "alias": ['-v'],
            "argparse": {"action": "store_true"}
        },
    },
    "General": {
        "csv_path": {
            "default": None,
            "help": "Path to the CSV file containing the LEGO collection",
            "argparse": {"required": True, "type": str}
        },
        "analyze_by_theme": {
            "default": False,
            "help": "Analyze collection by theme",
            "argparse": {"action": "store_true"}
        },
        "theme": {
            "default": None,
            "help": "Specify a LEGO theme to analyze",
            "alias": ['-t'],
            "argparse": {"type": str}
        },
        "subtheme": {
            "default": None,
            "help": "Specify a LEGO subtheme to analyze",
            "alias": ['-st'],
            "argparse": {"type": str}
        },
        "minifig": {
            "default": None,
            "help": "Specify the number of minifigs",
            "alias": ['-m'],
            "argparse": {"type": str}
        },
        # Other global options here
    },
    # Other option groups here
}
