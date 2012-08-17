from collections import defaultdict
import thread, time

def div(a,b):
    n = float(a)/b
    intn = int(n)
    return intn if intn == n else -1

OPS = {"+": lambda a,b: a+b,
       "-": lambda a,b: a-b,
       "*": lambda a,b: a*b,
       "/": div}
last_len = defaultdict(lambda: 1000)
solutions = defaultdict(list)

def solve(target, all_numbers, numbers=None, operations=[]):
    if not numbers:
        numbers = all_numbers
    for i, a in enumerate(numbers):
        if a<=0: continue
        for j, b in enumerate(numbers):
            if i == j or b<=0: continue
            for op, func in OPS.iteritems():
                n = func(a, b)
                if n<=0: continue
                left_numbers = list(numbers)
                left_numbers.remove(a)
                left_numbers.remove(b)
                left_numbers.append(n)
                added_operations = operations+[(a,op,b,n)]
                if n == target:
                    add(target, all_numbers, added_operations)
                else:
                    solve(target, all_numbers, left_numbers, added_operations)

def add(target, all_numbers, operations):
    global last_len
    if len(operations) < last_len[target, all_numbers]:
        show(target, all_numbers, operations)
        last_len[target, all_numbers] = len(operations)
    solutions[target, all_numbers].append(tuple(operations))

def show(target, all_numbers, operations):
    all_numbers = tuple(all_numbers)
    len_ops = len(operations)
    print _('SHOW') % locals()
    for (a,op,b,n) in operations:
        print a, op, b, '=', n
    print '*'*10

def shortest(target, all_numbers):
    s = tuple(solutions[target, all_numbers])
    print _('SHORTEST')
    if len(s) == 0:
        print _('NO SOLUTION')
        return
    show(target, all_numbers, sorted(reversed(s), key=len)[0])

def test():
    puzzles = [(468, (1,6,6,7,2,3))]

    for p in puzzles:
        solve(*p)
        shortest(*p)

def play():
    global started
    all_numbers = []
    print '*'*20
    while True:
        try:
            n = input(_("NEXT NUMBER"))
        except KeyboardInterrupt:
            return False
        except:
            all_numbers = tuple(all_numbers)
            if len(all_numbers) == 0:
                return False
            v = input(_("TARGET"))
            try:
                start = time.time()
                solve(v, all_numbers)
                end = time.time()
                shortest(v, all_numbers)
                s = end-start
                m = int(s/60)
                s = int(s-m*60)
                duration = '%sm%ss' % (m, s)
                count = len(solutions[v, all_numbers])
                print _('TOOK') % locals()
            except KeyboardInterrupt:
                pass
            return True
        else:
            all_numbers.append(n)
    return True

messages = {'fr': {'NEXT NUMBER': 'Numero suivant (laisser vide si complet)? ',
                   'TARGET': 'Compte? ',
                   'NO SOLUTION': 'Pas de solution!',
                   'SHORTEST': 'Recherche de la plus courte solution en cours...',
                   'SHOW': 'Compte %(target)s, avec %(all_numbers)s en %(len_ops)s etapes:',
                   'TOOK': 'Trouve %(count)s solutions en %(duration)s.',
                   'HELLO': 'Salut.',
                   'GOODBYE': 'Au revoir.'},
            
            'en': {'NEXT NUMBER': 'Next number (Leave empty if full)? ',
                   'TARGET': 'Target number? ',
                   'NO SOLUTION': 'No solution!',
                   'SHORTEST': 'Finding shortest...',
                   'SHOW': 'Target %(target)s, with %(all_numbers)s in %(len_ops)s steps:',
                   'TOOK': 'Took %(duration)s to find %(count)s solutions.',
                   'HELLO': 'Hello.',
                   'GOODBYE': 'Goodbye.'},
            }
def _(msg):
    global messages, lang
    return messages[lang][msg]

if __name__ == "__main__":
    lang = raw_input('fr/en?')
    if lang not in messages:
        lang = 'en'
    print _('HELLO')
    while play():
        pass
    print _('GOODBYE')
