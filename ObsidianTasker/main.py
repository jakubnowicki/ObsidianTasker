import click
from .config import get_task_file_path
from .add_task import add_task
from .dmenu import open_dmenu

@click.command()
@click.argument('action', type=click.Choice(['config', 'add', 'help']))
@click.argument('task', required=False)

# Add more arguments and options here
def main(action, task):
    if action == 'help' or action == None:
        click.echo(click.get_current_context().get_help())

    if action == 'config':
        file = get_task_file_path()
        click.echo(file)

    if action == 'add':
        if task is not None:
            add_task(task=task)
        else:
            task = open_dmenu()
            add_task(task=task)

if __name__ == '__main__':
    main()
