#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int sumOfDigits(long long n) {
    int sum = 0;
    while (n > 0) {
        sum += n % 10;
        n /= 10;
    }
    return sum;
}

int main(){
    
    int n;
    cin >> n;
    
    string hexRepresentation;
    int temp = n;
    while (temp > 0) {
        int remainder = temp % 16;
        if (remainder < 10){
            hexRepresentation += char('0' + remainder);
        }
        else {
            hexRepresentation += char('A' + remainder - 10);
        }
        temp /= 16;
    }
    reverse(hexRepresentation.begin(), hexRepresentation.end());
    
    char maxHexDigit = *max_element(hexRepresentation.begin(), hexRepresentation.end());
    
    if ('0' <= maxHexDigit && maxHexDigit <= '9') {
            n *= 2;
    } 
    else if (maxHexDigit == 'A' || maxHexDigit == 'D') {
            n /= 10;
    } 
    else if (maxHexDigit == 'B' || maxHexDigit == 'C') {
        string decimalRepresentation = to_string(n);
        if (decimalRepresentation.size() > 1) {
            swap(decimalRepresentation[0], decimalRepresentation.back());
            n = stoll(decimalRepresentation);
        }
    } 
    else if (maxHexDigit == 'E') {
        n += 1;
    } 
    else if (maxHexDigit == 'F') {
        n += sumOfDigits(n);
    }
    cout << n << endl;
    return 0;
}