#include <iostream>
#include <sstream>
using namespace std;

class Student
{
    private:
      int age, std;
      string f_name, l_name;
    public:
        void set_age(int x)
        {age = x;}
        void set_first_name(string xy)
        {f_name = xy;}
        void set_last_name(string xxy)
        {l_name = xxy;}
        void set_standard(int xxyy)
        {std = xxyy;}
        int get_age()
        {return age;}
        string get_first_name()
        {return f_name;}
        string get_last_name()
        {return l_name;}
        int get_standard()
        {return std;}
        string to_string()
        {
            stringstream s1, s2;
            s1 << age; s2 << std;
            string ss1, ss2;
            s1>>ss1; s2>>ss2;
            string ss = ss1+","+f_name+","+l_name+","+ss2;
            return ss;
        }
};

int main() {
    int age, standard;
    string first_name, last_name;
    
    cin >> age >> first_name >> last_name >> standard;
    
    Student st;
    st.set_age(age);
    st.set_standard(standard);
    st.set_first_name(first_name);
    st.set_last_name(last_name);
    
    cout << st.get_age() << "\n";
    cout << st.get_last_name() << ", " << st.get_first_name() << "\n";
    cout << st.get_standard() << "\n";
    cout << "\n";
    cout << st.to_string();
    
    return 0;
}
