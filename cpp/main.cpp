#include <iostream>
#include <string>
using namespace std;


template <class elemType>
class list{
    public:
    virtual void clear() = 0;
    virtual int length() const = 0;
    virtual void insert(const elemType &x) = 0;
    virtual void remove(int i) = 0;
    virtual int search(const elemType &x) const = 0;
    virtual elemType visit(int i) const = 0;
    virtual void traverse() const = 0;
    virtual ~list() {}
};

int main()
{
    string user_name;
    int usr_val;
    int num_tries(0);
    int num_right = 0;
    double usr_score = 0.0;
    char usr_more;
    bool go_for_it = true;
    const int MAX_TRIES = 5;

    cout << "Try another sequence? (y/n): ";
    cin >> usr_more;

    return 0;
}
