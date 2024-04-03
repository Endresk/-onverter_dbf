import dbf

table = dbf.Table('STREET.dbf', codepage='cp866')
table.open()

print('Сколько нужно файлов:')
x = int(input())

count = 0
list_ = []

for rec in table:
    count += 1
    row_tuple = (f"{rec['NAME']}",
                 f"{rec['SOCR']}",
                 f"{rec['CODE']}",
                 f"{rec['INDEX']}",
                 f"{rec['GNINMB']}",
                 f"{rec['UNO']}",
                 f"{rec['OCATD']}")
    list_.append(row_tuple)

record_count = len(table)
part_ = int(record_count / x)

for i in range(0, x):

    table_1 = table.new(f"STREET_{i + 1}.dbf", codepage='cp866')
    table_1.open(mode=dbf.READ_WRITE)

    for j in range(i * part_, (i + 1) * part_):
        table_1.append(list_[j])
    table_1.close()

print("Все успешно!!! Файлы готовы!")

table.close()
