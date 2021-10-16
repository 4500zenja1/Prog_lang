#ifndef CLASSES_H
#define CLASSES_H

using namespace std;

class Document { // ����� ��������
public:
    Document();
    Document(string, string);
    virtual ~Document(); // ��� ��� ���� ����������� �������, �� � ���������� ������ ���� �����������
    virtual void show_item() = 0; // ������ ����������� ������� ��� �������� �������
    void add(); // ������� ���������� ��������� � ������
    void del(); // �������� ��������� �� ������ (��� �����������)
    static void show_list(); // ��� ������ ������ ���������
protected:
    string date; // ���� ��������
    string organisation; // �����������, ��������� � ���������
    static int index; // ���������� ����� ��������� � ������
    static int document_count; // ����������� ������� - ���-�� ����������
    static Document** documents; // ������ ����������
};

class Receipt : public Document { // ����� ���������
public:
    Receipt();
    Receipt(string, string, string, string, int);
    ~Receipt();
    void show_item() override; // �������������� ��-������� �� ������������� � �������� �����
protected:
    string sender; // ����������� ����� ��� ���� ���������
    string receiver; // ���������� ����� ��� ���� ���������
    int cost; // ��������� ����� ��� ���� ���������
    static int receipt_count; // ���-�� ���������
};

class Invoice : public Document { // ����� ���������
public:
    Invoice();
    Invoice(string, string, string, string, string);
    ~Invoice();
    void show_item() override;
protected:
    string goods; // ����������� �����, ��� ��������
    string provider; // ��������� ������
    string date_of_delivery; // ���� �������� ������
    static int invoice_count; // ���-�� ���������
};

class Check : public Document { // ����� ���
public:
    Check();
    Check(string, string, string, string, double);
    ~Check();
    void show_item() override;
protected:
    string payee; // �������������
    string drawer; // ����������
    double amount; // ����, ��������� � ����
    static int check_count;
};

#endif