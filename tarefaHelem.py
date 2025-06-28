print("O animal é mamífero? (s/n)")
resp = input()

if resp == 's':
    print("É quadrúpede? (s/n)")
    resp = input()
    if resp == 's':
        print("É carnívoro? (s/n)")
        resp = input()
        if resp == 's':
            print("O animal escolhido foi o leão.")
        else:
            print("É herbívoro? (s/n)")
            resp = input()
            if resp == 's':
                print("O animal escolhido foi o cavalo.")
    else:
        print("É bípede? (s/n)")
        resp = input()
        if resp == 's':
            print("É onívoro? (s/n)")
            resp = input()
            if resp == 's':
                print("O animal escolhido foi o homem.")
            else:
                print("É frutívoro? (s/n)")
                resp = input()
                if resp == 's':
                    print("O animal escolhido foi o macaco.")
        else:
            print("É voador? (s/n)")
            resp = input()
            if resp == 's':
                print("O animal escolhido foi o morcego.")
            else:
                print("É aquático? (s/n)")
                resp = input()
                if resp == 's':
                    print("O animal escolhido foi a baleia.")

else:
    print("O animal é ave? (s/n)")
    resp = input()
    if resp == 's':
        print("É não voadora? (s/n)")
        resp = input()
        if resp == 's':
            print("É tropical? (s/n)")
            resp = input()
            if resp == 's':
                print("O animal escolhido foi o avestruz.")
            else:
                print("É polar? (s/n)")
                resp = input()
                if resp == 's':
                    print("O animal escolhido foi o pinguim.")
        else:
            print("É nadadora? (s/n)")
            resp = input()
            if resp == 's':
                print("O animal escolhido foi o pato.")
            else:
                print("É de rapina? (s/n)")
                resp = input()
                if resp == 's':
                    print("O animal escolhido foi a águia.")

    else:
        print("O animal é réptil? (s/n)")
        resp = input()
        if resp == 's':
            print("Tem casco? (s/n)")
            resp = input()
            if resp == 's':
                print("O animal escolhido foi a tartaruga.")
            else:
                print("É carnívoro? (s/n)")
                resp = input()
                if resp == 's':
                    print("O animal escolhido foi o crocodilo.")
                else:
                    print("Não tem patas? (s/n)")
                    resp = input()
                    if resp == 's':
                        print("O animal escolhido foi a cobra.")
