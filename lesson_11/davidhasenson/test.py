
# with open("lesson_11/davidhasenson/person.csv", "r") as file:
#     nr_records = 0
#     for row in file:
#         cur.execute("INSERT INTO persons VALUES (?,?,?,?,?)", row.split(","))
#         conn.commit()
#         nr_records += 1
# conn.close()
# print("\n {} records transferred ".format(nr_records))