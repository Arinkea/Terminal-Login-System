from rich.console import Console
import time

console = Console()
console.clear()

users = {

    'никита': {
        'Позывной': 'miki',
        'Возраст': 29,
        'Рост': '185cm',
        'Собшения': "Вы В базе",
        'password': "111"
    },
    'оля': {
        'Позывной': 'fox',
        'Возраст': 27,
        'Рост': '165cm',
        'Собшения': "Вы В базе",
        'password': "222"
    },

    'леха': {
        'Позывной': 'могильшик',
        'Возраст': 41,
        'Рост': '191cm',
        'Собшения': "Вы В базе",
        'password': "333"
        },
        
}

name = console.input('[bold blue]Введите Имя для доступа к базе: [/]').strip().lower()
password = console.input('[bold blue]Введите Пороль для доступа к базе: [/]').strip()

if name in users and password == users[name]['password']:
    console.rule("[bold green]ДОСТУП РАЗРЕШЁН[/]")

    console.print(f"[bold yellow]{users[name]['Собшения']}[/]", justify=("center"))
    console.print(f"[bold yellow]Информация Вам скажут на постороение[/]", justify=("center"))

else:
    console.rule("[bold red]ДОСТУП ЗАПРЕШЁН[/bold red]", style="red")
    print()
    console.print('[bold red]ЧЕРЕЗ 10 СЕКУНД САМОУНИЧТОЖЕНИЯ УСТРОЙСТВА[/bold red]', justify="center")
    time.sleep(10)
    console.print('[bold red]System ERROR: Incorrect data was entered[/bold red]', justify="center")
    time.sleep(5)
    console.clear()
