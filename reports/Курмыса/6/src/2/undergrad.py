from student import Student

class Undergrad(Student):
  count = 0
  __undergrad_number = 0
  _project_theme = str() # ���� �������
  _director = str() # ������� ������������

  def __init__(self, name='����������', age=0, town='�����_����������', course=0, specialty='�������������_����������', university='�����������_����������', project_theme='�����������_����������', director='�������_����������'):
    Undergrad.count += 1
    self.__undergrad_number = Undergrad.count
    print('����� ������������ ������ Undergrad No.', self.__undergrad_number)
    super(Undergrad, self).__init__(name, age, town, course, specialty, university)
    self._project_theme = project_theme
    self._director = director
  
  def __del__(self):
    print('��������� ������ ������ Undergrad No.', self.__undergrad_number)
    super().__del__()
  
  def get_project_theme(self):
    return self._project_theme
  
  def get_director(self):
    return self._director 
  
  def set_project_theme(self, project_theme):
    self._project_theme = project_theme
  
  def set_director(self, director):
    self._director = director
  
  def read(self):
    try:
      self._name = input('������� ��� �����������: ')
      self._age = int(input('������� ������� �����������: '))
      self._town = input('������� ����� �����������: ')
      self._course = int(input('������� ���� �����������: '))
      self._specialty = input('������� ������������� �����������: ')
      self._university = input('������� ����������� �����������: ')
      self._project_theme = input('������� ���� �������� �������: ')
      self._director = input('������� ��� �������� ������������: ')
    except ValueError as e:
      print(e)
  
  def show(self):
    print(
      '���:', self._name, 
      '\n�������:', self._age,
       '\n�����:', self._town, 
       '\n����:', self._course,
        '\n�������������:', self._specialty,
         '\n�����������:', self._university, 
         '\n���� �������:', self._project_theme,
          '\n��� �������� ������������:', self._director, end='\n\n')