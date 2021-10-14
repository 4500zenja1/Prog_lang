class Flat:
  count = 0 # ���������� ��������� �������� ������

  __address = str() # ����� ��������
  __area = int() # ������� ��������
  __floor = int() # ����

  # ����������� ��� ���������� (�� ���������)
  # ������������� ��������� ���� ���� ����������� � ������ + ����� ����� ����������� �������� �� ���������
  # def __init__(self):
  #   self.count += 1
  #   print('������ ����� ������. ���������� ��������� ��������:', self.count)
  
  def __init__(self, address = "", area = 0, floor = 0): # ����������� � �����������; ���� �� ���, �� �������� �� ���������
    try:
      Flat.count += 1
      print('\n������ ����� ������. ���������� ��������� ��������:', self.count, end='\n\n')
      self.__address = address
      self.__area = int(area)
      self.__floor = int(floor)
    except ValueError as e:
      print(e)
  
  def get_address(self):
    return self.__address
  
  def get_area(self):
    return self.__area
  
  def get_floor(self):
    return self.__floor
  
  def set_address(self, address):
    self.__address = address
  
  def set_area(self, area):
    self.__area = area
  
  def set_floor(self, floor):
    self.__floor = floor
  
  def read(self):
    try:
      self.__address= input('������� ����� ��������: ')
      self.__area = int(input('������� ������� �������� (� ��. �): '))
      self.__floor = input('������� ����� �����, �� ������� ����������� ��������: ')
    except ValueError as e:
      print(e)
  
  def show(self):
    print('\n' + '-' * 20)
    print('�����:', self.__address, '\n�������:', self.__area, '��. �\n����� �����:', self.__floor)
    print('-' * 20)

if __name__ == "__main__":
  grad1 = Flat() # ����� ������������ �� ���������
  grad1.read() # ������ ������ � ������ ����� �������
  grad1.show() # ����� ������ � �������

  grad2 = Flat("������, ��. ������������, �. 14, ��. 81", 129, 9) # ����� ������������ � �����������
  print('����� 2-�� ��������:', grad2.get_address())
  print('����� ����� 2-�� ��������:', grad2.get_floor()) # ��������� ������ ��� ������ ��������

  grad3 = Flat() # ����� ������������ �� ���������
  grad3.set_address("�����-���������, ��. ���������, �. 42, ��. 69")
  grad3.set_floor(4) # ������ ������ ��� ������ ��������
  print('������� 3-�� ��������:', grad3.get_area()) # �� �� ���������� ������� � ��������, �� �� ��������� ��� ����� 0, ��� ��� ������ �� �����
  grad3.show()