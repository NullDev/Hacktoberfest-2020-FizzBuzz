(*
  Coq solution from someone who has no clue
  Author: @CRTified
*)
Require Import List.
Require Import Strings.String.
Require Import Strings.Ascii.


Open Scope char_scope.

Definition digitToStr n : ascii :=
  match n with
  | 0 => "0"
  | 1 => "1"
  | 2 => "2"
  | 3 => "3"
  | 4 => "4"
  | 5 => "5"
  | 6 => "6"
  | 7 => "7"
  | 8 => "8"
  | _ => "9"
  end.


Fixpoint natToStr (time n: nat) (acc: string) : string :=
  let acc' := String (digitToStr (Nat.modulo n 10)) acc in
  match time with
  | 0 => acc'
  | S time' => match (Nat.div n 10) with
               | 0 => acc'
               | n' => natToStr time' n' acc'
               end
 end.


Definition cfizz x := Nat.modulo x 3.
Definition cbuzz x := Nat.modulo x 5.
Definition cfizzbuzz x := Nat.modulo x 15.

Definition fizzle x :=
    match x with
    | 0 => ""%string
    | _ =>
      match cfizzbuzz x with
      | 0 => "FizzBuzz"%string
      | _ => match cfizz x with
             | 0 => "Fizz"%string
             | _ => match cbuzz x with
                    | 0 => "Buzz"%string
                    | _ => natToStr x x ""
                    end
             end
      end
    end.


Import ListNotations.

Fixpoint fizzleList (time: nat) (l: list nat) (acc: string) : string :=
  let acc' := String.append (String.append acc " ") (fizzle (List.hd 0 l)) in
  match time with
  | 0 => acc'
  | S time' =>
    match l with
    | [] => acc'
    | _ => fizzleList time' (List.tl l) acc'
    end
  end.

Compute fizzleList 100 (seq 1 100) "".
