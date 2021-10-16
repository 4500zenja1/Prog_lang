#include <iostream>
#include "classes.h"

int Document::document_count = 0;
int Document::index = 0;
int Receipt::receipt_count = 0;
int Invoice::invoice_count = 0;
int Check::check_count = 0;
Document** Document::documents = nullptr;

int main() {
	// ������� ���������� �������� � ������ (����� �����������)
	Receipt doc1;
	Receipt doc2("1 ������ 2001 �.", "Vitruvium", "������� �.�.", "�������� �.�.", 846);

	Invoice doc3;
	Invoice doc4("29 ������� 2004 �.", "��������� � ��������", "�������������� ���������", "��������� �.�.", "7 ����� 2004 �.");

	Check doc5;
	Check doc6("15 �������� 2021 �.", "���������������", "���������� �.�.", "�������� �.�.", 500.39);

	// ����� ���������� �������� � ������ ���� ������ add()
	doc2.add();
	doc5.add();
	doc4.add();

	Document::show_list();
}