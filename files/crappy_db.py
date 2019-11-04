import os

# file format:
# <student id>,<first name>,<last name>


def setup():
    if not os.path.isdir('data'):
        os.mkdir('data')
    os.chdir('data')


def insert_data():
    # insert
    records = [
        ['w000001', 'john', 'smith'],
        ['w001002', 'jane', 'doe'],
        ['w000003', 'jack', 'sprat']
    ]
    f = open('crappy_db.txt', 'w')
    for r in records:
        new_rec = f"{r[0]},{r[1]},{r[2]}\n"
        f.write(new_rec)
    f.close()


def select_data():
    with open('crappy_db.txt') as f:
        for line in f:
            # print(line.rstrip('\n'))
            fields = line.rstrip('\n').split(',')
            # where clause
            if fields[0].startswith('w000'):
                print(line)


def update_data():
    outfile = open('updated_db.txt', 'w')
    with open('crappy_db.txt') as infile:
        for line in infile:
            fields = line.rstrip('\n').split(',')
            # where
            if fields[1] == 'jack':
                fields[0] = 'w000002'
            new_rec = ','.join(fields) + '\n'
            outfile.write(new_rec)
    outfile.close()
    os.replace('updated_db.txt', 'crappy_db.txt')


def delete_data():
    outfile = open('updated_db.txt', 'w')
    with open('crappy_db.txt') as infile:
        for line in infile:
            fields = line.rstrip('\n').split(',')
            # where
            if fields[2] != 'smith':
                new_rec = ','.join(fields) + '\n'
                outfile.write(new_rec)
    outfile.close()
    os.replace('updated_db.txt', 'crappy_db.txt')



if __name__ == '__main__':
    setup()
    insert_data()
    select_data()
    update_data()
    delete_data()
