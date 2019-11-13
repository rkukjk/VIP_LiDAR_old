import csv


if __name__ == '__main__':

    csv_file = open('UTMNew.csv', 'r')
    reader = csv.reader(csv_file)

    txt_file = open('output_2.txt', 'w')

    row_num = 0
    for row in reader:
        if row_num != 0:
            line = row[0] + ' ' + row[1] + ' ' + row[2] + ' ' + row[3] + ' ' + row[4] + ' ' + row[5] + ' ' + row[6] + ' ' + row[7] + ' ' + row[8] + ' ' + row[9] + '\n'
            txt_file.write(line)
        row_num += 1

    csv_file.close()
    txt_file.close()
