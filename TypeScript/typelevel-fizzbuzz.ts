/* 
  It is proven that TypeScript Type System is Turing Complete 
  (https://gist.github.com/hediet/63f4844acf5ac330804801084f87a6d4 and https://github.com/microsoft/TypeScript/issues/14833)
  which means it is possible to implement FizzBuzz in TypeScript on Type Level entirely

  Below you can find such implementation,
  it should be easy to understand if you are experienced with logic programming.
  You can copy this code to TypeScript Playground (tested with v4.0.2)
  and check the types yourself by hovering the mouse above test types (T1 ... T30)
  
  Author: @minajevs
*/

/*
  Boolean algebra
*/

type True = 'true'
type False = 'false'

type Bool = False | True

type If<Condition extends Bool, Then, Else> = {
  'true': Then
  'false': Else
}[Condition]

type And<Condition1 extends Bool, Cond2 extends Bool> = If<Condition1, Cond2, False>

/*
  Natural Numbers
*/

type Zero = { zero: True }

type NaturalNumber = Zero | { zero: False, previousNumber: NaturalNumber }

type NextNumber<Number extends NaturalNumber> = { zero: False, previousNumber: Number }
type PreviousNumber<Number extends NaturalNumber> =
  Number extends NextNumber<NaturalNumber>
  ? Number['previousNumber']
  : Zero

type IsZero<Number extends NaturalNumber> = Number['zero']

/* 
  Natural number algebra
*/

// Recursive compare if Number1 is less or equal than Number2
type LessThanOrEqual<Number1 extends NaturalNumber, Number2 extends NaturalNumber> = {
  // If both numbers are 0 - True
  'true': IsZero<Number2>
  // If Number1 is positive and Number2 is 0 - False, else - compare Number1-1 and Number2-1
  'false': If<IsZero<Number2>, False, LessThanOrEqual<PreviousNumber<Number1>, PreviousNumber<Number2>>>
}[IsZero<Number1>]

// Compare if two numbers are equal
type NumbersEqual<Number1 extends NaturalNumber, Number2 extends NaturalNumber> =
  // If Number1 ≤ Number2 and Number2 ≤ Number1, then Number1 = Number2
  // @ts-ignore Type instantiation is excessively deep and possibly infinite
  And<LessThanOrEqual<Number1, Number2>, LessThanOrEqual<Number2, Number1>>

// Recursively add one number to another
type Add<Number1 extends NaturalNumber, Number2 extends NaturalNumber> = {
  // Number1 + 0 = Number1
  'true': Number1
  // Number1 + Number2 = (Number1 + Number2 - 1) - 1
  'false': NextNumber<Add<Number1, PreviousNumber<Number2>>>
}[IsZero<Number2>]

// Recursively multiply numbers
type Multiply<Number1 extends NaturalNumber, Number2 extends NaturalNumber> = {
  // Number1 * 0 = 0
  'true': Zero
  // Number1 * Number2 = Number1 + Number1 * (Number2 - 1)
  // @ts-ignore Type instantiation is excessively deep and possibly infinite
  'false': Add<Number1, Multiply<Number1, PreviousNumber<Number2>>>
}[IsZero<Number2>]

// Recursively substract one number from another
type Substract<Number1 extends NaturalNumber, Number2 extends NaturalNumber> = {
  // Number1 - 0 = 0
  'true': Number1,
  // Number1 - Number2 = (Number1 - 1) - (Number2 - 1)
  'false': Substract<PreviousNumber<Number1>, PreviousNumber<Number2>>
}[IsZero<Number2>]

// Safely substract one number from 
type SafeSubstractionResult<IsOverflowing extends Bool, Result extends NaturalNumber> = {
  isOverflowing: IsOverflowing
  result: Result
}

type SafeSubstract<Number1 extends NaturalNumber, Number2 extends NaturalNumber> = {
  // Number1 - 0 = Number1, no overflow 
  'true': SafeSubstractionResult<'false', Number1>,
  'false': {
    // 0 - Number2 = 0, overflowing to negative
    'true': SafeSubstractionResult<'true', Number1>,
    // Number1 - Number2 = (Number1 - 1) - (Number2 - 1)
    'false': SafeSubstract<PreviousNumber<Number1>, PreviousNumber<Number2>>
  }[IsZero<Number1>]
}[IsZero<Number2>]

// Recursively calculate remainder of Number1 division by Number2
type Mod<Number1 extends NaturalNumber, Number2 extends NaturalNumber> = {
  // 0 % Number2 = 0
  'true': Zero,
  // Number1 % Number2 = (Number1 - Number2) % Number2
  // @ts-ignore Type instantiation is excessively deep and possibly infinite
  'false': _Mod<Number1, Number2, SafeSubstract<Number1, Number2>>
}[IsZero<Number1>]

