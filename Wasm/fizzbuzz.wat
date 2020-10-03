;; FizzBuzz in hand-written Wasm
;; Author: @nlordell

;; A WASI-compliant WebAssembly FizzBuzz implementation. In order to run, use a
;; WASI-compliant runtime such as [Wasmtime](https://wasmtime.dev/).
;;
;; ```
;; wasmtime fizzbuz.wat
;; ```

(module
  ;; In order to print the fizzbuzz for each number, we need to use a host
  ;; import that allows us to write to stdout. `fd_write`, which is the WASI
  ;; `writev` equivalent, and perfect for the job!
  ;;
  ;; It is declared as:
  ;;
  ;; ```c
  ;; __wasi_errno_t __wasi_fd_write(
  ;;   __wasi_fd_t fd,
  ;;   const __wasi_ciovec_t *iovs,
  ;;   size_t iovs_len,
  ;;   __wasi_size_t *nwritten
  ;; );
  ;; ```
  (import "wasi_snapshot_preview1" "fd_write"
    (func $__wasi_fd_write (param i32 i32 i32 i32) (result i32))
  )

  ;; Declare and export memory.
  ;;
  ;; The Wasm memory is used to keep our string data for fizzbuzz and integer to
  ;; string conversion. It needs to be exported so that the host can read the
  ;; the data to print to stdout.
  (memory (export "memory") 1)

  ;; Prepare data for `fd_write` WASI call. Specifically, it uses an `iovec`
  ;; to describe the buffers to be written. They are laid out as:
  ;;
  ;; ```c
  ;; struct __wasi_ciovec_t {
  ;;   const uint8_t * buf;
  ;;   __wasi_size_t buf_len;
  ;; }
  ;; ```
  ;;
  ;; For our fizzbuzz implementation, we want to use 2, one for the fizzbuzz
  ;; result for each number (i.e. "fizz", "11", etc.) and one for the newline.
  ;; We prepare the data before hand so the method for computing the the result
  ;; per number just needs to fill in the string and length.
  ;;
  ;; The following definitions roughly correspond to:
  ;;
  ;; ```
  ;; $iovs = {
  ;;   { .buf =    0, .buf_len = 0 }
  ;;   { .buf = 0x24, .buf_len = 1 }
  ;; }
  ;; *(0x24) = '\0a'
  ;; ```
  (data (i32.const 8) "\00\00\00\00\00\00\00\00\18\00\00\00\01\00\00\00\0a")
  (global $iovs i32 (i32.const 8))     ;; note don't start at 0 since thats `NULL`
  (global $iovs_len i32 (i32.const 2))

  ;; The file descriptor for stdout is 1.
  (global $stdout i32 (i32.const 1))

  ;; Prints the string currently stored in the shared `iovs` to stdout.
  ;;
  ;; This function traps if writing to stdout fails.
  (func $print
    (local $pnwritten i32)
    (local.set $pnwritten (i32.const 2048))

    (call $__wasi_fd_write
      (global.get $stdout)
      (global.get $iovs)
      (global.get $iovs_len)
      (local.get $pnwritten)
    )
    (if
      (i32.or
        (i32.ne (i32.const 0))                  ;; non-zero exit code
        (i32.ne                                 ;; not all bytes written
          (i32.load (local.get $pnwritten))
          (i32.add
            (i32.load (global.get $plen))
            (i32.const 1)                       ;; add 1 for newline
          )
        )
      )
      ;; the write to stdout failed, so trap
      (then unreachable)
    )
  )

  ;; ASCII encoded data for printing the fizzbuzz.
  (data (i32.const 128) "fizzbuzz")
  (global $fizz i32 (i32.const 128))
  (global $buzz i32 (i32.const 132))
  (global $ascii_zero i32 (i32.const 0x30))

  (global $pbuf i32 (i32.const 8))  ;; pointer to buffer field of first `iovec`
  (global $plen i32 (i32.const 12)) ;; pointer to length field of first `iovec`

  ;; Writes the fizzbuzz for a number to memory so that it can be printed.
  (func $fizzbuzz (param $x i32)
    (local $itoa i32)
    (local $ndigits i32)

    (if (i32.eqz
      (i32.rem_u
        (local.get $x)
        (i32.const 15)
      )
    ) (then
      (i32.store (global.get $pbuf) (global.get $fizz))
      (i32.store (global.get $plen) (i32.const 8))
    )
    (else (if (i32.eqz
      (i32.rem_u
        (local.get $x)
        (i32.const 5)
      )
    ) (then
      (i32.store (global.get $pbuf) (global.get $buzz))
      (i32.store (global.get $plen) (i32.const 4))
    )
    (else (if (i32.eqz
      (i32.rem_u
        (local.get $x)
        (i32.const 3)
      )
    ) (then
      (i32.store (global.get $pbuf) (global.get $fizz))
      (i32.store (global.get $plen) (i32.const 4))
    )
    (else
      ;; Write the number backwards, note that 10 is the maximum number of
      ;; digits a u32 can hold.
      (local.set $itoa (i32.const 1034))
      (local.set $ndigits (i32.const 0))

      (loop
        (local.set $itoa (i32.sub (local.get $itoa) (i32.const 1)))
        (local.set $ndigits (i32.add (local.get $ndigits) (i32.const 1)))

        (i32.store8 (local.get $itoa)
          (i32.add
            (global.get $ascii_zero)
            (i32.rem_u (local.get $x) (i32.const 10))
          )
        )

        (local.set $x (i32.div_u (local.get $x) (i32.const 10)))
        (br_if 0 (i32.ne (local.get $x) (i32.const 0)))
      )

      (i32.store (global.get $pbuf) (local.get $itoa))
      (i32.store (global.get $plen) (local.get $ndigits))
    ))))))
  )

  ;; WASI start function.
  (func (export "_start")
    (local $n i32)
    (local.set $n (i32.const 0))

    (loop
      (local.set $n (i32.add (local.get $n) (i32.const 1)))
      (call $fizzbuzz (local.get $n))
      (call $print)
      (br_if 0 (i32.lt_u (local.get $n) (i32.const 100)))
    )
  )
)
