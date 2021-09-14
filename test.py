import click
import typer

def hi(name: str):
    print(f'hi {name}')

if __name__ == '__main__':
    typer.run(hi)