type _Mod<Number1 extends NaturalNumber, Number2 extends NaturalNumber, Result extends SafeSubstractionResult<Bool, NaturalNumber>> = {
  // Number1 < 0, return Number1
  'true': Number1,
  // Number1 >= 0, return (Number1 - Number2) % Number2 
  'false': Mod<Result['result'], Number2>
}[Result['isOverflowing']]

/*
  Natural number declaration 
*/
type _0 = Zero
type _1 = NextNumber<_0>
type _2 = NextNumber<_1>
type _3 = NextNumber<_2>
type _4 = NextNumber<_3>
type _5 = NextNumber<_4>
type _6 = NextNumber<_5>
type _7 = NextNumber<_6>
type _8 = NextNumber<_7>
type _9 = NextNumber<_8>
type _10 = NextNumber<_9>
type _11 = NextNumber<_10>
type _12 = NextNumber<_11>
type _13 = NextNumber<_12>
type _14 = NextNumber<_13>
type _15 = NextNumber<_14>
type _16 = NextNumber<_15>
type _17 = NextNumber<_16>
type _18 = NextNumber<_17>
type _19 = NextNumber<_18>
type _20 = NextNumber<_19>
type _21 = NextNumber<_20>
type _22 = NextNumber<_21>
type _23 = NextNumber<_22>
type _24 = NextNumber<_23>
type _25 = NextNumber<_24>
type _26 = NextNumber<_25>
type _27 = NextNumber<_26>
type _28 = NextNumber<_27>
type _29 = NextNumber<_28>
type _30 = NextNumber<_29>

/*
  FizzBuzz implementation
*/

// Check if Number1 is divisable by Number2 
type Divisable<Number1 extends NaturalNumber, Number2 extends NaturalNumber> =
  // @ts-ignore Type instantiation is excessively deep and possibly infinite
  NumbersEqual<Mod<Number1, Number2>, _0>

type FizzBuzz<Number extends NaturalNumber> =
  Divisable<Number, _15> extends True ? 'FizzBuzz' :
  Divisable<Number, _5> extends True ? 'Buzz' :
  Divisable<Number, _3> extends True ? 'Fizz' :
  Number

/*
  Test
*/
// Assert both types are equal
type AssertEqual<T1, T2 extends T1> = T1

type T1 = AssertEqual<FizzBuzz<_1>, _1>
type T2 = AssertEqual<FizzBuzz<_2>, _2>
type T3 = AssertEqual<FizzBuzz<_3>, 'Fizz'>
type T4 = AssertEqual<FizzBuzz<_4>, _4>
type T5 = AssertEqual<FizzBuzz<_5>, 'Buzz'>
type T6 = AssertEqual<FizzBuzz<_6>, 'Fizz'>
type T7 = AssertEqual<FizzBuzz<_7>, _7>
type T8 = AssertEqual<FizzBuzz<_8>, _8>
type T9 = AssertEqual<FizzBuzz<_9>, 'Fizz'>
type T10 = AssertEqual<FizzBuzz<_10>, 'Buzz'>
type T11 = AssertEqual<FizzBuzz<_11>, _11>
type T12 = AssertEqual<FizzBuzz<_12>, 'Fizz'>
type T13 = AssertEqual<FizzBuzz<_13>, _13>
type T14 = AssertEqual<FizzBuzz<_14>, _14>
type T15 = AssertEqual<FizzBuzz<_15>, 'FizzBuzz'>
type T16 = AssertEqual<FizzBuzz<_16>, _16>
type T17 = AssertEqual<FizzBuzz<_17>, _17>
type T18 = AssertEqual<FizzBuzz<_18>, 'Fizz'>
type T19 = AssertEqual<FizzBuzz<_19>, _19>
type T20 = AssertEqual<FizzBuzz<_20>, 'Buzz'>
type T21 = AssertEqual<FizzBuzz<_21>, 'Fizz'>
type T22 = AssertEqual<FizzBuzz<_22>, _22>
type T23 = AssertEqual<FizzBuzz<_23>, _23>
type T24 = AssertEqual<FizzBuzz<_24>, 'Fizz'>
type T25 = AssertEqual<FizzBuzz<_25>, 'Buzz'>
type T26 = AssertEqual<FizzBuzz<_26>, _26>
type T27 = AssertEqual<FizzBuzz<_27>, 'Fizz'>
type T28 = AssertEqual<FizzBuzz<_28>, _28>
type T29 = AssertEqual<FizzBuzz<_29>, _29>
type T30 = AssertEqual<FizzBuzz<_30>, 'FizzBuzz'>