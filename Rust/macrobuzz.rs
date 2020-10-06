extern crate proc_macro;
use proc_macro2::TokenStream;
use quote::quote;

const MAX_FIZZBUZZ: u32 = 100;

#[proc_macro]
pub fn fizzbuzz(_input: proc_macro::TokenStream) -> proc_macro::TokenStream {
    let precomputed: Vec<TokenStream> = (1..=MAX_FIZZBUZZ).map(|num| {
        if num % 3 == 0 && num % 5 == 0 {
            quote! {
                #num => println!("FizzBuzz")
            }
        } else if num % 3 == 0 {
            quote! {
                #num => println!("Fizz")
            }
        } else if num % 5 == 0 {
            quote! {
                #num => println!("Buzz")
            }
        } else {
            let numstr = num.to_string();
            quote! {
                #num => println!(#numstr)
            }
        }
    }).collect();

    let output: proc_macro2::TokenStream = quote! {
        const MAX_FIZZBUZZ: u32 = #MAX_FIZZBUZZ;
        fn main() {
            (1..=MAX_FIZZBUZZ).for_each(|num: u32| {
                match num {
                    #(#precomputed),*
                    ,_ => panic!("Whoops")
                }
            });
        }
    };
    output.into()
}
