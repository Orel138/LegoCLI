#!/usr/bin/env python3

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
        "minifigs": {
            "default": None,
            "help": "Specify the number of minifigs",
            "alias": ['-m'],
            "argparse": {"action": "store_true"}
        },
        "pieces": {
            "default": None,
            "help": "Specify the number of pieces",
            "alias": ['-p'],
            "argparse": {"action": "store_true"}
        },
        # Other global options here
    },
    "Specifier": {
        "id": {
            "default": None,
            "help": "Specify the ID of the set",
            "alias": ['-i'],
            "argparse": {"type": str}
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
        "year": {
            "default": None,
            "help": "Specify a year",
            "alias": ['-y'],
            "argparse": {"type": str}
        },
    }
    # Other option groups here
}
