import pgzrun
from cfg import *
from clss import *




'''
locations.append(Locations( "id этой локации",
                            "название этой локации",
                            "1 описание этой локации",
                            "2 описание этой локации",
                            "3 описание этой локации",
                            "4 описание этой локации",
                            "5 описание этой локации",
                            "6 описание этой локации",
                            "7 описание этой локации",
                            "8 описание этой локации",
                            "9 описание этой локации",
                            "10 описание этой локации",
                            "11 описание этой локации",
                            "12 описание этой локации",
                            answer.get ("id первой кнопки"),
                            answer.get ("id второй кнопки"),
                            answer.get ("id третьей кнопки")
                             ))

locations.append(Locations( "",
                            "",
                            "",
                            "",
                            "",
                            "",
                            "",
                            "",
                            "",
                            "",
                            "",
                            "",
                            "",
                            "",
                            answer.get (""),
                            answer.get (""),
                            answer.get ("")
                             ))
'''




locations.append(Locations( "start",
                            "Комната со шкафом",
                            "Вы очнулись в неизвестном месте.",
                            "Тусклая лампочка на толстом проводе слабо освещает бетонную комнату.",
                            "В углу комнаты стоит шкаф, перед вами дверь.",
                            "Возле двери на стене большая красная кнопка, с надписью 'Не нажимать!'",
                            "",
                            "",
                            "",
                            "",
                            "",
                            "",
                            "",
                            "",
                            answer.get ("a.start.door.locked"),
                            answer.get ("a.start.closet"),
                            answer.get ("a.start.button")
                             ))

locations.append(Locations( "l.start.door.locked",
                            "Комната со шкафом",
                            "Дверь заперта.",
                            "",
                            "",
                            "",
                            "",
                            "",
                            "",
                            "",
                            "",
                            "",
                            "",
                            "",
                            answer.get ("a.start.door.locked"),
                            answer.get ("a.start.closet"),
                            answer.get ("a.start.button")
                             ))

locations.append(Locations( "l.start.closet.open",
                            "Комната со шкафом",
                            "Вы открыли шкаф и нашли в нём ключ!",
                            "",
                            "",
                            "",
                            "",
                            "",
                            "",
                            "",
                            "",
                            "",
                            "",
                            "",
                            answer.get ("a.start.door.open"),
                            answer.get ("a.start.button"),
                            answer.get ("a.start.closet.open.none")
                             ))

locations.append(Locations( "l.start.button.press",
                            "Комната со шкафом",
                            "Вы нажали на кнопку, после чего комната заполнилась ядовитым газом.",
                            "Вы умерли. Конец!",
                            "",
                            "",
                            "",
                            "",
                            "",
                            "",
                            "",
                            "",
                            "",
                            "",
                            answer.get ("end"),
                            answer.get ("replay"),
                            answer.get ("a.start.button.press.none")
                             ))

locations.append(Locations( "l.room2",
                            "Комната с кнопками",
                            "Вы открыли дверь и вошли в комнату.",
                            "Дверь за вами закрылась.",
                            "Перед вами три кнопки.",
                            "Какую следует нажать?",
                            "",
                            "",
                            "",
                            "",
                            "",
                            "",
                            "",
                            "",
                            answer.get ("a.room2.b1"),
                            answer.get ("a.room2.b2"),
                            answer.get ("a.room2.b3")
                             ))

locations.append(Locations( "l.room2.b1",
                            "Комната с кнопками",
                            "Вы нажали на кнопку 1.",
                            "Потолок сверху начал медленно опускаться.",
                            "Вы понимаете, что вот-вот умрете.",
                            "Спустя минуту потолок раздавил вас насмерть.",
                            "Вы умерли!",
                            "",
                            "",
                            "",
                            "",
                            "",
                            "",
                            "",
                            answer.get ("end"),
                            answer.get ("replay"),
                            answer.get ("a.room2.b1.none")
                             ))

locations.append(Locations( "l.room2.b2",
                            "Комната с кнопками",
                            "Вы нажали на кнопку 2.",
                            "Ничего не произошло.",
                            "",
                            "",
                            "",
                            "",
                            "",
                            "",
                            "",
                            "",
                            "",
                            "",
                            answer.get ("a.room2.b1"),
                            answer.get ("a.room2.b2"),
                            answer.get ("a.room2.b3")
                             ))

