# Password Generator

This is a Python script that generates passwords based on specified criteria. It uses the `argparse` module to handle command line arguments, and `secrets` and `random` modules to generate random password strings.

## How to use

python.exe password-generator.py [-h] [-n ANGKA] [-l HURUF-KECIL] [-u HURUF-BESAR] [-s KARAKTER-KHUSUS] [-t TOTAL-PANJANG] [-a JUMLAH] [-o FILE-OUTPUT]

```bash
python password-generator.py -n 2 -l 3 -u 1 -s 1 -t 10 -a 2 -o passwords.txt

```

### Arguments

`-n`, `--angka`: The number of digits in the password (default: 0)

`-l`, `--huruf-kecil`: The number of lowercase letters in the password (default: 0)

`-u`, `--huruf-besar`: The number of uppercase letters in the password (default: 0)

`-s`, `--karakter-khusus`: The number of special characters in the password (default: 0)

`-t`, `--total-panjang`: The total length of the password. If specified, overrides the individual criteria arguments (default: None)

`-a`, `--jumlah`: The number of passwords to generate (default: 1)

`-o`, `--file-output`: The path to the output file. If specified, saves the passwords to a file (default: None)

Note: If both `-t` and individual criteria arguments are provided, the script will generate passwords that meet both criteria.

## Examples

1. Generate 5 passwords with 8 digits each:
`python password_generator.py -n 8 -a 5`

2. Generate a password with a total length of 12 characters, including 2 digits, 6 lowercase letters, and 4 special characters:
`python password_generator.py -t 10`

3. Generate a password with a total length of 10 characters, ignoring individual criteria arguments:
`python password_generator.py -n 8 -a 3 -o passwords.txt`

4. Generate 3 passwords and save them to a file named "passwords.txt":
