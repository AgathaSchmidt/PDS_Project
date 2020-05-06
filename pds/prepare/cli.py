import click

from pds.prepare.info import *


@click.command()
@click.option('--column_info/--no-column_info', default=False, help='Get column information')
def main(column_info):
    if c_info:
        c_info(df)
    else:
        print('You do not do anything')


if __name__ == '__main__':
    main()
