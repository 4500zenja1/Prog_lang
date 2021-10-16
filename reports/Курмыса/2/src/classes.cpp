#include <iostream>
#include <cstring>
#include "classes.h"

using namespace std;

// ����������� �� ��������� ��� ������ Document
Document::Document() {
	date = "1 ������ 1970";
	organisation = "Feel Good Inc.";
	add();
	cout << "������ ������ ������ Document ����� " << ++document_count << " ����� ����������� �� ���������.\n";
}

// ����������� � ����������� ��� ������ Document
Document::Document(string date, string organisation) :
	date(date), organisation(organisation) {
	add();
	cout << "������ ������ ������ Document ����� " << ++document_count << " ����� ����������� � �����������.\n";
}

// ���������� ��� ������ Document
Document::~Document() {
	del();
	cout << "��������� ������ ������ Document ����� " << document_count-- << ".\n";
}

// ���������� ������ �������� � ������ (��� ������������ ��� ����� ������)
void
Document::add() {
	Document** temp = documents;
	documents = new Document * [index + 1];
	for (int i = 0; i < index; i++) documents[i] = temp[i];
	documents[index] = this;
	index++;
}

// �������� ���������� �������� �� ������ (��� �����������)
void
Document::del() {
	Document** temp = documents;
	documents = new Document * [index];
	for (int i = 0; i < index - 1; i++) documents[i] = temp[i];
	index--;
}

// ����� ������ ��������� ����������
void
Document::show_list() {
	cout << "\n������ ���� ����������:\n";
	for (int i = 0; i < index; i++) documents[i]->show_item();
}

// ����������� �� ��������� ��� ������ Receipt
Receipt::Receipt() :
	Document("1 ������ 1970 �.", "Feel Good Inc.") {
	sender = "������ �.�.";
	receiver = "������� �.�.";
	cost = 150;
	cout << "������ ������ ������ Receipt ����� " << ++receipt_count << " ����� ����������� �� ���������.\n";
}

// ����������� � ����������� ��� ������ Receipt
Receipt::Receipt(string date, string organisation, string sender, string receiver, int cost) :
	Document(date, organisation), sender(sender), receiver(receiver), cost(cost) {
	cout << "������ ������ ������ Receipt ����� " << ++receipt_count << " ����� ����������� � �����������.\n";
}

// ���������� ��� ������ Receipt
Receipt::~Receipt() {
	cout << "��������� ������ ������ Receipt ����� " << receipt_count-- << ".\n";
}

// ����� ���������� ��� ������� ������ Receipt
void
Receipt::show_item() {
	cout << "���������:" << endl;
	cout << "����: " << this->date << endl;
	cout << "�����������: " << this->organisation << endl;
	cout << "�����������: " << this->sender << endl;
	cout << "����������: " << this->receiver << endl;
	cout << "���������: " << this->cost << endl << endl;
}

// ����������� �� ��������� ��� ������ Invoice
Invoice::Invoice() :
	Document("1 ������ 1970 �.", "Feel Good Inc.") {
	goods = "����, ��������, ����, �������� ���, ������";
	provider = "������� �.�.";
	date_of_delivery = "8 �������� 2008 �.";
	cout << "������ ������ ������ Invoice ����� " << ++invoice_count << " ����� ����������� �� ���������.\n";
}

// ����������� � ����������� ��� ������ Invoice
Invoice::Invoice(string date, string organisation, string goods, string provider, string date_of_delivery) :
	Document(date, organisation), goods(goods), provider(provider), date_of_delivery(date_of_delivery) {
	cout << "������ ������ ������ Invoice ����� " << ++invoice_count << " ����� ����������� � �����������.\n";
}

// ���������� ��� ������ Invoice
Invoice::~Invoice() {
	cout << "��������� ������ ������ Invoice ����� " << invoice_count-- << ".\n";
}

// ����� ���������� ��� ������� ������ Invoice
void
Invoice::show_item() {
	cout << "���������:" << endl;
	cout << "����: " << this->date << endl;
	cout << "�����������: " << this->organisation << endl;
	cout << "������: " << this->goods << endl;
	cout << "���������: " << this->provider << endl;
	cout << "���� ��������: " << this->date_of_delivery << endl << endl;
}

// ����������� �� ��������� ��� ������ Check
Check::Check() :
	Document("1 ������ 1970 �.", "Feel Good Inc.") {
	payee = "��������� �.�.";
	drawer = "���������� �.�.";
	amount = 288.20;
	cout << "������ ������ ������ Check ����� " << ++check_count << " ����� ����������� �� ���������.\n";
}

// ����������� � ����������� ��� ������ Check
Check::Check(string date, string organisation, string payee, string drawer, double amount) :
	Document(date, organisation), payee(payee), drawer(drawer), amount(amount) {
	cout << "������ ������ ������ Check ����� " << ++check_count << " ����� ����������� � �����������.\n";
}

// ���������� ��� ������ Check
Check::~Check() {
	cout << "��������� ������ ������ Check ����� " << check_count-- << ".\n";
}

// ����� ���������� ��� ������� ������ Check
void
Check::show_item() {
	cout << "���:" << endl;
	cout << "����: " << this->date << endl;
	cout << "�����������: " << this->organisation << endl;
	cout << "������������: " << this->payee << endl;
	cout << "����������: " << this->drawer << endl;
	cout << "����� (� ���. ���.): " << this->amount << endl << endl;
}