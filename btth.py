employee_amount = int(
    input("Nhap so luong nhan vien: ")
)
for i in range(1, employee_amount + 1):
    print(f"Nhap thong tin nhan vien thu {i}")
    employee_name = input(
        "Nhap ten nhan vien: "
    )
    working_days = int(
        input("Nhap so ngay lam viec (0 -> 22): ")
    )
    if working_days < 0 or working_days > 22:
        print("Du lieu khong hop le")
        continue
    if working_days == 0:
        print("Nhan vien nghi toan bo thang")
    print("Bieu do ngay lam viec:")
    for row in range(1):
        for star in range(working_days):
            print("*", end="")
    print()
    if working_days >= 18:
        work_status = "Lam viec cham chi"
    elif working_days < 10:
        work_status = "Lam viec it"
    else:
        work_status = "Lam viec binh thuong"
    print("Ten nhan vien :", employee_name)
    print("So ngay lam   :", working_days)
    print("Danh gia      :", work_status)