locations.append(Locations( "l.room2.b3",
                            "Комната с кнопками",
                            "Вы нажали на кнопку 3.",
                            "В стене открылись 2 потайные двери.",
                            "",
                            "",
                            "",
                            "",
                            "",
                            "",
                            "",
                            "",
                            "",
                            "",
                            answer.get ("a.room2.b3.door1"),
                            answer.get ("a.room2.b3.door2"),
                            answer.get ("a.room2.b3.stand")
                             ))

locations.append(Locations( "l.room2.b3.stand",
                            "Комната с кнопками",
                            "Вы решили остаться.",
                            "Внезапно выключился свет, в углу засветились красные глаза.",
                            "Через пару секунд вы мгновенно погибли!",
                            "",
                            "",
                            "",
                            "",
                            "",
                            "",
                            "",
                            "",
                            "",
                            answer.get ("end"),
                            answer.get ("replay"),
                            answer.get ("a.room2.b3.stand.none")
                             ))

locations.append(Locations( "l.room2.b3.door1",
                            "Темный корридор",
                            "Вы вошли в первую дверь.",
                            "Вы идете по коридору несколько часов.",
                            "Вы умерли от голода.",
                            "Игра окончена!",
                            "",
                            "",
                            "",
                            "",
                            "",
                            "",
                            "",
                            "",
                            answer.get ("end"),
                            answer.get ("replay"),
                            answer.get ("a.room2.b3.door1.none")
                             ))

locations.append(Locations( "l.corridor",
                            "Темный корридор",
                            "Вы вошли в темный узкий коридор.",
                            "Дверь за вами закрылась.",
                            "Вы продолжаете идти вперед, пока не видите на стене факел.",
                            "",
                            "",
                            "",
                            "",
                            "",
                            "",
                            "",
                            "",
                            "",
                            answer.get ("a.corridor.torch"),
                            answer.get ("a.corridor.go"),
                            answer.get ("a.corridor.none")
                             ))

locations.append(Locations( "l.corridor.torch",
                            "Корридор",
                            "Вы взяли факел.",
                            "Вы подняли голову вверх и увидели руку с длинными ногтями.",
                            "Она схватила вас за голову и быстро потянула вверх.",
                            "Вы умерли!",
                            "",
                            "",
                            "",
                            "",
                            "",
                            "",
                            "",
                            "",
                            answer.get ("end"),
                            answer.get ("replay"),
                            answer.get ("a.corridor.torch.none")
                             ))

locations.append(Locations( "l.corridor.exit",
                            "Корридор",
                            "Вы решили не брать факел и пойти дальше.",
                            "Вы шли несколько часов, пока не увидели свет в конце - выход.",
                            "",
                            "",
                            "",
                            "",
                            "",
                            "",
                            "",
                            "",
                            "",
                            "",
                            answer.get ("a.corridor.exit.run"),
                            answer.get ("a.corridor.exit.walk"),
                            answer.get ("a.corridor.exit.slow")
                             ))

locations.append(Locations( "l.corridor.exit.slow",
                            "Корридор",
                            "Вы решили замедлится, зачем спешить.",
                            "Внезапно выход чем-то завалило и свет опять пропал.",
                            "Спустя пару часов вы погибли от обезвоживания!",
                            "",
                            "",
                            "",
                            "",
                            "",
                            "",
                            "",
                            "",
                            "",
                            answer.get ("end"),
                            answer.get ("replay"),
                            answer.get ("a.corridor.exit.slow.none")
                             ))

locations.append(Locations( "l.corridor.exit.run",
                            "Корридор",
                            "Вы решили побежать, что-бы как можно скорее сбежать отсюда.",
                            "Но вы подскользнулись и разбили голову.",
                            "Игра окончена!",
                            "",
                            "",
                            "",
                            "",
                            "",
                            "",
                            "",
                            "",
                            "",
                            answer.get ("end"),
                            answer.get ("replay"),
                            answer.get ("a.corridor.exit.run.none")
                             ))

locations.append(Locations( "l.forest",
                            "Лес",
                            "Вы пошли к выходу, не изменяя своего темпа.",
                            "Вы вышли в густой лес.",
                            "Обернувшись, вы увидели, что вы вышли из пещеры.",
                            "Вы на свободе!",
                            "",
                            "Спасибо за прохождение демонстрационной игры.",
                            "Квесты я конечно делаю так себе, но это и не самое важное.",
                            "Вы можете изучить файлы игры и создать свой квест.",
                            "",
                            "",
                            "",
                            "",
                            answer.get ("a.forest"),
                            answer.get ("a.forest.none"),
                            answer.get ("a.forest.none")
                             ))
