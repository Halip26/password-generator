from argparse import ArgumentParser
import secrets
import random
import string

# Persiapan Argument Parser
parser = ArgumentParser(
    prog="Generator Password",
    description="Menghasilkan password dengan menggunakan alat ini.",
)

# Menambahkan argumen ke dalam parser
parser.add_argument(
    "-n", "--angka", default=0, help="Jumlah digit dalam password", type=int
)
parser.add_argument(
    "-l", "--huruf-kecil", default=0, help="Jumlah huruf kecil dalam password", type=int
)
parser.add_argument(
    "-u", "--huruf-besar", default=0, help="Jumlah huruf besar dalam password", type=int
)
parser.add_argument(
    "-s",
    "--karakter-khusus",
    default=0,
    help="Jumlah karakter khusus dalam password",
    type=int,
)

# Menambahkan argumen total panjang password
parser.add_argument(
    "-t",
    "--total-panjang",
    type=int,
    help="Panjang total password. Jika diisi, akan mengabaikan -n, -l, -u, dan -s, "
    "serta menghasilkan password yang benar-benar acak dengan panjang yang ditentukan",
)

# Jumlah password harus berupa bilangan, jadi kita periksa apakah bertipe int.
parser.add_argument("-a", "--jumlah", default=1, type=int)
parser.add_argument("-o", "--file-output")

# Parsing argumen dari baris perintah.
args = parser.parse_args()

# Daftar password
passwords = []
# Melakukan perulangan sejumlah jumlah password.
for _ in range(args.jumlah):
    if args.total_panjang:
        # Menghasilkan password acak dengan panjang total_panjang
        passwords.append(
            "".join(
                [
                    secrets.choice(
                        string.digits + string.ascii_letters + string.punctuation
                    )
                    for _ in range(args.total_panjang)
                ]
            )
        )
    else:
        password = []
        # Jika / berapa banyak angka yang harus dimasukkan dalam password
        for _ in range(args.angka):
            password.append(secrets.choice(string.digits))

        # Jika / berapa banyak huruf besar yang harus dimasukkan dalam password
        for _ in range(args.huruf_besar):
            password.append(secrets.choice(string.ascii_uppercase))

        # Jika / berapa banyak huruf kecil yang harus dimasukkan dalam password
        for _ in range(args.huruf_kecil):
            password.append(secrets.choice(string.ascii_lowercase))

        # Jika / berapa banyak karakter khusus yang harus dimasukkan dalam password
        for _ in range(args.karakter_khusus):
            password.append(secrets.choice(string.punctuation))

        # Mengacak daftar berisi semua huruf, angka, dan simbol yang mungkin.
        random.shuffle(password)

        # Mengambil huruf-huruf pada string hingga mencapai panjang argument dan menggabungkannya.
        password = "".join(password)

        # Menambahkan password ini ke daftar password keseluruhan.
        passwords.append(password)

# Menyimpan password ke file .txt.
if args.file_output:
    with open(args.file_output, "w") as f:
        f.write("\n".join(passwords))

# Menampilkan password di layar
print("\n".join(passwords))
