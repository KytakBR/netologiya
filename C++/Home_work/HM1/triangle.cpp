#include <iostream>
#include <cmath>

using namespace std;

int main () {
    
    float xa, ya, xb, yb, xc, yc, l1, l2, l3, s, p;
    
    cout << "Введите xa: " << endl;
    cin >> xa;
    cout << "Введите ya: " << endl;
    cin >> ya;
    cout << "Введите xb: " << endl;
    cin >> xb;
    cout << "Введите yb: " << endl;
    cin >> yb;
    cout << "Введите xc: " << endl;
    cin >> xc;
    cout << "Введите yc: " << endl;
    cin >> yc;
    
    l1 = sqrt(pow((xb-xa), 2) + pow((yb-ya), 2));
    l2 = sqrt(pow((xc-xb), 2) + pow((yc-yb), 2));
    l3 = sqrt(pow((xa-xc), 2) + pow((ya-yc), 2));
    p = l1 + l2 + l3;
    s = (abs((xb-xa)*(yc-ya)-(xc-xa)*(yb-ya)))/2;
    cout << "Периметр заданного треугольника равна: " << p << endl;
    cout << "Площадь заданного треугольника равна: " << s << endl;
    
    return 0;
}
    

