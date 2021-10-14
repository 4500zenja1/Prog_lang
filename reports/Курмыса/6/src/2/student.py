from pupil import Pupil

class Student(Pupil):
  count = 0
  __student_number = int()
  _course = int()
  _specialty = str()
  _university = str()

  def __init__(self, name='�������', age=0, town='�����_�������', course=0, specialty='�������������_�������', university='�����������_�������'):
    Student.count += 1
    self.__student_number = Student.count
    print('����� ������������ ������ Student No.', self.__student_number)
    super().__init__(name, age, town)
    self._course = int(course)
    self._specialty = specialty
    self._university = university
  
  def __del__(self):
    print('��������� ������ ������ Student No.', self.__student_number)
    super().__del__()

  def get_course(self):
    return self._course
  
  def get_specialty(self):
    return self._specialty
  
  def get_university(self):
    return self._university
  
  def set_course(self, course):
    self._course = course
  
  def set_specialty(self, specialty):
    self._specialty = specialty
  
  def set_university(self, university):
    self._university = university
  
  def read(self):
    try:
      self._name = input('������� ��� ��������: ')
      self._age = int(input('������� ������� ��������: '))
      self._town = input('������� ����� ��������: ')
      self._course = int(input('������� ���� ��������: '))
      self._specialty = input('������� ������������� ��������: ')
      self._university = input('������� ����������� ��������: ')
    except ValueError as e:
      print(e)
  
  def show(self):
    print(
      '���:', self._name, 
      '\n�������:', self._age, 
      '\n�����:', self._town, 
      '\n����:', self._course, 
      '\n�������������:', self._specialty, 
      '\n�����������:', self._university, end='\n\n')