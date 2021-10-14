from pupil import Pupil
from student import Student
from undergrad import Undergrad

if __name__ == "__main__":
  person1 = Pupil()
  person1.read()
  print('������ �� ������� ���������:')
  person1.show()
  person2 = Pupil('����', 13, '������')
  print('��� ������� ���������:', person2.get_name())
  print('����� ������� ���������:', person2.get_town())

  person3 = Student()
  person4 = Student('����', 18, '�����')
  person3.read()
  person4.set_specialty('��')
  person4.set_course(1)
  person4.set_university('���� ��. �������')
  print('������ �� �������� ���������:')
  person3.show()
  print('������ �� ��������� ���������:')
  person4.show()

  person5 = Undergrad()
  print('������ �� ������ ��������� (���������):')
  person5.show()
  person5.read()
  print('���� �������� ������� ��� ������ ���������:', person5.get_project_theme())
  print('��� �������� ������������ ������ ���������:', person5.get_director())
  print('������ �� ������ ��������� (��������):')
  person5.show()

  del person1, person2, person3, person4, person5