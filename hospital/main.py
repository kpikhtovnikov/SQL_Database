import db
import os


import datetime
def registratura():
    print('Вы зашли как работник регистратуры\n Выберите действие:')
    print('1. Адрес, дата заболевания, диагноз данного больного')
    print('2. ФИО лечащего врача больного')
    print('3. Номер кабинета, дни и часы приема данного врача')
    print('4. Больные, находяшиеся на лечении у данного врача')
    print('5. Симптомы заболевания и лечение')
    print('6. Выдать справку')
    print('7. Отчет')
    choose =input()
    if (choose == '1'):
        print("Введите ФИО:")
        fio = input()
        cur,count=db.query(
        "SELECT "
        "diagnosis_of_the_patient.DIAGNOSIS, patients.STREET, patients.HOME, diagnosis_of_the_patient.DATE, diagnosis_of_the_patient.patients_FIO "
        "from diagnosis_of_the_patient INNER "
        "JOIN "
        "patients "
        "on "
        "diagnosis_of_the_patient.patients_FIO = patients.FIO "
        "INNER "
        "JOIN "
        "adress_area "
        "ON "
        "patients.STREET = adress_area.STREET "
        "INNER "
        "JOIN "
        "doctors "
        "ON "
        "doctors.AREA = adress_area.AREA WHERE patients_FIO='"+fio+"'")
        if(count!=0):
            rows = cur.fetchall()
            for r in rows:
                print(r[0],r[3],r[4],r[1],r[2])
    if(choose=='2'):
        print("Введите ФИО:")
        fio = input()
        cur, count = db.query(
            "SELECT diagnosis_of_the_patient.DIAGNOSIS, doctors.DOCTOR_FIO, diagnosis_of_the_patient.DATE, diagnosis_of_the_patient.patients_FIO from diagnosis_of_the_patient INNER JOIN patients on diagnosis_of_the_patient.patients_FIO = patients.FIO INNER JOIN adress_area ON patients.STREET = adress_area.STREET INNER JOIN doctors ON doctors.AREA = adress_area.AREA WHERE patients_FIO = '" + fio + "'")
        print("Врач")
        if (count != 0):
            rows = cur.fetchall()
            for r in rows:
                print(r[1])
        else:
            print("Не найдено")
    if (choose == '3'):
        print("Введите ФИО:")
        fio = input()
        cur, count = db.query(
            "SELECT * FROM DOCTORS WHERE DOCTOR_FIO='"+fio+"'")
        if (count != 0):
            rows = cur.fetchall()
            for r in rows:
                print(r[1],r[2],r[3])
        else:
            print("Не найдено")
    if(choose=='4'):
        print("Введите ФИО:")
        fio =input()
        cur, count = db.query(  " SELECT * "
        " from patients INNER "
        " join "
        " adress_area "
        "on "
        " adress_area.STREET = patients.STREET "
        " where "
        " adress_area.AREA = (SELECT doctors.AREA from doctors WHERE doctors.DOCTOR_FIO='"+fio+"') ")
        print("Пациенты")
        if(count!=0):
            rows = cur.fetchall()
            for r in rows:
                print(r[0], r[1], r[2])
        else:
            print("Не найдено")
    if (choose == '5'):
        print("Введите заболевание:")
        bol = input()
        cur, count = db.query("SELECT * from description_disease where diagnosis = '"+bol+"'")
        if (count != 0):
            rows = cur.fetchall()
            print('Симптомы:')
            for r in rows:
                print(r[1])
        else:
            print("Не найдено")
        cur, count = db.query("SELECT * from medicaments where diagnosis = '" + bol + "'")
        if (count != 0):
            rows = cur.fetchall()
            print('Лечение:')
            for r in rows:
                print(r[1])
        else:
            print("Не найдено")
    if (choose == '6'):
        print('Ведите ФИО пациента:')
        fio = input()
        cur,count=db.query("SELECT diagnosis_of_the_patient.DIAGNOSIS, doctors.DOCTOR_FIO, diagnosis_of_the_patient.DATE, diagnosis_of_the_patient.patients_FIO from diagnosis_of_the_patient INNER JOIN patients on diagnosis_of_the_patient.patients_FIO = patients.FIO INNER JOIN adress_area ON patients.STREET = adress_area.STREET INNER JOIN doctors ON doctors.AREA = adress_area.AREA WHERE patients_FIO = '" + fio + "'")
        if (count != 0):
            rows = cur.fetchall()
            print(rows)
            for r in rows:
                my_file = open("справка.txt", "w")
                my_file.write("Пациент:\t"+r[3])
                my_file.write("\nДиагноз:\t"+r[0])
                my_file.write("\nВрач:\t" + r[1]+"\t Дата \t"+r[2].strftime('%m/%d/%Y'))
                my_file.close()
    if(choose=='7'):
        cur, count = db.query("SELECT COUNT(patients.FIO) FROM patients")
        if (count != 0):
            rows = cur.fetchall()
            print("Количество пациентов:")
            for r in rows:
                print(r[0])
        print("-----------------")
        cur, count = db.query(
        "SELECT "
        "count(FIO), doctors.DOCTOR_FIO "
        "from patients INNER "
        "join "
        "adress_area "
        "on "
        "patients.STREET = adress_area.STREET "
        "INNER "
        "JOIN "
        "doctors "
        "on "
        "doctors.AREA = adress_area.AREA "
        "GROUP "
        "by "
        "doctors.DOCTOR_FIO ")
        print("Количество пациентов у врачей:")
        if (count != 0):
            rows = cur.fetchall()
            print("Количество пациентов:")
            for r in rows:
                print(r[1]," - ",r[0])
        print("-----------------")
        cur, count = db.query(
        "SELECT "
        "COUNT(diagnosis_of_the_patient.FIO), diagnosis_of_the_patient.FIO "
        "FROM "
        "diagnosis_of_the_patient "
        "GROUP "
        "by "
        "diagnosis_of_the_patient.FIO ")
        print("Количество заболеваний:")
        if (count != 0):
            rows = cur.fetchall()
            for r in rows:
                print(r[1], " - ", r[0])
        print("-----------------")
        cur, count = db.query(
            "SELECT * FROM DOCTORS ")
        print("Расписание врачей:")
        if (count != 0):
            rows = cur.fetchall()
            for r in rows:
                print(r[1],r[2],r[3])
        print("-----------------")
    print('---------------------------------------------------')
    x.active=registratura()


