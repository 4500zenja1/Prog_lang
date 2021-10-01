import os, csv

def task_1():
    print('� ����� "files" �������������', len(os.listdir('files/')), '����(�/��).')

def output_table(table):
    print('\n������ ���������:')
    print("{0:4}{1:25}{2:10}{3:10}".format("�", "���", "�������", "������"))
    for row in table:
        print("{0:4}{1:25}{2:10}{3:10}".format(row[0], row[1], row[2], row[3]))

def task_2():
    f = open("files/students.csv", "r+")
    csv_f = csv.reader(f)
    students = []
    i = 0
    for row in csv_f:
        if i > 0:
            students.append(row)
        i += 1
    students.sort(key=lambda x: int(x[2]))
    output_table(students)
    choice = input('\n������� ��������� ������� ��������� �������� �� 1? [y/yes/��/1 - ��, ����� - ���]\n').lower()
    if choice in ['y', 'yes', '��', '1']:
        while True:
            N = input('�������� ���� �� �����: ')
            for i in range(len(students)):
                if students[i][3] == N:
                    students[i][2] = str(int(students[i][2]) - 1)
            choice = input('\n������� ���������� ���������� �������? [y/yes/��/1 - ��, ����� - ���]\n').lower()
            if choice not in ['y', 'yes', '��', '1']:
                break
        output_table(students)
        choice = input('\n������� ��������� ������ �����? [y/yes/��/1 - ��, ����� - ���]\n').lower()
        if choice in ['y', 'yes', '��', '1']:
            f.seek(0)
            f.truncate()
            writer = csv.writer(f)
            writer.writerow(["�", "���", "�������", "������"])
            students.sort(key=lambda x: int(x[0]))
            for student in students:
                writer.writerow(student)
            print('\n���� ������� �����������!')
    f.close()

def task_3():
    with open("files/task_3.csv", "r+") as f:
      option = int(input('�������� ���� �� ������������ ������� ���� ������� 0, ����� ����� �� �������:\n1 - ������ � ����;\n2 - ������ �� �����\n'))
      if option == 0:
        print('\n������������ ����� �� �������...')
      elif option == 1:
        writer = csv.writer(f)
        while True:
          s = input("������� ������ ��� ����� ����� ������ � ���� ������ ���� Enter ��� ���������� ������ �������: ").split()
          if s:
            writer.writerow(s)
          else:
            break
      elif option == 2:
        csv_f = csv.reader(f)
        for row in csv_f:
          print(','.join(row))
      else:
        print('������������ ������� ��������!')


print('������������ ������ �5:\n�������� ������� Python')
while True:
  N = int(input('\n������� ����� ������� �� 1 �� 3 ���� 0, ���� �� ������ ����� �� ���������:\n1 - ���������� ���������� ������ � ����� files;\n2 - ������ � ������������� csv-�������;\n3 - ������ � ����������������� csv-�������\n'))
  if N == 0:
    print('\n������������ ����� �� ���������...\n')
    break
  elif N == 1:
    task_1()
  elif N == 2:
    task_2()
  elif N == 3:
    task_3()
  else:
    print('\n������������ ��������!\n')