"""
Command Line Interface for SOLID Inspector.

This module provides the CLI interface for analyzing code and running tutorials.
"""

import click
import sys
from pathlib import Path


@click.group()
@click.version_option(version="0.1.0", prog_name="solid-inspector")
def cli():
    """
    🔍 SOLID Inspector - Analyze code quality based on SOLID design principles.
    
    This tool helps you analyze Python code for SOLID principle violations
    and provides educational tutorials to improve your code quality.
    """
    pass


@cli.command()
@click.argument('file_path', type=click.Path(exists=True))
@click.option('--output', '-o', help='Output file for the analysis report')
@click.option('--format', 'output_format', 
              type=click.Choice(['console', 'json', 'html']), 
              default='console',
              help='Output format for the analysis report')
def analyze(file_path, output, output_format):
    """
    Analyze a Python file for SOLID principle violations.
    
    FILE_PATH: Path to the Python file to analyze
    """
    click.echo(f"🔍 Analyzing {file_path}...")
    click.echo("⚠️  Analysis engine is under development.")
    click.echo("📚 In the meantime, check out our educational tutorials!")
    
    if output:
        click.echo(f"📄 Report will be saved to: {output}")
    
    click.echo(f"📊 Output format: {output_format}")


@cli.command()
@click.option('--notebook', '-n', help='Specific notebook to open')
def tutorial(notebook):
    """
    Launch the SOLID principles tutorial notebooks.
    """
    click.echo("📚 Launching SOLID principles tutorials...")
    
    if notebook:
        click.echo(f"📖 Opening specific notebook: {notebook}")
    else:
        click.echo("📖 Opening tutorial overview...")
    
    # For now, just show the available notebooks
    notebooks = [
        "00_SOLID_Principles_Overview.ipynb",
        "01_Single_Responsibility_Principle.ipynb", 
        "02_Open_Closed_Principle.ipynb",
        "03_Liskov_Substitution_Principle.ipynb",
        "04_Interface_Segregation_Principle.ipynb",
        "05_Dependency_Inversion_Principle.ipynb"
    ]
    
    click.echo("\n📋 Available tutorials:")
    for i, nb in enumerate(notebooks, 1):
        click.echo(f"  {i}. {nb}")
    
    click.echo("\n💡 To launch Jupyter notebooks, run:")
    click.echo("   jupyter notebook")


@cli.command()
def interactive():
    """
    Start interactive mode for code analysis.
    """
    click.echo("🚀 Starting SOLID Inspector interactive mode...")
    click.echo("⚠️  Interactive mode is under development.")
    click.echo("📚 Check out our tutorials to learn about SOLID principles!")


@cli.command()
def version():
    """
    Show version information.
    """
    click.echo("🔍 SOLID Inspector v0.1.0")
    click.echo("📚 Educational tutorials and analysis tools")
    click.echo("🌐 https://github.com/mdhabibi/solid-inspector")


if __name__ == '__main__':
    cli()
