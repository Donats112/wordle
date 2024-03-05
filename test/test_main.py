from ..main import check_guess, print_word

def test_get_guess(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "magic")
    guess = input("Guess the word with 5 letters: ")
    assert guess == "magic"

    monkeypatch.setattr('builtins.input', lambda _: "people")
    guess = input("Guess the word with 6 letters: ")
    assert guess == "people"

    monkeypatch.setattr('builtins.input', lambda _: "contact")
    guess = input("Guess the word with 7 letters: ")
    assert guess == "contact"

    monkeypatch.setattr('builtins.input', lambda _: "internet")
    guess = input("Guess the word with 8 letters: ")
    assert guess == "internet"

    monkeypatch.setattr('builtins.input', lambda _: "balls")
    guess = input("Guess the word with 5 letters: ")
    assert guess == "balls"


def test_check_guess():
    assert check_guess("crane", "crane") == "GGGGG"
    assert check_guess("cranl", "crane") == "GGGGR"
    assert check_guess("ccane", "crane") == "GYGGG"
    assert check_guess("qqqqqs", "cranes") == "RRRRRG"
    assert check_guess("earcn", "crane") == "YYYYY"

def test_print_word():
    assert print_word("GGGGG", "crane") == "[green]c[/green][green]r[/green][green]a[/green][green]n[/green][green]e[/green]"
    assert print_word("RRRRR", "crane") == "[red]c[/red][red]r[/red][red]a[/red][red]n[/red][red]e[/red]"
    assert print_word("YYYYY", "crane") == "[yellow]c[/yellow][yellow]r[/yellow][yellow]a[/yellow][yellow]n[/yellow][yellow]e[/yellow]"
    assert print_word("GGGGGGGG", "internet") == "[green]i[/green][green]n[/green][green]t[/green][green]e[/green][green]r[/green][green]n[/green][green]e[/green][green]t[/green]"
    assert print_word("GRYGRY", "system") == "[green]s[/green][red]y[/red][yellow]s[/yellow][green]t[/green][red]e[/red][yellow]m[/yellow]"