def admin():
    print('Вы зашли как администратор \n Выберите действие:')
    print('1. Добавить пациента')
    print('2. Удалить пациента')
    print('3. Добавить Врача')
    print('4. Уволить Врача')
    print('5. Изменить диагноз')
    print('6. Создание нового пользователя')
    print('7. Удалить пользователя')
    choose =input()
    if(choose == '1'):
        print('Ведите ФИО пациента:')
        fio = input()
        print('Ведите улицу проживания пациента:')
        street = input()
        print('Ведите номер дома пациента:')
        num = input()
        db.query("INSERT INTO `patients` VALUES ('"+fio+"','"+street+"','"+num+"')")
        print('Пациент успешно добавлен')
        x.active = admin()
    if(choose == '2'):
        print('Ведите ФИО пациента:')
        fio = input()
        try:
            if(db.query("DELETE FROM `patients` WHERE FIO='"+fio+"'")[1]!=0):
                print('Успешно')
            else:
                print('Ничего не найдено')
        except Exception:
            print('Не выполнено')
        x.active = admin()
    if(choose=='4'):
        print('Ведите ФИО врача:')
        fio = input()
        try:
            if(db.query("DELETE FROM DOCTORS WHERE DOCTOR_FIO='"+fio+"'")[1]!=0):
                print('Успешно')
            else:
                print('Ничего не найдено')
        except Exception:
            print('Не выполнено')
        x.active = admin()
    if(choose=='5'):
        print('Ведите ФИО пациента:')
        fio = input()
        if(db.query("SELECT * FROM PATIENTS WHERE FIO = '"+fio+"'")[1]!=0):
            print('Ведите Диагноз:')
            dia = input()
            try:
                if (db.query("SELECT * FROM `diagnosis_of_the_patient` WHERE patients_FIO='"+fio+"'")[1] != 0):
                    db.query("UPDATE `diagnosis_of_the_patient` SET FIO='"+dia+"' WHERE patients_FIO='"+fio+"'")
                    print('Обновлено')
                else:
                    db.query("INSERT INTO `diagnosis_of_the_patient` (`FIO`, `DIAGNOSIS`, `patients_FIO`) VALUES('"+dia+"','"+dia+"','"+fio+"') ")
                    print('Добавлено')
            except Exception:
                print('Не выполнено')
            x.active = admin()

        else:
            print('Пациент не найден')

    if (choose=='6'):
        print("Введите логин")
        login = input()
        print("Введите пароль")
        password = input()
        print("Назначьте роль нового пользователя. Введите слово-'админ' или слово-'пользователь' ")
        role= input()
        if(role=='админ'):
            role='admin'
        elif(role=='пользователь'):
            role='regis'
        cur, count = db.query("SELECT User FROM mysql.user where User='"+login+"'")
        if(count!=0):
            print("Такой пользователь уже существует")
        else:
            if(role=='admin'):
                db.query("CREATE user '"+login+"'@'%' identified by '"+password+"'")
                db.query("GRANT SELECT, INSERT, DELETE, UPDATE, CREATE user on *.* TO '"+login+"'@'%' ")
                db.query("FLUSH PRIVILEGES;")
                db.query("INSERT INTO `accounts` VALUES ('"+login+"','"+password+"','"+role+"')")
            elif(role=='regis'):
                db.query("CREATE USER '"+login+"'@'%' identified by '"+password+"'")
                db.query("GRANT SELECT on mydb.* TO '"+login+"'@'%' ")
                db.query("FLUSH PRIVILEGES;")
                db.query("INSERT INTO `accounts` VALUES ('"+login+"','"+password+"','"+role+"')")
            cur, count = db.query("SELECT User FROM mysql.user where User='"+login+"'")
            if (count!=0):
                if (role=='admin'):
                    print('Админ успешно добавлен')
                elif(role=='regis'):
                    print('Пользователь успешно добавлен')
            elif(count==0):
                print('Не удалось добавить нового пользователя')
        print('---------------------------------------------------')
        x.active = admin()

    if (choose=='7'):
        print("Введите логин пользователя, которого хотите удалить")
        login = input()
        cur, count = db.query("SELECT User FROM mysql.user where User='"+login+"'")
        if(count==0):
            print("Такого пользователя не существует")
        elif(count!=0):
            db.query("DROP user '"+login+"'@'%' ")
            db.query("FLUSH PRIVILEGES;")
            db.query("DELETE FROM accounts where login='"+login+"'")
            cur, count = db.query("SELECT User FROM mysql.user where User='"+login+"'")
            if (count==0 ):
                print('Пользователь удален')
            elif(count!=0):
                print('Не удалось удалить пользователя')
        print('---------------------------------------------------')
        x.active = admin()



def greetings():
    print('Добро пожаловать')
    print('Пожалуйста, выполните вход в систему')
    print('Логин:')
    login=input()
    print('Пароль:')
    password=input()
    cur, count = db.query("SELECT * FROM accounts where login='"+login+"' and password='"+password+"'")
    if(count!=0):
        rows = cur.fetchall()
        for r in rows:
            if(r[2]=='admin'):
                print('---------------------------------------------------')
                x.active=admin()
            else:
                print('---------------------------------------------------')
                x.active=registratura()

    else:
        print("Неверный логин или пароль")
        print('---------------------------------------------------')
        x.active=greetings()


class menu():
    def __init__(self):
        self.active = greetings()

x = menu()
while True:
    x.active
