#include <iostream>
#include "workshop.h"

using namespace std;

int main() {
	Workshop first; // ����������� ��� ����������
	Workshop second("Workshop", "Zubenko Mikhail", 5928); // ����������� � �����������
	Workshop third = first; // ����������� ������������ ������� �������
	Workshop group[3] = { Workshop(), Workshop("Second", "Belyaev", 7), first }; // ����������� ������, ������ ���� ��� ������������. ������������
	Workshop* dynamic_group; // ������������ ������ + ���������
	dynamic_group = new Workshop[2];
	dynamic_group[0].set("Steel", "Golubev", 19); // ���������� � ������ ����� ������
	dynamic_group[1].setAmount(5); // ��������� � ������ �� �����������
	dynamic_group[1].setBoss("Dolubev");
	dynamic_group[1].setName("Piping");
	void (Workshop:: *secret)(); // ��������� �� �������-����������
	secret = &Workshop::secret;

	cout << "The name of workshop No. 1 is " << first.getName() << endl;
	first.setName("Concrete"); // ��������� �������� ����
	cout << "The name of workshop No. 1 is " << first.getName() << endl;

	cout << "The boss of workshop No. 2 is " << second.getBoss() << endl;
	second.setBoss("Kamyshov"); // ��������� ����������
	cout << "The boss of workshop No. 2 is " << second.getBoss() << endl;

	cout << "The amount of workers in workshop No. 3 is " << third.getAmount() << endl;
	third.setAmount(16); // ��������� ���������� �������
	cout << "The amount of workers in workshop No. 3 is " << third.getAmount() << endl;

	group[0].show();
	group[0].set("Name", "Boss", 100); // ��������� ����� ����� set
	group[0].show();

	dynamic_group[1].show();
	(dynamic_group[1].*secret)(); // ������ ������� :)
	dynamic_group[1].show();

	system("pause");

	delete[] dynamic_group; // ������� ������������ ������ dynamic_group
}