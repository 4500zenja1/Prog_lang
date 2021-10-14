class Pupil:
  count = 0
  __pupil_number = int()
  _name = str()
  _age = int()
  _town = str()

  def __init__(self, name='��������', age=0, town='�����_��������'):
    Pupil.count += 1
    self.__pupil_number = Pupil.count
    print('����� ������������ ������ Pupil No.', self.__pupil_number)
    self._name = name
    self._age = int(age)
    self._town = town
  
  def __del__(self):
    print('��������� ������ ������ Pupil No.', self.__pupil_number)
  
  def get_name(self):
    return self._name
  
  def get_age(self):
    return self._age
  
  def get_town(self):
    return self._town
  
  def set_name(self, name):
    self._name = name
  
  def set_age(self, age):
    self._age = age
  
  def set_town(self, town):
    self._town = town

  def read(self):
    try:
      self._name = input('������� ��� ���������: ')
      self._age = int(input('������� ������� ���������: '))
      self._town = input('������� ����� ���������: ')
    except ValueError as e:
      print(e)
  
  def show(self):
    print('���:', self._name, '\n�������:', self._age, '\n�����:', self._town, end='\n\n')