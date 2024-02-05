#!/usr/bin/env python3

# main.py
from cli_config import OPTIONS
from data_analysis import analyze_by_theme
import argparse
import sys


class LegoCLI:
    def __init__(self, **options):
        # Initialize an error code. Default is 0, indicating no error.
        self.err = 0

        # Create a Namespace object from the passed options.
        # This object will store command line arguments.
        self.option = argparse.Namespace(**options)

        # Create another Namespace object to store
        # additional information about options.
        self.info = argparse.Namespace()

        # Variable to store the script name (argv[0])
        # once parse_argv is called. Initially None.
        self.argv0 = None

        # Create an ArgumentParser object for parsing command line arguments.
        # Set a description for the parser.
        self.parser = argparse.ArgumentParser(
            description='LEGO Collection Analyzer')

        # A dictionary to hold argument groups
        # for organizing command line options.
        self.group = {}

        # Define the options for the command line interface
        # based on the OPTIONS dictionary.
        self.define_options(OPTIONS)

    def analyse_command(self, argv):
        """
        Perform analysis actions based on the command line arguments.

        Args:
        argv (list): The list of command line arguments.

        Returns:
        int: The status code after performing the analysis.
            0 indicates success, and any positive value indicates an error.
        """
        return self.parse_argv(argv).analyze_lego_data().status()

        # self.parse_argv(argv)
        # Parse the command line arguments and update
        # the options and state of the CLI.
        # `parse_argv` returns self (the LegoCLI instance),
        # allowing for method chaining.

        # .analyze_lego_data()
        # Perform the data analysis based on the parsed arguments.
        # `analyze_lego_data` is expected to carry out the analysis
        # and may modify the state of the CLI.

        # .status()
        # Return the current status of the CLI (error code).
        # A status of 0 typically indicates success,
        # and any positive value indicates an error.

    def define_options(self, options):
        """Define command line options based on a provided dictionary structure
        This method iterates through a nested dictionary of options,
        groups them, and adds them to an argparse.ArgumentParser instance
        for command line parsing.
        """
        for group, group_options in options.items():
            # Check if the option group already exists in the parser.
            # If not, create it.
            if group not in self.group:
                self.group[group] = self.parser.add_argument_group(group)

            # Iterate over each option in the group.
            for key, info in group_options.items():
                # Store the option information in the 'info' namespace.
                setattr(self.info, key, info)

                # If the option does not have
                # specific argparse-related settings,
                # skip further processing.
                if 'argparse' not in info:
                    continue

                # Extract the argparse-specific settings for this option.
                argument = info['argparse']

                # Determine the attribute name for this option.
                # Use the 'dest' field from argparse settings if available,
                # otherwise use the option key.
                attribute = argument.get('dest', key)

                # Set the default value for the option
                # in the 'option' namespace if it's not already set.
                if attribute not in self.option:
                    setattr(self.option, attribute, info['default'])

                # Prepare the command line argument names.
                # This includes the primary name and any aliases.
                # Replace underscores in the option name with
                # hyphens for command line convention.
                names = ['--' + key]
                if '_' in key:
                    names.append('--' + key.replace('_', '-'))

                # Add any aliases for the option
                # as specified in the configuration.
                if 'alias' in info:
                    names += info['alias']

                # Add the argument to the argparse group with its settings.
                self.group[group].add_argument(
                    *names,
                    help=info['help'],
                    default=getattr(self.option, attribute),
                    **argument)

        # Return self to allow method chaining.
        return self

    def status(self):
        """Return the current error code."""
        return self.err

    def parse_argv(self, argv):
        """Handle command line options."""
        self.argv0 = argv[0]
        self.parser.parse_args(argv[1:], namespace=self.option)
        return self

    def log(self, *args):
        """Optionally log a message to stderr."""
        if self.option.verbose:
            print(*args, file=sys.stderr)

    def analyze_by_theme(self, csv_path, theme, subtheme):
        analyze_by_theme(csv_path, theme, subtheme)

    def analyze_lego_data(self):
        """Perform analysis according to self.option."""
        self.log('self :', self)
        self.log('self.group :', self.group)

        if self.option.analyze_by_theme:
            self.analyze_by_theme(
                self.option.csv_path, self.option.theme, self.option.subtheme)

        print("self.option :", self.option)
        return self


if __name__ == "__main__":
    sys.exit(LegoCLI().analyse_command(sys.argv))
