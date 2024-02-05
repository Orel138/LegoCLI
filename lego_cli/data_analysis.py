#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt

def analyze_by_theme(csv_path, theme_filter=None, subtheme_filter=None):
    """ Analyzes LEGO data by theme and subtheme. """
    lego_data = pd.read_csv(csv_path)
    
    # Grouping by Year, Theme, and Subtheme
    theme_counts_by_year = lego_data.groupby(['Year', 'Theme', 'Subtheme']).size().reset_index(name='Count')
    
    # Filtering by Theme and Subtheme if specified
    if theme_filter:
        theme_counts_by_year = theme_counts_by_year[theme_counts_by_year['Theme'] == theme_filter]
    if subtheme_filter:
        theme_counts_by_year = theme_counts_by_year[theme_counts_by_year['Subtheme'] == subtheme_filter]
    
    for (theme, subtheme), df in theme_counts_by_year.groupby(['Theme', 'Subtheme']):
        if df['Year'].nunique() > 1:  # Plot only if there's data for more than one year
            plt.figure(figsize=(10, 6))
            plt.plot(df['Year'], df['Count'], marker='o', linestyle='-')
            plt.title(f'Evolution of {theme} - {subtheme} over the years')
            plt.xlabel('Year')
            plt.ylabel('Number of Sets')
            plt.xticks(rotation=45)
            plt.grid(True)
            plt.tight_layout()  # Adjust layout to ensure everything fits without overlap
            plt.show()

