import main

main.Spell.import_spells("Spells.csv")
ticket1 = main.Line("Jacky", "Bob")
print(main.Spell.all_spells_bst.get_min())
print(main.Spell.all_spells_bst.get_max())
print(main.Line.all_spells_qu.dequeue())
main.Line.all_spells_qu.traverse()

match1 = main.QuidditchMatch('2023-04-21', 'Slytherin')
match2 = main.QuidditchMatch('2023-03-11', 'Gryffindor')
match3 = main.QuidditchMatch('2023-02-01', 'Hufflepuff')

main.QuidditchMatch.upcoming_games.traverse()
main.QuidditchMatch.upcoming_games.dequeue()
main.uidditchMatch.upcoming_games.enqueue()
