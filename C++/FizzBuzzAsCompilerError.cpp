/*
   This code will never compile. Instead it will output FizzBuzz as a compiler error.
*/

#include <iostream>

#define BOOST_MPL_CFG_NO_PREPROCESSED_HEADERS
#define BOOST_MPL_LIMIT_VECTOR_SIZE 110

#include "boost/mpl/if.hpp"
#include "boost/mpl/int.hpp"
#include "boost/mpl/vector.hpp"
#include "boost/mpl/push_back.hpp"

using namespace std;
using namespace boost::mpl;

struct Fizz{};
struct Buzz{};
struct FizzBuzz{};

template<int i>
struct RunFizzBuzz
{
   typedef vector<int_<i> > Number;

   typedef typename if_c<(i % 3 == 0) && (i % 5 == 0), FizzBuzz, 
                    typename if_c<i % 3 == 0, Fizz,
                             typename if_c<i % 5 == 0, Buzz, Number>::type>::type >::type t1;

   typedef typename push_back<typename RunFizzBuzz<i - 1>::ret, t1>::type ret;
};
template<>
struct RunFizzBuzz<0> // Terminate the recusion.
{
   typedef vector<int_<0> > ret;
};
int main()
{
   typedef RunFizzBuzz<100>::ret::compilation_error_here res;
} 
